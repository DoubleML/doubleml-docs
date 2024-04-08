.. _se_confint:

Variance estimation and confidence intervals 
--------------------------------------------

Variance estimation
+++++++++++++++++++

Under regularity conditions the estimator :math:`\tilde{\theta}_0` concentrates in a :math:`1/\sqrt{N}`-neighborhood
of :math:`\theta_0` and the sampling error :math:`\sqrt{N}(\tilde{\theta}_0 - \theta_0)` is approximately normal

.. math::

    \sqrt{N}(\tilde{\theta}_0 - \theta_0) \leadsto N(o, \sigma^2),

with mean zero and variance given by

.. math::

    \sigma^2 := J_0^{-2} \mathbb{E}(\psi^2(W; \theta_0, \eta_0)),

where :math:`J_0 = \mathbb{E}(\psi_a(W; \eta_0))`, if the score function is linear in the parameter :math:`\theta`.
If the score is not linear in the parameter :math:`\theta`, then
:math:`J_0 = \partial_\theta\mathbb{E}(\psi(W; \theta, \eta_0)) \big|_{\theta=\theta_0}`.

Estimates of the variance are obtained by

.. math::

    \hat{\sigma}^2 &= \hat{J}_0^{-2} \frac{1}{N} \sum_{k=1}^{K} \sum_{i \in I_k} \big[\psi(W_i; \tilde{\theta}_0, \hat{\eta}_{0,k})\big]^2,

    \hat{J}_0 &= \frac{1}{N} \sum_{k=1}^{K} \sum_{i \in I_k} \psi_a(W_i; \hat{\eta}_{0,k}),

for score functions being linear in the parameter :math:`\theta`.
For non-linear score functions, the implementation assumes that derivatives and expectations are interchangeable, so
that

.. math::

    \hat{J}_0 = \frac{1}{N} \sum_{k=1}^{K} \sum_{i \in I_k} \partial_\theta \psi(W_i; \tilde{\theta}_0, \hat{\eta}_{0,k}).

An approximate confidence interval is given by

.. math::

    \big[\tilde{\theta}_0 \pm \Phi^{-1}(1 - \alpha/2) \hat{\sigma} / \sqrt{N}].

As an example we consider a partially linear regression model (PLR)
implemented in ``DoubleMLPLR``.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            from doubleml.datasets import make_plr_CCDDHNR2018
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.base import clone

            np.random.seed(3141)
            learner = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_l = clone(learner)
            ml_m = clone(learner)
            data = make_plr_CCDDHNR2018(alpha=0.5, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m)
            dml_plr_obj.fit();

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            library(DoubleML)
            library(mlr3)
            library(mlr3learners)
            library(data.table)
            lgr::get_logger("mlr3")$set_threshold("warn")

            learner = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
            ml_l = learner$clone()
            ml_m = learner$clone()

            set.seed(3141)
            obj_dml_data = make_plr_CCDDHNR2018(alpha=0.5)
            dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)
            dml_plr_obj$fit()


The ``fit()`` method of ``DoubleMLPLR``
stores the estimate :math:`\tilde{\theta}_0` in its ``coef`` attribute.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj.coef)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            print(dml_plr_obj$coef)

The asymptotic standard error :math:`\hat{\sigma}/\sqrt{N}` is stored in its ``se`` attribute.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj.se)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            print(dml_plr_obj$se)

Additionally, the value of the :math:`t`-statistic and the corresponding p-value are provided in the attributes
``t_stat`` and ``pval``.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj.t_stat)
            print(dml_plr_obj.pval)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            print(dml_plr_obj$t_stat)
            print(dml_plr_obj$pval)


.. note::
    - In Python, an overview of all these estimates, together with a 95 % confidence interval is stored in the
      attribute ``summary``.
    - In R, a summary can be obtained by using the method ``summary()``. The ``confint()`` method performs estimation of
      confidence intervals.


.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj.summary)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj$summary()
            dml_plr_obj$confint()

A more detailed overview of the fitted model, its specifications and the summary can be obtained via the
string-representation of the object.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            print(dml_plr_obj)

.. _sim_inf:

Confidence bands and multiplier bootstrap for valid simultaneous inference
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:ref:`DoubleML <doubleml_package>` provides methods to perform valid simultaneous inference for multiple treatment variables.
As an example, consider a PLR with :math:`p_1` causal parameters of interest :math:`\theta_{0,1}, \ldots, \theta_{0,p_1}` associated with
treatment variables :math:`D_1, \ldots, D_{p_1}`. Inference on multiple target coefficients can be performed by iteratively applying the DML inference procedure over the target variables of
interests: Each of the coefficients of interest, :math:`\theta_{0,j}`, with :math:`j \in \lbrace 1, \ldots, p_1 \rbrace`, solves a corresponding moment condition

.. math::

    \mathbb{E}[ \psi_j(W; \theta_{0,j}, \eta_{0,j})] = 0.

Analogously to the case with a single parameter of interest, the PLR model with multiple treatment variables includes two regression steps to achieve orthogonality.
First, the main regression is given by

.. math::

    Y = D_j \theta_{0,j} + g_{0,j}([D_k, X]) + \zeta_j, \quad \mathbb{E}(\zeta_j | D, X) = 0,

with :math:`[D_k, X]` being a matrix comprising the confounders, :math:`X`, and all remaining treatment variables
:math:`D_k` with  :math:`k \in \lbrace 1, \ldots, p_1\rbrace \setminus j`, by default.
Second, the relationship between the treatment variable :math:`D_j` and the remaining explanatory variables is determined by the equation

.. math::

    D_j = m_{0,j}([D_k, X]) + V_j, \quad \mathbb{E}(V_j | D_k, X) = 0,

For further details, we refer to Belloni et al. (2018). Simultaneous inference can be based on a multiplier bootstrap procedure introduced in Chernozhukov et al. (2013, 2014).
Alternatively, traditional correction approaches, for example the Bonferroni correction, can be used to adjust p-values.

The ``bootstrap()`` method provides an implementation of a multiplier bootstrap for double machine learning models.
For :math:`b=1, \ldots, B` weights :math:`\xi_{i, b}` are generated according to a normal (Gaussian) bootstrap, wild
bootstrap or exponential bootstrap.
The number of bootstrap samples is provided as input ``n_rep_boot`` and for ``method`` one can choose ``'Bayes'``,
``'normal'`` or ``'wild'``.
Based on the estimates of the standard errors :math:`\hat{\sigma}_j`
and :math:`\hat{J}_{0,j} = \mathbb{E}_N(\psi_{a,j}(W; \eta_{0,j}))`
that are obtained from DML, we construct bootstraped t-statistics :math:`t^{*,b}_j`
for :math:`j=1, \ldots, p_1`

.. math::

    t^{*,b}_{j} = \frac{1}{\sqrt{N} \hat{J}_{0,j} \hat{\sigma}_{j}} \sum_{k=1}^{K} \sum_{i \in I_k} \xi_{i}^b  \cdot \psi_j(W_i; \tilde{\theta}_{0,j}, \hat{\eta}_{0,j;k}).

The output of the multiplier bootstrap can be used to determine the constant, :math:`c_{1-\alpha}` that is required for the construction of a
simultaneous :math:`(1-\alpha)` confidence band

.. math::

    \left[\tilde\theta_{0,j} \pm c_{1-\alpha} \cdot \hat\sigma_j/\sqrt{N} \right].

To demonstrate the bootstrap, we simulate data from a sparse partially linear regression model.
Then we estimate the PLR model and perform the multiplier bootstrap.
Joint confidence intervals based on the multiplier bootstrap are then obtained by setting the option ``joint``
when calling the method ``confint``.

Moreover, a multiple hypotheses testing adjustment of p-values from a high-dimensional model can be obtained with
the method ``p_adjust``. :ref:`DoubleML <doubleml_package>`  performs a version of the Romano-Wolf stepdown adjustment,
which is based on the multiplier bootstrap, by default. Alternatively, ``p_adjust`` allows users to apply traditional corrections
via the option ``method``.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            import numpy as np
            from sklearn.base import clone
            from sklearn.linear_model import LassoCV

            # Simulate data
            np.random.seed(1234)
            n_obs = 500
            n_vars = 100
            X = np.random.normal(size=(n_obs, n_vars))
            theta = np.array([3., 3., 3.])
            y = np.dot(X[:, :3], theta) + np.random.standard_normal(size=(n_obs,))

            dml_data = dml.DoubleMLData.from_arrays(X[:, 10:], y, X[:, :10])

            learner = LassoCV()
            ml_l = clone(learner)
            ml_m = clone(learner)
            dml_plr = dml.DoubleMLPLR(dml_data, ml_l, ml_m)

            print(dml_plr.fit().bootstrap().confint(joint=True))
            print(dml_plr.p_adjust())
            print(dml_plr.p_adjust(method='bonferroni'))

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            library(DoubleML)
            library(mlr3)
            library(mlr3learners)
            library(data.table)
            lgr::get_logger("mlr3")$set_threshold("warn")

            set.seed(3141)
            n_obs = 500
            n_vars = 100
            theta = rep(3, 3)
            X = matrix(stats::rnorm(n_obs * n_vars), nrow = n_obs, ncol = n_vars)
            y = X[, 1:3, drop = FALSE] %*% theta  + stats::rnorm(n_obs)
            dml_data = double_ml_data_from_matrix(X = X[, 11:n_vars], y = y, d = X[,1:10])

            learner = lrn("regr.cv_glmnet", s="lambda.min")
            ml_l = learner$clone()
            ml_m = learner$clone()
            dml_plr = DoubleMLPLR$new(dml_data, ml_l, ml_m)

            dml_plr$fit()
            dml_plr$bootstrap()
            dml_plr$confint(joint=TRUE)
            dml_plr$p_adjust()
            dml_plr$p_adjust(method="bonferroni")


Simultaneous inference over different DoubleML models (advanced)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The :ref:`DoubleML <doubleml_package>` package provides a method to perform valid simultaneous inference over different DoubleML models.

.. note::
    Remark that the confidence intervals will generally only be valid if the stronger (uniform) assumptions on e.g. nuisance
    estimates are satisfied. Further, the models should be estimated on the same data set.

The :py:class:`doubleml.DoubleML` class contains a ``framework`` attribute which stores a :py:class:`doubleml.DoubleMLFramework` object. This
object contains a scaled version of the score function

.. math::

    \tilde{psi}(W_i; \theta, \eta) = \hat{J}_{0}^{-1}\psi(W_i; \hat{\theta}_{0}, \hat{\eta}_{0})

which is used to construct confidence intervals. The framework objects can be concatenated using the
:py:function:`doubleml.DoubleML.concat` function.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            import numpy as np
            from sklearn.base import clone
            from sklearn.linear_model import LassoCV
            from sklearn.ensemble import RandomForestRegressor

            import doubleml as dml

            # Simulate data
            np.random.seed(1234)
            n_obs = 500
            n_vars = 100
            X = np.random.normal(size=(n_obs, n_vars))
            theta = np.array([3., 3., 3.])
            y = np.dot(X[:, :3], theta) + np.random.standard_normal(size=(n_obs,))

            dml_data = dml.DoubleMLData.from_arrays(X[:, 10:], y, X[:, :10])

            learner = LassoCV()
            dml_plr_1 = dml.DoubleMLPLR(dml_data, clone(learner), clone(learner))

            learner_rf = RandomForestRegressor()
            dml_plr_2 = dml.DoubleMLPLR(dml_data, clone(learner_rf), clone(learner_rf))

            dml_plr_1.fit()
            dml_plr_2.fit()

            dml_combined = dml.concat([dml_plr_1.framework, dml_plr_2.framework])
            dml_combined.bootstrap().confint(joint=True)

Frameworks can also be added or subtracted from each other. Of course, this changes the estimated parameter and should be used with caution. 


.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            import numpy as np
            from sklearn.base import clone
            from sklearn.linear_model import LassoCV
            from sklearn.ensemble import RandomForestRegressor

            import doubleml as dml

            # Simulate data
            np.random.seed(1234)
            n_obs = 500
            n_vars = 100
            X = np.random.normal(size=(n_obs, n_vars))
            theta = np.array([3., 3., 3.])
            y = np.dot(X[:, :3], theta) + np.random.standard_normal(size=(n_obs,))

            dml_data = dml.DoubleMLData.from_arrays(X[:, 10:], y, X[:, :10])

            learner = LassoCV()
            dml_plr_1 = dml.DoubleMLPLR(dml_data, clone(learner), clone(learner))

            learner_rf = RandomForestRegressor()
            dml_plr_2 = dml.DoubleMLPLR(dml_data, clone(learner_rf), clone(learner_rf))

            dml_plr_1.fit()
            dml_plr_2.fit()

            dml_combined = dml_plr_1.framework - dml_plr_2.framework
            dml_combined.bootstrap().confint(joint=True)

One possible use case is to substract the estimates from two average potential outcome models as e.g. in the :class:`DoubleMLQTE` example.

This also works for multiple repetitions if both models have the same number of repetitions, as each repetition is treated seperately.


References
++++++++++

* Belloni, A., Chernozhukov, V., Chetverikov, D., Wei, Y. (2018), Uniformly valid post-regularization confidence regions for many functional parameters in z-estimation framework. The Annals of Statistics, 46 (6B): 3643-75,  `doi: 10.1214/17-AOS1671 <https://dx.doi.org/10.1214%2F17-AOS1671>`_.

* Chernozhukov, V., Chetverikov, D., Kato, K. (2013). Gaussian approximations and multiplier bootstrap for maxima of sums of high-dimensional random vectors. The Annals of Statistics 41 (6): 2786-2819, `doi: 10.1214/13-AOS1161 <https://dx.doi.org/10.1214/13-AOS1161>`_.

* Chernozhukov, V., Chetverikov, D., Kato, K. (2014), Gaussian approximation of suprema of empirical processes. The Annals of Statistics 42 (4): 1564-97, `doi: 10.1214/14-AOS1230 <https://dx.doi.org/10.1214/14-AOS1230>`_.
