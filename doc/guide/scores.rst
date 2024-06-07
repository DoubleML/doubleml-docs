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

.. _plr-score:

Partially linear regression model (PLR)
***************************************

For the PLR model implemented in ``DoubleMLPLR`` one can choose between
``score='partialling out'`` and ``score='IV-type'``.

``score='partialling out'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - \ell(X) - \theta (D - m(X))] [D - m(X)]

    &= - (D - m(X)) (D - m(X)) \theta + (Y - \ell(X)) (D - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(\ell,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - (D - m(X)) (D - m(X)),

    \psi_b(W; \eta) &= (Y - \ell(X)) (D - m(X)).

``score='IV-type'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - D \theta - g(X)] [D - m(X)]

    &= - D (D - m(X)) \theta + (Y - g(X)) (D - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - D (D - m(X)),

    \psi_b(W; \eta) &= (Y - g(X)) (D - m(X)).


Partially linear IV regression model (PLIV)
*******************************************


For the PLIV model implemented in ``DoubleMLPLIV`` one can choose between
``score='IV-type'`` and ``score='partialling out'``.

``score='partialling out'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - \ell(X) - \theta (D - r(X))] [Z - m(X)]

    &= - (D - r(X)) (Z - m(X)) \theta + (Y - \ell(X)) (Z - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(\ell, m, r)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - (D - r(X)) (Z - m(X)),

    \psi_b(W; \eta) &= (Y - \ell(X)) (Z - m(X)).

``score='IV-type'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - D \theta - g(X)] [Z - m(X)]

    &= - D (Z - m(X)) \theta + (Y - g(X)) (Z - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - D (Z - m(X)),

    \psi_b(W; \eta) &= (Y - g(X)) (Z - m(X)).


Interactive regression model (IRM)
**********************************

For the IRM model implemented in ``DoubleMLIRM`` one can choose between
``score='ATE'`` and ``score='ATTE'``.

``score='ATE'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= g(1,X) - g(0,X) + \frac{D (Y - g(1,X))}{m(X)} - \frac{(1 - D)(Y - g(0,X))}{1 - m(X)} - \theta

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - 1,

    \psi_b(W; \eta) &= g(1,X) - g(0,X) + \frac{D (Y - g(1,X))}{m(X)} - \frac{(1 - D)(Y - g(0,X))}{1 - m(X)}.

``score='ATTE'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= \frac{D (Y - g(0,X))}{p} - \frac{m(X) (1 - D) (Y - g(0,X))}{p(1 - m(X))} - \frac{D}{p} \theta

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, p)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - \frac{D}{p},

    \psi_b(W; \eta) &= \frac{D (Y - g(0,X))}{p} - \frac{m(X) (1 - D) (Y - g(0,X))}{p(1 - m(X))}.


Interactive IV model (IIVM)
***************************

For the IIVM model implemented in ``DoubleMLIIVM``
we employ for ``score='LATE'`` the score function:

``score='LATE'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) :=\; &g(1,X) - g(0,X)
    + \frac{Z (Y - g(1,X))}{m(X)} - \frac{(1 - Z)(Y - g(0,X))}{1 - m(X)}

    &- \bigg(r(1,X) - r(0,X) + \frac{Z (D - r(1,X))}{m(X)} - \frac{(1 - Z)(D - r(0,X))}{1 - m(X)} \bigg) \theta

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, r)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - \bigg(r(1,X) - r(0,X) + \frac{Z (D - r(1,X))}{m(X)} - \frac{(1 - Z)(D - r(0,X))}{1 - m(X)} \bigg),

    \psi_b(W; \eta) &= g(1,X) - g(0,X) + \frac{Z (Y - g(1,X))}{m(X)} - \frac{(1 - Z)(Y - g(0,X))}{1 - m(X)}.

Difference-in-Differences for Panel Data
****************************************

For the difference-in-differences model implemented in ``DoubleMLDID`` one can choose between
``score='observational'`` and ``score='experimental'``.

``score='observational'`` implements the score function (dropping the unit index :math:`i`):

.. math::

    \psi(W,\theta, \eta) 
    :&= -\frac{D}{\mathbb{E}_n[D]}\theta + \left(\frac{D}{\mathbb{E}_n[D]} - \frac{\frac{m(X) (1-D)}{1-m(X)}}{\mathbb{E}_n\left[\frac{m(X) (1-D)}{1-m(X)}\right]}\right) \left(Y_1 - Y_0 - g(0,X)\right)

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - \frac{D}{\mathbb{E}_n[D]},

    \psi_b(W; \eta) &= \left(\frac{D}{\mathbb{E}_n[D]} - \frac{\frac{m(X) (1-D)}{1-m(X)}}{\mathbb{E}_n\left[\frac{m(X) (1-D)}{1-m(X)}\right]}\right) \left(Y_1 - Y_0 - g(0,X)\right)

and the nuisance elements :math:`\eta=(g, m)` are defined as

.. math::

    g_{0}(0, X) &= \mathbb{E}[Y_1 - Y_0|D=0, X]

    m_0(X) &= P(D=1|X).

If ``in_sample_normalization='False'``, the score is set to

.. math::

    \psi(W,\theta,\eta) &= - \frac{D}{p}\theta + \frac{D - m(X)}{p(1-m(X))}\left(Y_1 - Y_0 -g(0,X)\right)

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, p)`, where :math:`p_0 = \mathbb{E}[D]` is estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.

``score='experimental'`` assumes that the treatment probability is independent of the covariates :math:`X` and
implements the score function:

.. math::

    \psi(W,\theta, \eta) 
    :=\; &-\theta + \left(\frac{D}{\mathbb{E}_n[D]} - \frac{1-D}{\mathbb{E}_n[1-D]}\right)\left(Y_1 - Y_0 -g(0,X)\right)

    &+ \left(1 - \frac{D}{\mathbb{E}_n[D]}\right) \left(g(1,X) - g(0,X)\right)

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) \;=  &- 1,

    \psi_b(W; \eta) \;= &\left(\frac{D}{\mathbb{E}_n[D]} - \frac{1-D}{\mathbb{E}_n[1-D]}\right)\left(Y_1 - Y_0 -g(0,X)\right)

    &+  \left(1 - \frac{D}{\mathbb{E}_n[D]}\right) \left(g(1,X) - g(0,X)\right)

and the nuisance elements :math:`\eta=(g)` are defined as

.. math::

    g_{0}(0, X) &= \mathbb{E}[Y_1 - Y_0|D=0, X]

    g_{0}(1, X) &= \mathbb{E}[Y_1 - Y_0|D=1, X]

Analogously, if ``in_sample_normalization='False'``,  the score is set to

.. math::

    \psi(W,\theta, \eta) 
    :=\; &-\theta +  \frac{D - p}{p(1-p)}\left(Y_1 - Y_0 -g(0,X)\right)

    &+ \left(1 - \frac{D}{p}\right) \left(g(1,X) - g(0,X)\right)

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, p)`, where :math:`p_0 = \mathbb{E}[D]` is estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.

Difference-in-Differences for repeated cross-sections
*****************************************************

For the difference-in-differences model implemented in ``DoubleMLDIDCS`` one can choose between
``score='observational'`` and ``score='experimental'``.

``score='observational'`` implements the score function (dropping the unit index :math:`i`):

.. math::

    \psi(W,\theta,\eta) :=\; & - \frac{D}{\mathbb{E}_n[D]}\theta + \frac{D}{\mathbb{E}_n[D]}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{m(X) (1-D)T}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)T}{1-m(X)}\right]^{-1} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-D)(1-T)}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)(1-T)}{1-m(X)}\right]^{-1} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) =\; &- \frac{D}{\mathbb{E}_n[D]},

    \psi_b(W; \eta) =\; &\frac{D}{\mathbb{E}_n[D]}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{m(X) (1-D)T}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)T}{1-m(X)}\right]^{-1} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-D)(1-T)}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)(1-T)}{1-m(X)}\right]^{-1} (Y-g(0,0,X))

and the nuisance elements :math:`\eta=(g)` are defined as

.. math::

    g_{0}(d, t, X) = \mathbb{E}[Y|D=d, T=t, X].

If ``in_sample_normalization='False'``, the score is set to

.. math::

    \psi(W,\theta,\eta) :=\; & - \frac{D}{p}\theta + \frac{D}{p}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{p\lambda} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{p(1-\lambda)}(Y - g(1,0,X))

    & - \frac{m(X) (1-D)T}{p(1-m(X))\lambda} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-D)(1-T)}{p(1-m(X))(1-\lambda)} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, p, \lambda)`, where :math:`p_0 = \mathbb{E}[D]` and :math:`\lambda_0 = \mathbb{E}[T]` are estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.

``score='experimental'`` assumes that the treatment probability is independent of the covariates :math:`X` and
implements the score function:

.. math::

    \psi(W,\theta,\eta) :=\; & - \theta + \Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{(1-D)T}{\mathbb{E}_n[(1-D)T]} (Y-g(0,1,X)) 

    & + \frac{(1-D)(1-T)}{\mathbb{E}_n[(1-D)(1-T)]} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) \;=  &- 1,

    \psi_b(W; \eta) \;= &\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{(1-D)T}{\mathbb{E}_n[(1-D)T]} (Y-g(0,1,X)) 

    & + \frac{(1-D)(1-T)}{\mathbb{E}_n[(1-D)(1-T)]} (Y-g(0,0,X))

and the nuisance elements :math:`\eta=(g, m)` are defined as

.. math::

    g_{0}(d, t, X) &= \mathbb{E}[Y|D=d, T=t, X]

    m_0(X) &= P(D=1|X).

Analogously, if ``in_sample_normalization='False'``,  the score is set to

.. math::

    \psi(W,\theta,\eta) :=\; & - \theta + \Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{p\lambda} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{p(1-\lambda)}(Y - g(1,0,X))

    & - \frac{(1-D)T}{(1-p)\lambda} (Y-g(0,1,X)) 

    & + \frac{(1-D)(1-T)}{(1-p)(1-\lambda)} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, p, \lambda)`, where :math:`p_0 = \mathbb{E}[D]` and :math:`\lambda_0 = \mathbb{E}[T]` are estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.

Potential quantiles (PQs)
*************************

For ``DoubleMLPQ`` the only valid option is ``score='PQ'``. For ``treatment=d`` with :math:`d\in\{0,1\}` and
a quantile :math:`\tau\in (0,1)` this implements the nonlinear score function:

.. math::

    \psi(W; \theta, \eta) := g_{d}(X, \tilde{\theta}) + \frac{1\{D=d\}}{m(X)}(1\{Y\le \theta\} - g_d(X, \tilde{\theta})) - \tau


where :math:`\eta=(g_d,m)` with true values

.. math::

    g_{d,0}(X, \theta_0) &= \mathbb{E}[1\{Y\le \theta_0\}|X, D=d]

    m_0(X) &= P(D=d|X).

Remark that :math:`g_{d,0}(X,\theta_0)` depends on the target parameter :math:`\theta_0`, such that
the score is estimated with a preliminary estimate :math:`\tilde{\theta}`. For further details, see `Kallus et al. (2019) <https://arxiv.org/abs/1912.12945>`_. 


Local potential quantiles (LPQs)
**********************************

For ``DoubleMLLPQ`` the only valid option is ``score='LPQ'``. For ``treatment=d`` with :math:`d\in\{0,1\}`, instrument :math:`Z` and
a quantile :math:`\tau\in (0,1)` this implements the nonlinear score function:

.. math::

    \psi(W; \theta, \eta) :=& \Big(g_{d, Z=1}(X, \tilde{\theta}) - g_{d, Z=0}(X, \tilde{\theta}) + \frac{Z}{m(X)}(1\{D=d\} \cdot 1\{Y\le \theta\} - g_{d, Z=1}(X, \tilde{\theta}))

    &\quad - \frac{1-Z}{1-m(X)}(1\{D=d\} \cdot 1\{Y\le \theta\} - g_{d, Z=0}(X, \tilde{\theta}))\Big) \cdot \frac{2d -1}{\gamma} - \tau


where :math:`\eta=(g_{d,Z=1}, g_{d,Z=0}, m, \gamma)` with true values

.. math::

    g_{d,Z=z,0}(X, \theta_0) &= \mathbb{E}[1\{D=d\} \cdot 1\{Y\le \theta_0\}|X, Z=z],\quad z\in\{0,1\}

    m_{Z=z,0}(X) &= P(D=d|X, Z=z),\quad z\in\{0,1\}

    m_0(X) &= P(Z=1|X)

    \gamma_0 &= \mathbb{E}[P(D=d|X, Z=1) - P(D=d|X, Z=0)].

Further, the compliance probability :math:`\gamma_0` is estimated with the two additional nuisance components 

.. math::

    m_{Z=z,0}(X) = P(D=d|X, Z=z),\quad z\in\{0,1\}.

Remark that :math:`g_{d,Z=z,0}(X, \theta_0)` depends on the target parameter :math:`\theta_0`, such that
the score is estimated with a preliminary estimate :math:`\tilde{\theta}`. For further details, see `Kallus et al. (2019) <https://arxiv.org/abs/1912.12945>`_.


Conditional value at risk (CVaR)
**********************************

For ``DoubleMLCVAR`` the only valid option is ``score='CVaR'``. For ``treatment=d`` with :math:`d\in\{0,1\}` and
a quantile :math:`\tau\in (0,1)` this implements the score function:

.. math::

    \psi(W; \theta, \eta) := g_{d}(X, \gamma) + \frac{1\{D=d\}}{m(X)}(\max(\gamma, (1 - \tau)^{-1}(Y - \tau \gamma))  - g_d(X, \gamma)) - \theta

where :math:`\eta=(g_d,m,\gamma)` with true values

.. math::

    g_{d,0}(X, \gamma_0) &= \mathbb{E}[\max(\gamma_0, (1 - \tau)^{-1}(Y - \tau \gamma_0))|X, D=d]

    m_0(X) &= P(D=d|X)

and :math:`\gamma_0` being the potential quantile of :math:`Y(d)`. As for potential quantiles, the estimate :math:`g_d` is constructed via
a preliminary estimate of :math:`\gamma_0`. For further details, see `Kallus et al. (2019) <https://arxiv.org/abs/1912.12945>`_.

.. _ssm-mar-score:

Missingness at Random
*********************

For ``DoubleMLSSM`` the ``score='missing-at-random'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) := \tilde{\psi}_1(W; \eta) - \tilde{\psi}_0(W; \eta) - \theta

where

.. math::

    \tilde{\psi}_1(W; \eta) &= \frac{D \cdot S \cdot [Y - g(1,1,X)]}{m(X) \cdot \pi(1, X)} + g(1,1,X)

    \tilde{\psi}_0(W; \eta) &= \frac{(1-D) \cdot S \cdot [Y - g(0,1,X)]}{(1-m(X)) \cdot \pi(0, X)} + g(0,1,X)

for :math:`d\in\{0,1\}` and :math:`\eta=(g, m, \pi)` with true values

.. math::

    g_0(d,s,X) &= \mathbb{E}[Y|D=d, S=s, X]

    m_0(X) &= P(D=1|X)

    \pi_0(d, X) &= P(S=1|D=d, X).


For further details, see `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.

.. _ssm-nr-score:

Nonignorable Nonresponse
************************

For ``DoubleMLSSM`` the ``score='nonignorable'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) := \tilde{\psi}_1(W; \eta) - \tilde{\psi}_0(W; \eta) - \theta

where

.. math::

    \tilde{\psi}_1(W; \eta) &= \frac{D \cdot S \cdot [Y - g(1,1,X,\Pi)]}{m(X, \Pi) \cdot \pi(1,X,Z)} + g(1,1,X,\Pi)

    \tilde{\psi}_0(W; \eta) &= \frac{(1-D) \cdot S \cdot [Y - g(0,1,X,\Pi)]}{(1-m(X,\Pi)) \cdot \pi(0,X,Z)} + g(0,1,X,\Pi)

for :math:`d\in\{0,1\}` and :math:`\eta=(g, m, \pi, \Pi)` with true values

.. math::

    \pi_0(d, X, Z) &= P(S=1|D=d, X, Z)

    \Pi_0 &:= \pi_0(D, Z, X) = P(S=1|D,X,Z)
    
    g_0(d,s,X) &= \mathbb{E}[Y|D=d, S=s, X, \Pi_0]

    m_0(X, \Pi_0) &= P(D=1|X, \Pi_0).

The estimate of :math:`\Pi_0` is constructed via a preliminary estimate of :math:`\pi_0(D,X,Z)` via nested cross-fitting.

For further details, see `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.

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

