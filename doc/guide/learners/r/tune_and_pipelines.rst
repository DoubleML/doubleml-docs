As an alternative to the previously presented tuning approach, it is possible to base the parameter tuning on a pipeline
as provided by the `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_ package. The basic idea of this approach is to
define a learner via a pipeline and then perform the tuning via the ``tune()``. We will shortly repeat the lasso example
from above. In general, the pipeline-based approach can be used to find optimal values not only for the parameters of
one or multiple learners, but also for other parameters, which are, for example, involved in the data preprocessing. We
refer to more details provided in the `Pipelines Chapter in the mlr3book <https://mlr3book.mlr-org.com/chapters/chapter7/sequential_pipelines.html>`_.

.. tab-set::

  .. tab-item:: R
    :sync: r

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3tuning)
        library(mlr3pipelines)
        lgr::get_logger("mlr3")$set_threshold("warn")
        lgr::get_logger("bbotk")$set_threshold("warn")

        set.seed(3141)
        n_obs = 200
        n_vars = 200
        theta = 3
        X = matrix(stats::rnorm(n_obs * n_vars), nrow = n_obs, ncol = n_vars)
        d = X[, 1:3, drop = FALSE] %*% c(5, 5, 5) + stats::rnorm(n_obs)
        y = theta * d + X[, 1:3, drop = FALSE] %*% c(5, 5, 5)  + stats::rnorm(n_obs)
        dml_data = double_ml_data_from_matrix(X = X, y = y, d = d)

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
