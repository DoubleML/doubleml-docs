.. _learners:

Learners, hyperparameters and hyperparameter tuning
-----------------------------------------------------------

The estimation of a double/debiased machine learning model involves the estimation of several nuisance function with
machine learning estimators.
Such learners are implemented in various Python and R packages.
The implementation of :ref:`DoubleML <doubleml_package>` is based on the meta-packages
`scikit-learn <https://scikit-learn.org/>`_ for Python and `mlr3 <https://mlr3.mlr-org.com/>`_ for R.
The interfaces to specify the learners, set hyperparameters and tune hyperparameters are described in the following
separately for :ref:`Python <learners_python>` and :ref:`R <learners_r>`.

.. _learners_python:

Python: Learners and hyperparameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Minimum requirements for learners
#################################

The minimum requirement for a learner to be used for nuisance models in the :ref:`DoubleML <doubleml_package>`
package is

    * The implementation of a ``fit()`` and ``predict()`` method.
      Some models, like :py:class:`doubleml.DoubleMLIRM` and :py:class:`doubleml.DoubleMLIIVM` require classifiers.
    * In case of classifiers, the learner needs to come with a ``predict_proba()`` instead of, or in addition to, a
      ``predict()`` method, see for example :py:meth:`sklearn.ensemble.RandomForestClassifier.predict_proba`.
    * In order to be able to use the ``set_ml_nuisance_params()`` method of :ref:`DoubleML <doubleml_package>` classes the
      learner additionally needs to come with a ``set_params()`` method,
      see for example :py:meth:`sklearn.ensemble.RandomForestRegressor.set_params`.
    * We further rely on the function :py:func:`sklearn.base.clone` which adds the requirement of a ``get_params()``
      method for a learner in order to be used for nuisance models of :ref:`DoubleML <doubleml_package>` model classes.

Most learners from `scikit-learn <https://scikit-learn.org/>`_ satisfy all these minimum requirements.

Specifying learners and set hyperparameters
###########################################

The learners are set during initialization of the :ref:`DoubleML <doubleml_package>` model classes
:py:class:`doubleml.DoubleMLPLR`, :py:class:`doubleml.DoubleMLPLIV`,
:py:class:`doubleml.DoubleMLIRM` and :py:class:`doubleml.DoubleMLIIVM`.
Lets simulate some data and consider the partially linear regression model.
We need to specify learners for the nuisance functions :math:`g_0(X) = E[Y|X]` and :math:`m_0(X) = E[D|X]`,
for example :py:class:`sklearn.ensemble.RandomForestRegressor`.

.. tabbed:: Python

    .. ipython:: python

        import doubleml as dml
        from doubleml.datasets import make_plr_CCDDHNR2018
        from sklearn.ensemble import RandomForestRegressor

        np.random.seed(1234)
        ml_l = RandomForestRegressor()
        ml_m = RandomForestRegressor()
        data = make_plr_CCDDHNR2018(alpha=0.5, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m)
        dml_plr_obj.fit().summary

Without further specification of the hyperparameters, default values are used. To set hyperparameters:

    * We can also use pre-parametrized learners, like ``RandomForestRegressor(n_estimators=10)``.
    * Alternatively, hyperparameters can also be set after initialization via the method
      ``set_ml_nuisance_params(learner, treat_var, params)``


.. tabbed:: Python

    .. ipython:: python

        np.random.seed(1234)
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data,
                                      RandomForestRegressor(n_estimators=10),
                                      RandomForestRegressor())
        print(dml_plr_obj.fit().summary)

        np.random.seed(1234)
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data,
                                      RandomForestRegressor(),
                                      RandomForestRegressor())
        dml_plr_obj.set_ml_nuisance_params('ml_l', 'd', {'n_estimators': 10});
        print(dml_plr_obj.fit().summary)

Setting treatment-variable-specific or fold-specific hyperparameters:

    * In the multiple-treatment case, the method ``set_ml_nuisance_params(learner, treat_var, params)`` can be used to set
      different hyperparameters for different treatment variables.
    * The method ``set_ml_nuisance_params(learner, treat_var, params)`` accepts dicts and lists for ``params``.
      A dict should be provided if for each fold the same hyperparameters should be used.
      Fold-specific parameters are supported. To do so,  provide a nested list as ``params``, where the outer list is of
      length ``n_rep`` and the inner list of length ``n_folds``.


Hyperparameter tuning
#####################

Parameter tuning of learners for the nuisance functions of :ref:`DoubleML <doubleml_package>` models can be done via
the ``tune()`` method.
To illustrate the parameter tuning, we generate data from a sparse partially linear regression model.

.. tabbed:: Python

    .. ipython:: python

        import doubleml as dml
        import numpy as np

        np.random.seed(3141)
        n_obs = 200
        n_vars = 200
        theta = 3
        X = np.random.normal(size=(n_obs, n_vars))
        d = np.dot(X[:, :3], np.array([5, 5, 5])) + np.random.standard_normal(size=(n_obs,))
        y = theta * d + np.dot(X[:, :3], np.array([5, 5, 5])) + np.random.standard_normal(size=(n_obs,))
        dml_data = dml.DoubleMLData.from_arrays(X, y, d)

The hyperparameter-tuning is performed using either an exhaustive search over specified parameter values
implemented in :class:`sklearn.model_selection.GridSearchCV` or via a randomized search implemented in
:class:`sklearn.model_selection.RandomizedSearchCV`.

.. tabbed:: Python

    .. ipython:: python

        import doubleml as dml
        from sklearn.linear_model import Lasso

        ml_l = Lasso()
        ml_m = Lasso()
        dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_l, ml_m)
        par_grids = {'ml_l': {'alpha': np.arange(0.05, 1., 0.1)},
                     'ml_m': {'alpha': np.arange(0.05, 1., 0.1)}}
        dml_plr_obj.tune(par_grids, search_mode='grid_search');
        print(dml_plr_obj.params)
        print(dml_plr_obj.fit().summary)

        np.random.seed(1234)
        par_grids = {'ml_l': {'alpha': np.arange(0.05, 1., 0.01)},
                     'ml_m': {'alpha': np.arange(0.05, 1., 0.01)}}
        dml_plr_obj.tune(par_grids, search_mode='randomized_search', n_iter_randomized_search=20);
        print(dml_plr_obj.params)
        print(dml_plr_obj.fit().summary)

Hyperparameter tuning can also be done with more sophisticated methods, like for example an iterative fitting along
a regularization path implemented in :py:class:`sklearn.linear_model.LassoCV`.
In this case the tuning should be done externally and the parameters can then be set via the
``set_ml_nuisance_params()`` method.

.. tabbed:: Python

    .. ipython:: python

        import doubleml as dml
        from sklearn.linear_model import LassoCV

        np.random.seed(1234)
        ml_l_tune = LassoCV().fit(dml_data.x, dml_data.y)
        ml_m_tune = LassoCV().fit(dml_data.x, dml_data.d)

        ml_l = Lasso()
        ml_m = Lasso()
        dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_l, ml_m)
        dml_plr_obj.set_ml_nuisance_params('ml_l', 'd', {'alpha': ml_l_tune.alpha_});
        dml_plr_obj.set_ml_nuisance_params('ml_m', 'd', {'alpha': ml_m_tune.alpha_});
        print(dml_plr_obj.params)
        print(dml_plr_obj.fit().summary)


.. TODO: Also discuss other specification options like `tune_on_folds` or `scoring_methods`.

Evaluate learners
#################

To compare different learners it is possible to evaluate the out-of-sample performance of each learner. The ``summary``
already shows the root mean squared error (RMSE) for each learner and each corresponding repetition of cross-fitting (``n_rep`` argument).

To illustrate the parameter tuning, we work with the following example.

.. tabbed:: Python

    .. ipython:: python

        import doubleml as dml
        from doubleml.datasets import make_plr_CCDDHNR2018
        from sklearn.ensemble import RandomForestRegressor

        np.random.seed(1234)
        ml_l = RandomForestRegressor()
        ml_m = RandomForestRegressor()
        data = make_plr_CCDDHNR2018(alpha=0.5, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m)
        dml_plr_obj.fit()
        print(dml_plr_obj)

The RMSEs of each learner are also stored in the ``rmses`` attribute.
Further, the ``evaluate_learners()`` method is allows to evalute customized evaluation metrics as e.g. the mean absolute error. 
The default option is still the RMSE for evaluation.

.. tabbed:: Python

    .. ipython:: python

        print(dml_plr_obj.rmses)
        print(dml_plr_obj.evaluate_learners())

To evaluate a customized metric one hass to define a ``callable``. For some models (e.g. the IRM model) it is important that
the metric can handle ``nan`` values as not all target values are known.   

.. tabbed:: Python

    .. ipython:: python

        from sklearn.metrics import mean_absolute_error

        def mae(y_true, y_pred):
            subset = np.logical_not(np.isnan(y_true))
            return mean_absolute_error(y_true[subset], y_pred[subset])

        dml_plr_obj.evaluate_learners(learners=['ml_l'], metric=mae)

A more detailed notebook on the choice of learners is available in the :ref:`example gallery <examplegallery>`.

.. _learners_r:

R: Learners and hyperparameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Minimum requirements for learners
#################################

The minimum requirement for a learner to be used for nuisance models in the :ref:`DoubleML <doubleml_package>` package is

    * The implementation as a learner for regression or classification in the `mlr3 <https://mlr3.mlr-org.com/>`_ package
      or its extension packages `mlr3learners <https://mlr3learners.mlr-org.com/>`_ and
      `mlr3extralearners <https://mlr3extralearners.mlr-org.com/>`_ . A guide on how to add a learner is provided in the
      `chapter on extending learners in the mlr3 book <https://mlr3book.mlr-org.com/extending.html#sec-extending-learners>`_ .
    * The `mlr3 <https://mlr3.mlr-org.com/>`_ package makes sure that the learners satisfy some core functionalities.
      To specify a specific learner in :ref:`DoubleML <doubleml_package>` users can pass objects of the class
      `Learner <https://mlr3.mlr-org.com/reference/Learner.html>`_. A fast way to construct these objects is to use the
      `mlr3 <https://mlr3.mlr-org.com/>`_  function `lrn() <https://mlr3.mlr-org.com/reference/mlr_sugar.html>`_.
      An introduction to learners in `mlr3 <https://mlr3.mlr-org.com/>`_  is provided in the `chapter on learners of the mlr3 book <https://mlr3book.mlr-org.com/basics.html#sec-learners>`_.
    * It is also possible to pass learners that have been constructed from a pipeline with the `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_
      package.
    * The models `DoubleML::DoubleMLIRM <https://docs.doubleml.org/r/stable/reference/DoubleMLIRM.html>`_ and
      `DoubleML::DoubleMLIIVM <https://docs.doubleml.org/r/stable/reference/DoubleMLIIVM.html>`_ require classifiers.
      Users can also specify classifiers in the `DoubleML::DoubleMLPLR <https://docs.doubleml.org/r/stable/reference/DoubleMLPLR.html>`_
      in cases with binary treatment variables.
    * Hyperparameters of learners can either be set at instantiation in `mlr3 <https://mlr3.mlr-org.com/>`_ or after
      instantiation using the ``set_ml_nuisance_params()`` method.


An interactive list of provided learners in the `mlr3 <https://mlr3.mlr-org.com/>`_ and extension packages can be found on the
`website of the mlr3extralearners package <https://mlr3extralearners.mlr-org.com/articles/learners/list_learners.html>`_.



Specifying learners and set hyperparameters
###########################################

The learners are set during initialization of the :ref:`DoubleML <doubleml_package>` model classes
`DoubleML::DoubleMLPLR <https://docs.doubleml.org/r/stable/reference/DoubleMLPLR.html>`_,
`DoubleML::DoubleMLPLIV <https://docs.doubleml.org/r/stable/reference/DoubleMLPLIV.html>`_ ,
`DoubleML::DoubleMLIRM <https://docs.doubleml.org/r/stable/reference/DoubleMLIRM.html>`_
and `DoubleML::DoubleMLIIVM <https://docs.doubleml.org/r/stable/reference/DoubleMLIIVM.html>`_.
Lets simulate some data and consider the partially linear regression model.
We need to specify learners for the nuisance functions :math:`g_0(X) = E[Y|X]` and :math:`m_0(X) = E[D|X]`,
for example `LearnerRegrRanger <https://mlr3learners.mlr-org.com/reference/mlr_learners_regr.ranger.html>`_
(``lrn("regr.ranger")``) for regression with random forests based on the  `ranger <https://github.com/imbs-hl/ranger>`_
package for R.

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)
        lgr::get_logger("mlr3")$set_threshold("warn")

        # set up a mlr3 learner
        learner = lrn("regr.ranger")
        ml_l = learner$clone()
        ml_m = learner$clone()
        set.seed(3141)
        data = make_plr_CCDDHNR2018(alpha=0.5, return_type='data.table')
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)
        dml_plr_obj$fit()
        dml_plr_obj$summary()

Without further specification of the hyperparameters, default values are used. To set hyperparameters:

    * We can also use pre-parametrized learners ``lrn("regr.ranger", num.trees=10)``.
    * Alternatively, hyperparameters can be set after initialization via the method
      ``set_ml_nuisance_params(learner, treat_var, params, set_fold_specific)``.

.. tabbed:: R

    .. jupyter-execute::

        set.seed(3141)
        ml_l = lrn("regr.ranger", num.trees=10)
        ml_m = lrn("regr.ranger")
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)
        dml_plr_obj$fit()
        dml_plr_obj$summary()

        set.seed(3141)
        ml_l = lrn("regr.ranger")
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l , ml_m)
        dml_plr_obj$set_ml_nuisance_params("ml_l", "d", list("num.trees"=10))
        dml_plr_obj$fit()
        dml_plr_obj$summary()

Setting treatment-variable-specific or fold-specific hyperparameters:

    * In the multiple-treatment case, the method ``set_ml_nuisance_params(learner, treat_var, params, set_fold_specific)``
      can be used to set different hyperparameters for different treatment variables.
    * The method ``set_ml_nuisance_params(learner, treat_var, params, set_fold_specific)`` accepts lists for ``params``.
      The structure of the list depends on whether the same parameters should be provided for all folds or separate values
      are passed for specific folds.
    * Global parameter passing: The values in ``params`` are used for estimation on all folds.
      The named list in the argument ``params`` should have entries with names corresponding to
      the parameters of the learners. It is required that option ``set_fold_specific`` is set to ``FALSE`` (default).
    * Fold-specific parameter passing: ``params`` is a nested list. The outer list needs to be of length ``n_rep`` and the inner
      list of length ``n_folds``. The innermost list must have named entries that correspond to the parameters of the learner.
      It is required that option ``set_fold_specific`` is set to ``TRUE``. Moreover, fold-specific
      parameter passing is only supported, if all parameters are set fold-specific.
    * External setting of parameters will override previously set parameters. To assert the choice of parameters, access the
      fields ``$learner`` and ``$params``.

.. tabbed:: R

    .. jupyter-execute::

        set.seed(3141)
        ml_l = lrn("regr.ranger")
        ml_m = lrn("regr.ranger")
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")

        n_rep = 2
        n_folds = 3
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, n_rep=n_rep, n_folds=n_folds)

        # Set globally
        params = list("num.trees"=10)
        dml_plr_obj$set_ml_nuisance_params("ml_l", "d", params=params)
        dml_plr_obj$set_ml_nuisance_params("ml_m", "d", params=params)
        dml_plr_obj$learner
        dml_plr_obj$params
        dml_plr_obj$fit()
        dml_plr_obj$summary()


The following example illustrates how to set parameters for each fold.

.. tabbed:: R

    .. jupyter-execute::

        learner = lrn("regr.ranger")
        ml_l = learner$clone()
        ml_m = learner$clone()
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, n_rep=n_rep, n_folds=n_folds)

        # Set values for each fold
        params_exact = rep(list(rep(list(params), n_folds)), n_rep)
        dml_plr_obj$set_ml_nuisance_params("ml_l", "d", params=params_exact,
                                             set_fold_specific=TRUE)
        dml_plr_obj$set_ml_nuisance_params("ml_m", "d", params=params_exact,
                                             set_fold_specific=TRUE)
        dml_plr_obj$learner
        dml_plr_obj$params
        dml_plr_obj$fit()
        dml_plr_obj$summary()


Using pipelines to construct learners
#####################################

Users can also specify learners that have been constructed from a pipeline using the `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_
package. In general, pipelines can be used to perform data preprocessing, feature selection, combine learners and even
to perform hyperparameter tuning. In the following, we provide two examples on how to construct a single learner and how
to stack different learners via a pipeline. For a more detailed introduction to `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_,
we refer to the `Pipelines Chapter in the mlr3book <https://mlr3book.mlr-org.com/pipelines.html>`_. Moreover, a
notebook on how to use `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_ in combination with :ref:`DoubleML <doubleml_package>`
is available in the example gallery.

.. tabbed:: R

    .. jupyter-execute::

        library(mlr3pipelines)

        set.seed(3141)
        # Define random forest learner in a pipeline
        single_learner_pipeline = po("learner", lrn("regr.ranger", num.trees = 10))

        # Use pipeline to create a new instance of a learner
        ml_g = as_learner(single_learner_pipeline)
        ml_m = as_learner(single_learner_pipeline)

        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")

        n_rep = 2
        n_folds = 3
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_g, ml_m, n_rep=n_rep, n_folds=n_folds)
        dml_plr_obj$learner
        dml_plr_obj$fit()
        dml_plr_obj$summary()

        set.seed(3141)
        # Define ensemble learner in a pipeline
        ensemble_learner_pipeline = gunion(list(
                po("learner", lrn("regr.cv_glmnet", s = "lambda.min")),
                po("learner", lrn("regr.ranger")),
                po("learner", lrn("regr.rpart", cp = 0.01)))) %>>%
            po("regravg", 3)

        # Use pipeline to create a new instance of a learner
        ml_g = as_learner(ensemble_learner_pipeline)
        ml_m = as_learner(ensemble_learner_pipeline)

        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")

        n_rep = 2
        n_folds = 3
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_g, ml_m, n_rep=n_rep, n_folds=n_folds)
        dml_plr_obj$learner
        dml_plr_obj$fit()
        dml_plr_obj$summary()


Hyperparameter tuning
#####################

Parameter tuning of learners for the nuisance functions of :ref:`DoubleML <doubleml_package>` models can be done via the ``tune()`` method.
The ``tune()`` method passes various options and parameters to the tuning interface provided by the
`mlr3tuning <https://mlr3tuning.mlr-org.com/>`_ package. The `mlr3 book <https://mlr3book.mlr-org.com/>`_ provides a
`step-by-step introduction to parameter tuning <https://mlr3book.mlr-org.com/optimization.html>`_.

To illustrate the parameter tuning, we generate data from a sparse partially linear regression model.

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(data.table)

        set.seed(3141)
        n_obs = 200
        n_vars = 200
        theta = 3
        X = matrix(stats::rnorm(n_obs * n_vars), nrow = n_obs, ncol = n_vars)
        d = X[, 1:3, drop = FALSE] %*% c(5, 5, 5) + stats::rnorm(n_obs)
        y = theta * d + X[, 1:3, drop = FALSE] %*% c(5, 5, 5)  + stats::rnorm(n_obs)
        dml_data = double_ml_data_from_matrix(X = X, y = y, d = d)

The hyperparameter-tuning is performed according to options passed through a named list ``tune_settings``.
The entries in the list specify options during parameter tuning with `mlr3tuning <https://mlr3tuning.mlr-org.com/>`_:

    * ``terminator`` is a `Terminator object <https://bbotk.mlr-org.com/reference/Terminator.html>`_ passed to
      `mlr3tuning <https://mlr3tuning.mlr-org.com/>`_ that manages the budget to solve the tuning problem.
    * ``algorithm`` is an object of class
      `Tuner <https://mlr3tuning.mlr-org.com/reference/Tuner.html>`_ and specifies the tuning algorithm.
      Alternatively, ``algorithm`` can be a ``character()`` that is used as an argument in the wrapper
      `mlr3tuning <https://mlr3tuning.mlr-org.com/>`_ call
      `tnr(algorithm) <https://mlr3tuning.mlr-org.com/reference/tnr.html>`_.
      `The corresponding chapter in the mlr3book <https://mlr3book.mlr-org.com/optimization.html#sec-model-tuning>`_ illustrates
      how the `Tuner <https://mlr3tuning.mlr-org.com/reference/Tuner.html>`_ class supports grid search, random search,
      generalized simulated annealing and non-linear optimization.
    * ``rsmp_tune`` is an object of class `mlr3 resampling <https://mlr3.mlr-org.com/reference/Resampling.html>`_
      that specifies the resampling method for evaluation, for example `rsmp("cv", folds = 5)` implements 5-fold cross-validation.
      `rsmp("holdout", ratio = 0.8)` implements an evaluation based on a hold-out sample that contains 20 percent of the observations.
      By default, 5-fold cross-validation is performed.
    * ``measure`` is a named list containing the measures used for tuning of the nuisance components.
      The names of the entries must match the learner names (see method ``learner_names()``).  The entries in the list must either be
      objects of class `Measure <https://mlr3.mlr-org.com/reference/Measure.html>`_ or keys passed to `msr() <https://mlr3.mlr-org.com/reference/mlr_sugar.html>`_.
      If ``measure`` is not provided by the user, default measures are used, i.e., mean squared error for regression models
      and classification error for binary outcomes.

In the following example, we tune the penalty parameter :math:`\lambda` (``lambda``) for lasso with the R package
`glmnet <https://glmnet.stanford.edu/>`_. To tune the value of ``lambda``, a grid search  is performed over a grid of values that range from 0.05
to 0.1 at a resolution of 10. Using a resolution of 10 splits the grid of values in 10 equally spaced values ranging from a minimum of 0.05
to a maximum of 0.1. To evaluate the predictive performance in both nuisance parts, the cross-validated mean squared error is used.

Setting the option ``tune_on_folds=FALSE``, the tuning is performed on the whole sample. Hence, the cross-validated errors
are obtained from a random split of the whole sample into 5 folds. As a result, one set of ``lambda`` values are obtained
which are later used in the fitting stage for all folds.

Alternatively, setting the option ``tune_on_folds=TRUE`` would assign the tuning resampling scheme ``rsmp_tune`` to each fold.
For example, if we set ``n_folds=2`` at initialization of the ``DoubleMLPLR`` object and use a 5-fold cross-validated error
for tuning, each of the two folds would be split up into 5 subfolds and the error would be evaluated on these subfolds.


.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(data.table)
        library(mlr3learners)
        library(mlr3tuning)
        library(paradox)
        lgr::get_logger("mlr3")$set_threshold("warn")
        lgr::get_logger("bbotk")$set_threshold("warn")

        set.seed(1234)
        ml_l = lrn("regr.glmnet")
        ml_m = lrn("regr.glmnet")
        dml_plr_obj = DoubleMLPLR$new(dml_data, ml_l, ml_m)

        par_grids = list("ml_l" = ParamSet$new(list(
                                          ParamDbl$new("lambda", lower = 0.05, upper = 0.1))),
                         "ml_m" =  ParamSet$new(list(
                                          ParamDbl$new("lambda", lower = 0.05, upper = 0.1))))

        tune_settings = list(terminator = trm("evals", n_evals = 100),
                              algorithm = tnr("grid_search", resolution = 10),
                              rsmp_tune = rsmp("cv", folds = 5),
                              measure = list("ml_l" = msr("regr.mse"),
                                             "ml_m" = msr("regr.mse")))
        dml_plr_obj$tune(param_set=par_grids, tune_settings=tune_settings, tune_on_fold=TRUE)
        dml_plr_obj$params

        dml_plr_obj$fit()
        dml_plr_obj$summary()


Hyperparameter tuning can also be done with more sophisticated methods, for example by using built-in tuning
paths of learners. For example, the learner `regr.cv_glmnet <https://mlr3learners.mlr-org.com/reference/mlr_learners_regr.cv_glmnet.html>`_
performs an internal cross-validated choice of the parameter ``lambda``.
Alternatively, the powerful functionalities of the `mlr3tuning <https://mlr3tuning.mlr-org.com/>`_ package can be used for
external parameter tuning of the nuisance parts. The optimally chosen parameters can then be passed to the
:ref:`DoubleML <doubleml_package>` models using the ``set_ml_nuisance_params()`` method.

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(data.table)
        library(mlr3learners)
        library(mlr3tuning)
        lgr::get_logger("mlr3")$set_threshold("warn")
        lgr::get_logger("bbotk")$set_threshold("warn")

        set.seed(1234)
        ml_l = lrn("regr.cv_glmnet", s="lambda.min")
        ml_m = lrn("regr.cv_glmnet", s="lambda.min")
        dml_plr_obj = DoubleMLPLR$new(dml_data, ml_l, ml_m)

        dml_plr_obj$fit()
        dml_plr_obj$summary()


The following code chunk illustrates another example for global parameter tuning with random forests
as provided by the  `ranger <https://github.com/imbs-hl/ranger>`_ package. In this example, we use random search to find optimal
parameters ``mtry`` and ``max.depth`` of a random forest. Evaluation is based on 3-fold cross-validation.

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)
        library(mlr3tuning)
        library(paradox)
        lgr::get_logger("mlr3")$set_threshold("warn")
        lgr::get_logger("bbotk")$set_threshold("warn")

        # set up a mlr3 learner
        learner = lrn("regr.ranger")
        ml_l = learner$clone()
        ml_m = learner$clone()

        set.seed(3141)
        obj_dml_data = make_plr_CCDDHNR2018(alpha=0.5)
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)

        # set up a list of parameter grids
        param_grid = list("ml_l" = ParamSet$new(list(
                                          ParamInt$new("mtry", lower = 2 , upper = 20),
                                          ParamInt$new("max.depth", lower = 2, upper = 5))),
                          "ml_m" = ParamSet$new(list(
                                          ParamInt$new("mtry", lower = 2 , upper = 20),
                                          ParamInt$new("max.depth", lower = 2, upper = 5))))
        tune_settings = list(terminator = mlr3tuning::trm("evals", n_evals = 20),
                              algorithm = tnr("random_search"),
                              rsmp_tune = rsmp("cv", folds = 3),
                              measure = list("ml_l" = msr("regr.mse"),
                                             "ml_m" = msr("regr.mse")))
        dml_plr_obj$tune(param_set=param_grid, tune_settings=tune_settings, tune_on_folds=FALSE)
        dml_plr_obj$params

        dml_plr_obj$fit()
        dml_plr_obj$summary()


Hyperparameter tuning with pipelines
####################################

As an alternative to the previously presented tuning approach, it is possible to base the parameter tuning on a pipeline
as provided by the `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_ package. The basic idea of this approach is to
define a learner via a pipeline and then perform the tuning via the ``tune()``. We will shortly repeat the lasso example
from above. In general, the pipeline-based approach can be used to find optimal values not only for the parameters of
one or multiple learners, but also for other parameters, which are, for example, involved in the data preprocessing. We
refer to more details provided in the `Pipelines Chapter in the mlr3book <https://mlr3book.mlr-org.com/pipelines.html>`_.

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3tuning)
        library(mlr3pipelines)
        lgr::get_logger("mlr3")$set_threshold("warn")
        lgr::get_logger("bbotk")$set_threshold("warn")

        # Define learner in a pipeline
        set.seed(1234)
        lasso_pipe = po("learner",
            learner = lrn("regr.glmnet"))
        ml_g = as_learner(lasso_pipe)
        ml_m = as_learner(lasso_pipe)

        # Instantiate a DoubleML object
        dml_plr_obj = DoubleMLPLR$new(dml_data, ml_g, ml_m)

        # Parameter grid for lambda
        par_grids = ps(regr.glmnet.lambda = p_dbl(lower = 0.05, upper = 0.1))

        tune_settings = list(terminator = trm("evals", n_evals = 100),
                             algorithm = tnr("grid_search", resolution = 10),
                             rsmp_tune = rsmp("cv", folds = 5),
                             measure = list("ml_g" = msr("regr.mse"),
                                            "ml_m" = msr("regr.mse")))
        dml_plr_obj$tune(param_set = list("ml_g" = par_grids,
                                          "ml_m" = par_grids),
                                          tune_settings=tune_settings,
                                          tune_on_fold=TRUE)
        dml_plr_obj$fit()
        dml_plr_obj$summary()



References
++++++++++

* Lang, M., Binder, M., Richter, J., Schratz, P., Pfisterer, F., Coors, S., Au, Q., Casalicchio, G., Kotthoff, L., Bischl, B. (2019), mlr3: A modern object-oriented machine learing framework in R. Journal of Open Source Software, `doi:10.21105/joss.01903 <https://doi.org/10.21105/joss.01903>`_.

* Becker, M., Binder, M., Bischl, B., Lang, M., Pfisterer, F., Reich, N.G., Richter, J., Schratz, P., Sonabend, R. (2020), mlr3 book, available at `https://mlr3book.mlr-org.com <https://mlr3book.mlr-org.com>`_.

