.. _sim_inf:

Confidence bands and multiplier bootstrap for valid simultaneous inference
---------------------------------------------------------------------------

:ref:`DoubleML <doubleml_package>` provides methods to perform valid simultaneous inference for multiple treatment variables.
As an example, consider a PLR with :math:`p_1` causal parameters of interest :math:`\theta_{0,1}, \ldots, \theta_{0,p_1}` associated with
treatment variables :math:`D_1, \ldots, D_{p_1}`

.. math::

    Y = D_1 \theta_{0,1} + \ldots + D_{p_1} \theta_{0, p_1}  + g_0(X) + \zeta, \quad \mathbb{E}(\zeta | D,X) = 0,

Inference on multiple target coefficients can be performed by iterating the DML inference procedure over the target variables of
interests. The relationship between the treatment variable :math:`D_j` and the remaining explanatory variables is determined by the equation

.. math::

    D_j = m_{0,j}(D_k, X) + V_j, \quad \mathbb{E}(V_j | X) = 0,

:math:`j \in \lbrace 1, \ldots, p_1 \rbrace` and :math:`k \in \lbrace 1, \ldots, p_1\rbrace \setminus j`.
All remaining treatment variables :math:`D_k` are comprised in the nuisance component :math:`m_{0,j}`.
The parameter of interest :math:`\theta_j` solves a corresponding moment condition

.. math::

    \mathbb{E}[ \psi_j(W; \theta_{0,j}, \eta_{0,j})] = 0.

For further details, we refer to Belloni et al. (2018).
Simultaneous inference can be based on a multiplier bootstrap procedure introduced in Belloni et al. (2014a, 2014b).
Alternatively, traditional correction approaches, for example the Bonferroni correction, can be used to adjust p-values.

Multiplier bootstrap and joint confidence intervals
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

The ``bootstrap()`` method provides an implementation of a multiplier bootstrap for double machine learning models.
For :math:`b=1, \ldots, B` weights :math:`\xi_{i, b}` are generated according to a normal (Gaussian) bootstrap, wild
bootstrap or exponential bootstrap.
The number of bootstrap samples is provided as input ``n_rep_boot`` and for ``method`` one can choose ``'Bayes'``,
``'normal'`` or ``'wild'``.
Based on the estimates of the standard errors that are obtained from DML, we construct bootstrap coefficients
:math:`\theta^{*,b}_j` and bootstrap t-statistics :math:`t^{*,b}_j`

.. math::

    \theta^{*,b}_{j} &= \frac{1}{\sqrt{N} \hat{J}_0}\sum_{k=1}^{K} \sum_{i \in I_k} \xi_{i}^b \cdot \psi_j(W_i; \tilde{\theta}_{0,j}, \hat{\eta}_{0,j;k}),

    t^{*,b}_{j} &= \frac{1}{\sqrt{N} \hat{J}_0 \hat{\sigma}} \sum_{k=1}^{K} \sum_{i \in I_k} \xi_{i}^b  \cdot \psi_j(W_i; \tilde{\theta}_{0,j}, \hat{\eta}_{0,j;k}).

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
which is based on the multiplier bootstrap, by default. Alternatively, ``p_adjust`` allows the user to apply traditional corrections
via the option ``method``.

.. tabbed:: Python

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
        ml_g = clone(learner)
        ml_m = clone(learner)
        dml_plr = dml.DoubleMLPLR(dml_data, ml_g, ml_m)

        print(dml_plr.fit().bootstrap().confint(joint=True))
        print(dml_plr.p_adjust())
        print(dml_plr.p_adjust(method='bonferroni'))

.. tabbed:: R

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
        ml_g = learner$clone()
        ml_m = learner$clone()
        dml_plr = DoubleMLPLR$new(dml_data, ml_g, ml_m)

        dml_plr$fit()
        dml_plr$bootstrap()
        dml_plr$confint(joint=TRUE)
        dml_plr$p_adjust()
        dml_plr$p_adjust(method="bonferroni")


References
++++++++++

* Belloni, A., Chernozhukov, V., Kato, K. (2014a), Gaussian approximation of suprema of empirical processes. The Annals of Statistics 42 (4): 1564-97, `doi: 10.1214/14-AOS1230 <https://dx.doi.org/10.1214/14-AOS1230>`_.

* Belloni, A., Chernozhukov, V., Kato, K. (2014b). Gaussian approximations and multiplier bootstrap for maxima of sums of high-dimensional random vectors. The Annals of Statistics 41 (6): 2786-2819, `doi: 10.1214/13-AOS1161 <https://dx.doi.org/10.1214/13-AOS1161>`_.

* Belloni, A., Chernozhukov, V., Chetverikov, D., Wei, Y. (2018), Uniformly valid post-regularization confidence regions for many functional parameters in z-estimation framework. Annals of Statistics, 46 (6B): 3643-75,  `doi: 10.1214/17-AOS1671 <https://dx.doi.org/10.1214%2F17-AOS1671>`_.