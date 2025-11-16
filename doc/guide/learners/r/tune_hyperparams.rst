Parameter tuning of learners for the nuisance functions of :ref:`DoubleML <doubleml_package>` models can be done via the ``tune()`` method.
The ``tune()`` method passes various options and parameters to the tuning interface provided by the
`mlr3tuning <https://mlr3tuning.mlr-org.com/>`_ package. The `mlr3 book <https://mlr3book.mlr-org.com/>`_ provides a
`step-by-step introduction to parameter tuning <https://mlr3book.mlr-org.com/chapters/chapter4/hyperparameter_optimization.html>`_.

To illustrate the parameter tuning, we generate data from a sparse partially linear regression model.

.. tab-set::

  .. tab-item:: R
    :sync: r

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
  `The corresponding chapter in the mlr3book <https://mlr3book.mlr-org.com/chapters/chapter4/hyperparameter_optimization.html#sec-tuner>`_ illustrates
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


.. tab-set::

  .. tab-item:: R
    :sync: r

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

        par_grids = list(
          "ml_l" = ps(lambda = p_dbl(lower = 0.05, upper = 0.1)),
          "ml_m" = ps(lambda = p_dbl(lower = 0.05, upper = 0.1)))

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

.. tab-set::

  .. tab-item:: R
    :sync: r

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

.. tab-set::

  .. tab-item:: R
    :sync: r

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
        param_grid = list("ml_l" = ps(mtry = p_int(lower = 2 , upper = 20),
                                      max.depth = p_int(lower = 2, upper = 5)),
                          "ml_m" = ps(mtry = p_int(lower = 2 , upper = 20),
                                      max.depth = p_int(lower = 2, upper = 5)))

        tune_settings = list(terminator = mlr3tuning::trm("evals", n_evals = 20),
                              algorithm = tnr("random_search"),
                              rsmp_tune = rsmp("cv", folds = 3),
                              measure = list("ml_l" = msr("regr.mse"),
                                             "ml_m" = msr("regr.mse")))
        dml_plr_obj$tune(param_set=param_grid, tune_settings=tune_settings, tune_on_folds=FALSE)
        dml_plr_obj$params

        dml_plr_obj$fit()
        dml_plr_obj$summary()