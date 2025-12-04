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

.. tab-set::

  .. tab-item:: R
    :sync: r

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

.. tab-set::

  .. tab-item:: R
    :sync: r

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

.. tab-set::

  .. tab-item:: R
    :sync: r

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

.. tab-set::

  .. tab-item:: R
    :sync: r

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
