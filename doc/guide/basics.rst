.. _basics:

The basics of double/debiased machine learning
----------------------------------------------

In the following we provide a brief summary of and motivation to the double machine learning (DML) framework and show how the
corresponding methods provided by the :ref:`DoubleML <doubleml_package>` package can be applied.
For details we refer to Chernozhukov et al. (2018).


.. Add references to the vignette here when it is ready.

.. note::
    Detailed notebooks containing the complete code for the examples can be found in the :ref:`Example Gallery <examplegallery>`.

Data generating process
+++++++++++++++++++++++

We consider the following partially linear model

.. math::

        y_i = \theta_0 d_i + g_0(x_i) + \zeta_i, & &\zeta_i \sim \mathcal{N}(0,1),

        d_i = m_0(x_i) + v_i, & &v_i \sim \mathcal{N}(0,1),


with covariates :math:`x_i \sim \mathcal{N}(0, \Sigma)`, where  :math:`\Sigma` is a matrix with entries
:math:`\Sigma_{kj} = 0.7^{|j-k|}`. We are interested in performing valid inference on the causal parameter
:math:`\theta_0`. The true parameter :math:`\theta_0` is set to :math:`0.5` in our simulation experiment.

The nuisance functions are given by

.. math::

    m_0(x_i) &= x_{i,1} + \frac{1}{4}  \frac{\exp(x_{i,3})}{1+\exp(x_{i,3})},

    g_0(x_i) &= \frac{\exp(x_{i,1})}{1+\exp(x_{i,1})} + \frac{1}{4} x_{i,3}.


.. note::
    - In Python the data can be generated with :py:func:`doubleml.datasets.make_plr_CCDDHNR2018`.
    - In R the data can be generated with `DoubleML::make_plr_CCDDHNR2018() <https://docs.doubleml.org/r/stable/reference/make_plr_CCDDHNR2018.html>`_.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. code-block:: python

            import numpy as np
            from doubleml.datasets import make_plr_CCDDHNR2018

            np.random.seed(1234)
            n_rep = 1000
            n_obs = 500
            n_vars = 20
            alpha = 0.5

            data = list()

            for i_rep in range(n_rep):
                (x, y, d) = make_plr_CCDDHNR2018(alpha=alpha, n_obs=n_obs, dim_x=n_vars, return_type='array')
                data.append((x, y, d))

    .. tab-item:: R
        :sync: r

        .. code-block:: r

            library(DoubleML)
            set.seed(1234)
            n_rep = 1000
            n_obs = 500
            n_vars = 20
            alpha = 0.5

            data = list()
            for (i_rep in seq_len(n_rep)) {
                data[[i_rep]] = make_plr_CCDDHNR2018(alpha=alpha, n_obs=n_obs, dim_x=n_vars,
                                                    return_type="data.frame")
            }

Regularization bias in simple ML-approaches
+++++++++++++++++++++++++++++++++++++++++++

Naive inference that is based on a direct application of machine learning methods to estimate the causal
parameter, :math:`\theta_0`, is generally invalid. The use of machine learning methods introduces a bias that arises due to
regularization. A simple ML approach is given by randomly splitting the sample into two parts.
On the auxiliary sample indexed by :math:`i \in I^C` the nuisance function :math:`g_0(X)` is estimated with an ML method,
for example a random forest learner.
Given the estimate :math:`\hat{g}_0(X)`, the final estimate of :math:`\theta_0` is obtained as (:math:`n=N/2`) using the
other half of observations indexed with :math:`i \in I`

.. math::

    \hat{\theta}_0 = \left(\frac{1}{n} \sum_{i\in I} D_i^2\right)^{-1} \frac{1}{n} \sum_{i\in I} D_i (Y_i - \hat{g}_0(X_i)).

The following figure shows the distribution of the resulting estimates :math:`\hat{\theta}_0` for the simple ML approach (the corresponding notebooks are
available in the :ref:`Example Gallery <examplegallery>`).

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_non_orthogonal.svg
            :width: 800
            :alt: Distribution with non-orthogonal score
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_non_orthogonal.svg
            :width: 800
            :alt: Distribution with non-orthogonal score
            :align: center


The regularization bias in the simple ML-approach is caused by the slow convergence of :math:`\hat{\theta}_0`

.. math::

    |\sqrt{n} (\hat{\theta}_0 - \theta_0) | \rightarrow_{P} \infty

i.e., slower than :math:`1/\sqrt{n}`.
The driving factor is the bias that arises by learning :math:`g` with a random forest or any other ML technique.
A heuristic illustration is given by

.. math::

    \sqrt{n}(\hat{\theta}_0 - \theta_0) = \underbrace{\left(\frac{1}{n} \sum_{i\in I} D_i^2\right)^{-1} \frac{1}{n} \sum_{i\in I} D_i \zeta_i}_{=:a}
    +  \underbrace{\left(\frac{1}{n} \sum_{i\in I} D_i^2\right)^{-1} \frac{1}{n} \sum_{i\in I} D_i (g_0(X_i) - \hat{g}_0(X_i))}_{=:b}.

:math:`a` is approximately Gaussian under mild conditions.
However, :math:`b` (the regularization bias) diverges in general.

.. _bias_non_orth:

Overcoming regularization bias by orthogonalization
+++++++++++++++++++++++++++++++++++++++++++++++++++

To overcome the regularization bias we can partial out the effect of :math:`X` from :math:`D` to obtain the
orthogonalized regressor :math:`V = D - m(X)`. We then use the final estimate

.. math::

    \check{\theta}_0 = \left(\frac{1}{n} \sum_{i\in I} \hat{V}_i D_i\right)^{-1} \frac{1}{n} \sum_{i\in I} \hat{V}_i (Y_i - \hat{g}_0(X_i)).

The following figure shows the distribution of the resulting estimates :math:`\hat{\theta}_0` without sample-splitting (the corresponding notebooks are
available in the :ref:`Example Gallery <examplegallery>`).

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_dml_nosplit.svg
            :width: 800
            :alt: Distribution without sample-splitting
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_dml_nosplit.svg
            :width: 800
            :alt: Distribution without sample-splitting
            :align: center

If the nuisance models :math:`\hat{g}_0()` and :math:`\hat{m}()` are estimated on the whole dataset, which is also used for obtaining
the final estimate :math:`\check{\theta}_0`, another bias is observed.

.. _bias_overfitting:

Sample splitting to remove bias induced by overfitting
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Using sample splitting, i.e., estimate the nuisance models :math:`\hat{g}_0()` and :math:`\hat{m}()` on one part of the
data (training data) and estimate :math:`\check{\theta}_0` on the other part of the data (test data), overcomes the bias
induced by overfitting. We can exploit the benefits of cross-fitting by switching the role of the training and test sample.
Cross-fitting performs well empirically because the entire sample can be used for estimation.

The following figure shows the distribution of the resulting estimates :math:`\hat{\theta}_0` with orthogonal score and sample-splitting 
(the corresponding notebooks are available in the :ref:`Example Gallery <examplegallery>`).

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_dml.svg
            :width: 800
            :alt: Distribution with orthogonal scores and sample-splitting
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_dml.svg
            :width: 800
            :alt: Distribution with orthogonal scores and sample-splitting
            :align: center

Double/debiased machine learning
++++++++++++++++++++++++++++++++

To illustrate the benefits of the auxiliary prediction step in the DML framework we write the error as

.. math::

    \sqrt{n}(\check{\theta}_0 - \theta_0) = a^* + b^* + c^*

Chernozhukov et al. (2018) argues that:

The first term

.. math::

    a^* := (EV^2)^{-1} \frac{1}{\sqrt{n}} \sum_{i\in I} V_i \zeta_i

will be asymptotically normally distributed.

The second term

.. math::

    b^* := (EV^2)^{-1} \frac{1}{\sqrt{n}} \sum_{i\in I} (\hat{m}(X_i) - m(X_i)) (\hat{g}_0(X_i) - g_0(X_i))

vanishes asymptotically for many data generating processes.

The third term :math:`c^*` vanishes in probability if sample splitting is applied. Finally, let us compare all distributions.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_all.svg
            :width: 800
            :alt: All distributions
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_all.svg
            :width: 800
            :alt: All distributions
            :align: center

The DoubleML implementation implements a several orthogonal scores and directly applies cross-fitting.
The complete code is available in the :ref:`Example Gallery <examplegallery>`.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. code-block:: python

            theta_dml = np.full(n_rep, np.nan)
            se_dml = np.full(n_rep, np.nan)

            for i_rep in range(n_rep):
                (x, y, d) = data[i_rep]
                obj_dml_data = DoubleMLData.from_arrays(x, y, d)
                obj_dml_plr = DoubleMLPLR(
                    obj_dml_data,
                    ml_l=LGBMRegressor(n_estimators=300, learning_rate=0.1),
                    ml_m=LGBMRegressor(n_estimators=200, learning_rate=0.1),
                    ml_g=LGBMRegressor(n_estimators=300, learning_rate=0.1),
                    n_folds=2,
                    score='IV-type')
                obj_dml_plr.fit()
                theta_dml[i_rep] = obj_dml_plr.coef[0]
                se_dml[i_rep] = obj_dml_plr.se[0]

    .. tab-item:: R
        :sync: r

        .. code-block:: r

            theta_dml = rep(NA, n_rep)
            se_dml = rep(NA, n_rep)

            for (i_rep in seq_len(n_rep)) {
                df = data[[i_rep]]
                obj_dml_data = double_ml_data_from_data_frame(df, y_col = "y", d_cols = "d")
                obj_dml_plr = DoubleMLPLR$new(
                    obj_dml_data,
                    ml_l,
                    ml_m,
                    ml_g,
                    n_folds=2,
                    score='IV-type')
                obj_dml_plr$fit()
                theta_dml[i_rep] = obj_dml_plr$coef
                se_dml[i_rep] = obj_dml_plr$se
            }


Partialling out score
+++++++++++++++++++++
Another debiased estimator, based on the partialling-out approach of Robinson(1988), is

.. math::

    \check{\theta}_0 = \left(\frac{1}{n} \sum_{i\in I} \hat{V}_i \hat{V}_i \right)^{-1} \frac{1}{n} \sum_{i\in I} \hat{V}_i (Y_i - \hat{\ell}_0(X_i)),

with :math:`\ell_0(X_i) = E(Y|X)`.
All nuisance parameters for the estimator with ``score='partialling out'`` are conditional mean functions, which can be
directly estimated using ML methods. This is a minor advantage over the estimator with ``score='IV-type'``.
In the following, we repeat the above analysis with ``score='partialling out'``. In a first part of the analysis, we
estimate :math:`\theta_0` without sample splitting. Again we observe a bias from overfitting.

The following figure shows the distribution of the resulting estimates :math:`\hat{\theta}_0` without sample-splitting 
(the corresponding notebooks are available in the :ref:`Example Gallery <examplegallery>`).

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_dml_po_nosplit.svg
            :width: 800
            :alt: Distribution without sample splitting
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_dml_po_nosplit.svg
            :width: 800
            :alt: Distribution without sample splitting
            :align: center

Using sample splitting, overcomes the bias induced by overfitting.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_dml_po.svg
            :width: 800
            :alt: Distribution with orthogonal score and sample-splitting
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_dml_po.svg
            :width: 800
            :alt: Distribution with orthogonal score and sample-splitting
            :align: center

Again, the implementation automatically applies cross-fitting. The complete code is available in the :ref:`Example Gallery <examplegallery>`.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. code-block:: python

            theta_dml_po = np.full(n_rep, np.nan)
            se_dml_po = np.full(n_rep, np.nan)

            for i_rep in range(n_rep):
                (x, y, d) = data[i_rep]
                obj_dml_data = DoubleMLData.from_arrays(x, y, d)
                obj_dml_plr = DoubleMLPLR(
                    obj_dml_data,
                    ml_l=LGBMRegressor(n_estimators=300, learning_rate=0.1),
                    ml_m=LGBMRegressor(n_estimators=200, learning_rate=0.1),
                    n_folds=2,
                    score='partialling out')
                obj_dml_plr.fit()
                theta_dml_po[i_rep] = obj_dml_plr.coef[0]
                se_dml_po[i_rep] = obj_dml_plr.se[0]

    .. tab-item:: R
        :sync: r

        .. code-block:: r

            theta_dml_po = rep(NA, n_rep)
            se_dml_po = rep(NA, n_rep)

            for (i_rep in seq_len(n_rep)) {
                df = data[[i_rep]]
                obj_dml_data = double_ml_data_from_data_frame(df, y_col = "y", d_cols = "d")
                obj_dml_plr = DoubleMLPLR$new(
                    obj_dml_data,
                    ml_l,
                    ml_m,
                    n_folds=2,
                    score='partialling out')
                obj_dml_plr$fit()
                theta_dml_po[i_rep] = obj_dml_plr$coef
                se_dml_po[i_rep] = obj_dml_plr$se
            }


Finally, let us compare all distributions.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. image:: figures/py_po_all.svg
            :width: 800
            :alt: All distributions with partialling-out score
            :align: center

    .. tab-item:: R
        :sync: r

        .. image:: figures/r_po_all.svg
            :width: 800
            :alt: All distributions with partialling-out score
            :align: center

References
++++++++++

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W. and Robins, J. (2018), Double/debiased
machine learning for treatment and structural parameters. The Econometrics Journal, 21: C1-C68.
doi:`10.1111/ectj.12097 <https://doi.org/10.1111/ectj.12097>`_.

Robinson, P. M. (1988). Root-N-consistent semi-parametric regression. Econometrica 56, 931-54.
doi:`10.2307/1912705 <https://doi.org/10.2307/1912705>`_.