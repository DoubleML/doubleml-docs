.. _se_confint:

Variance estimation and confidence intervals for a causal parameter of interest
-------------------------------------------------------------------------------

Variance estimation
+++++++++++++++++++

Under regularity conditions the estimator :math:`\tilde{\theta}_0` concentrates in a :math:`1/\sqrt(N)`-neighborhood
of :math:`\theta_0` and the sampling error :math:`\sqrt(N)(\tilde{\theta}_0 - \theta_0)` is approximately normal

.. math::

    \sqrt(N)(\tilde{\theta}_0 - \theta_0) \leadsto N(o, \sigma^2),

with mean zero and variance given by

.. math::

    \sigma^2 := J_0^{-2} \mathbb{E}(\psi^2(W; \theta_0, \eta_0)),

    J_0 = \mathbb{E}(\psi_a(W; \eta_0)).

Estimates of the variance are obtained by

.. math::

    \hat{\sigma}^2 &= \hat{J}_0^{-2} \frac{1}{N} \sum_{k=1}^{K} \sum_{i \in I_k} \big[\psi(W_i; \tilde{\theta}_0, \hat{\eta}_{0,k})\big]^2,

    \hat{J}_0 &= \frac{1}{N} \sum_{k=1}^{K} \sum_{i \in I_k} \psi_a(W_i; \hat{\eta}_{0,k}).

An approximate confidence interval is given by

.. math::

    \big[\tilde{\theta}_0 \pm \Phi^{-1}(1 - \alpha/2) \hat{\sigma} / \sqrt{N}].

As an example we consider a partially linear regression model (PLR)
implemented in ``DoubleMLPLR``.

.. tabbed:: Python

    .. ipython:: python

        import doubleml as dml
        from doubleml.datasets import make_plr_CCDDHNR2018
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.base import clone

        np.random.seed(3141)
        learner = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_g = clone(learner)
        ml_m = clone(learner)
        data = make_plr_CCDDHNR2018(alpha=0.5, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_g, ml_m)
        dml_plr_obj.fit();

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)
        lgr::get_logger("mlr3")$set_threshold("warn")

        learner = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        ml_g = learner$clone()
        ml_m = learner$clone()

        set.seed(3141)
        obj_dml_data = make_plr_CCDDHNR2018(alpha=0.5)
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_g, ml_m)
        dml_plr_obj$fit()


The ``fit()`` method of ``DoubleMLPLR``
stores the estimate :math:`\tilde{\theta}_0` in its ``coef`` attribute.

.. tabbed:: Python

    .. ipython:: python

        print(dml_plr_obj.coef)

.. tabbed:: R

    .. jupyter-execute::

        print(dml_plr_obj$coef)

The asymptotic standard error :math:`\hat{\sigma}/\sqrt{N}` is stored in its ``se`` attribute.

.. tabbed:: Python

    .. ipython:: python

        print(dml_plr_obj.se)

.. tabbed:: R

    .. jupyter-execute::

        print(dml_plr_obj$se)

Additionally, the value of the :math:`t`-statistic and the corresponding p-value are provided in the attributes
``t_stat`` and ``pval``.

.. tabbed:: Python

    .. ipython:: python

        print(dml_plr_obj.t_stat)
        print(dml_plr_obj.pval)

.. tabbed:: R

    .. jupyter-execute::

        print(dml_plr_obj$t_stat)
        print(dml_plr_obj$pval)


.. note::
    - In Python, an overview of all these estimates, together with a 95 % confidence interval is stored in the
      attribute ``summary``.
    - In R, a summary can be obtained by using the method ``summary()``. The ``confint()`` method performs estimation of
      confidence intervals.


.. tabbed:: Python

    .. ipython:: python

        print(dml_plr_obj.summary)

.. tabbed:: R

    .. jupyter-execute::

        dml_plr_obj$summary()
        dml_plr_obj$confint()

A more detailed overview of the fitted model, its specifications and the summary can be obtained via the
string-representation of the object.

.. tabbed:: Python

    .. ipython:: python

        print(dml_plr_obj)

.. tabbed:: R

    .. jupyter-execute::

        print(dml_plr_obj)

