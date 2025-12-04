Users can also specify learners that have been constructed from a pipeline using the `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_
package. In general, pipelines can be used to perform data preprocessing, feature selection, combine learners and even
to perform hyperparameter tuning. In the following, we provide two examples on how to construct a single learner and how
to stack different learners via a pipeline. For a more detailed introduction to `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_,
we refer to the `Pipelines Chapter in the mlr3book <https://mlr3book.mlr-org.com/chapters/chapter7/sequential_pipelines.html>`_. Moreover, a
notebook on how to use `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_ in combination with :ref:`DoubleML <doubleml_package>`
is available in the example gallery.

.. tab-set::

  .. tab-item:: R
    :sync: r

    .. jupyter-execute::
      
      library(DoubleML)
      library(mlr3)
      library(mlr3learners)
      library(mlr3pipelines)
      library(data.table)

      set.seed(3141)
      # Define random forest learner in a pipeline
      single_learner_pipeline = po("learner", lrn("regr.ranger", num.trees = 10))

      # Use pipeline to create a new instance of a learner
      ml_g = as_learner(single_learner_pipeline)
      ml_m = as_learner(single_learner_pipeline)

      data = make_plr_CCDDHNR2018(alpha=0.5, return_type='data.table')
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
