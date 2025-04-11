.. _scores:

Score functions
---------------

We use method-of-moments estimators for the target parameter :math:`\theta_0` based upon the empirical analog of the
moment condition

.. math::

    \mathbb{E}[ \psi(W; \theta_0, \eta_0)] = 0,

where we call :math:`\psi` the **score function**, :math:`W=(Y,D,X,Z)`,
:math:`\theta_0` is the parameter of interest and
:math:`\eta` denotes nuisance functions with population value :math:`\eta_0`.
We use score functions :math:`\psi(W; \theta, \eta)` that satisfy
:math:`\mathbb{E}[ \psi(W; \theta_0, \eta_0)] = 0` with :math:`\theta_0` being the unique solution
and that obey the **Neyman orthogonality condition**

.. math::

    \partial_{\eta} \mathbb{E}[ \psi(W; \theta_0, \eta)] \bigg|_{\eta=\eta_0} = 0.

The score functions of many double machine learning models (PLR, PLIV, IRM, IIVM) are linear in the parameter
:math:`\theta`, i.e.,

.. math::

    \psi(W; \theta, \eta) = \psi_a(W; \eta) \theta + \psi_b(W; \eta).

Hence the estimator can be written as

.. math::

    \tilde{\theta}_0 = - \frac{\mathbb{E}_N[\psi_b(W; \eta)]}{\mathbb{E}_N[\psi_a(W; \eta)]}.

The linearity of the score function in the parameter :math:`\theta` allows the implementation of key components in a very
general way.
The methods and algorithms to estimate the causal parameters, to estimate their standard errors, to perform a multiplier
bootstrap, to obtain confidence intervals and many more are implemented in the abstract base class ``DoubleML``.
The object-oriented architecture therefore allows for easy extension to new model classes for double machine learning.
This is doable with very minor effort.

If the linearity of the score function is not satisfied, the computations are more involved.
In the Python package ``DoubleML``, the functionality around the score functions is implemented in mixin classes called
``LinearScoreMixin`` and ``NonLinearScoreMixin``.
The R package currently only comes with an implementation for linear score functions.
In case of a non-linear score function, the parameter estimate :math:`\tilde{\theta}_0` is obtained via numerical root
search of the empirical analog of the moment condition :math:`\mathbb{E}[ \psi(W; \theta_0, \eta_0)] = 0`.

Implementation of the score function and the estimate of the causal parameter
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
            print(dml_plr_obj)

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
            data = make_plr_CCDDHNR2018(alpha=0.5, return_type='data.table')
            obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
            dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)
            dml_plr_obj$fit()
            print(dml_plr_obj)

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

The values of the score function components :math:`\psi_a(W_i; \hat{\eta}_0)` and :math:`\psi_b(W_i; \hat{\eta}_0)`
are stored in the attributes ``psi_elements['psi_a']`` and ``psi_elements['psi_b']`` (Python package ``DoubleML``)
and ``psi_a`` and ``psi_b`` (R package ``DoubleML``).
In the attribute ``psi`` the values of the score function :math:`\psi(W_i; \tilde{\theta}_0, \hat{\eta}_0)` are stored.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj.psi[:5])

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            print(dml_plr_obj$psi[1:5, ,1])


Implemented Neyman orthogonal score functions
+++++++++++++++++++++++++++++++++++++++++++++

.. _plm-scores:

Partially linear models (PLM)
*****************************

.. include:: scores/plm/plm_scores.inc


.. _irm-scores:

Interactive regression models (IRM)
***********************************

.. include:: scores/irm/irm_scores.inc


.. _did-scores:

Difference-in-Differences Models
********************************

.. include:: scores/did/did_scores.inc


.. _ssm-scores:

Sample Selection Models
************************

.. include:: scores/ssm/ssm_scores.inc


Specifying alternative score functions via callables
++++++++++++++++++++++++++++++++++++++++++++++++++++

Via callables user-written score functions can be used.
This functionality is at the moment only implemented for specific model classes in Python.
For the PLR model implemented in ``DoubleMLPLR`` an alternative score function can be
set via ``score``.
Choose a callable object / function with signature ``score(y, d, g_hat, m_hat, smpls)`` which returns
the two score components :math:`\psi_a()` and :math:`\psi_b()`.

For example, the non-orthogonal score function

.. math::

    \psi(W; \theta, \eta) = [Y - D \theta - g(X)] D

can be obtained with

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np

            def non_orth_score(y, d, l_hat, m_hat, g_hat, smpls):
                u_hat = y - g_hat
                psi_a = -np.multiply(d, d)
                psi_b = np.multiply(d, u_hat)
                return psi_a, psi_b

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            non_orth_score = function(y, d, l_hat, m_hat, g_hat, smpls) {
                u_hat = y - g_hat
                psi_a = -1*d*d
                psi_b = d*u_hat
                psis = list(psi_a = psi_a, psi_b = psi_b)
                return(psis)
            }

Use ``DoubleMLPLR`` with ``inf_model=non_orth_score`` in order to obtain the estimator

.. math::

    \tilde{\theta}_0 = - \frac{\mathbb{E}_N[D (Y-g(X))]}{\mathbb{E}_N[D^2]}

when applying ``fit()``.
Note that this estimate will in general be prone to a regularization bias, see also :ref:`bias_non_orth`.

