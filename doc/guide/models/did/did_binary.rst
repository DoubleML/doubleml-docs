**Difference-in-Differences Models (DID)** implemented in the package focus on the the binary treatment case with
with two treatment periods.

Adopting the notation from `Sant'Anna and Zhao (2020) <https://doi.org/10.1016/j.jeconom.2020.06.003>`_, 
let :math:`Y_{it}` be the outcome of interest for unit :math:`i` at time :math:`t`. Further, let :math:`D_{it}=1` indicate 
if unit :math:`i` is treated before time :math:`t` (otherwise :math:`D_{it}=0`). Since all units start as untreated (:math:`D_{i0}=0`), define 
:math:`D_{i}=D_{i1}.` Relying on the potential outcome notation, denote :math:`Y_{it}(0)` as the outcome of unit :math:`i` at time :math:`t` if the unit did not receive 
treatment up until time :math:`t` and analogously for :math:`Y_{it}(1)` with treatment. Consequently, the observed outcome 
for unit is :math:`i` at time :math:`t` is :math:`Y_{it}=D_{it} Y_{it}(1) + (1-D_{it}) Y_{it}(0)`. Further, let 
:math:`X_i` be a vector of pre-treatment covariates.

Target parameter of interest is the average treatment effect on the treated (ATTE)

.. math::

    \theta_0 = \mathbb{E}[Y_{i1}(1)- Y_{i1}(0)|D_i=1].

The corresponding identifying assumptions are

- **(Cond.) Parallel Trends:** :math:`\mathbb{E}[Y_{i1}(0) - Y_{i0}(0)|X_i, D_i=1] = \mathbb{E}[Y_{i1}(0) - Y_{i0}(0)|X_i, D_i=0]\quad a.s.`
- **Overlap:** :math:`\exists\epsilon > 0`: :math:`P(D_i=1) > \epsilon` and :math:`P(D_i=1|X_i) \le 1-\epsilon\quad a.s.`

.. note::
    For a more detailed introduction and recent developments of the difference-in-differences literature see e.g. `Roth et al. (2022) <https://arxiv.org/abs/2201.01194>`_.


Panel Data
~~~~~~~~~~~

If panel data are available, the observations are assumed to be iid. of form :math:`(Y_{i0}, Y_{i1}, D_i, X_i)`.
Remark that the difference :math:`\Delta Y_i= Y_{i1}-Y_{i0}` has to be defined as the outcome ``y`` in the ``DoubleMLData`` object.

``DoubleMLIDID`` implements difference-in-differences models for panel data.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            import doubleml as dml
            from doubleml.did.datasets import make_did_SZ2020
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=5)
            ml_m = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=5)
            np.random.seed(42)
            data = make_did_SZ2020(n_obs=500, return_type='DataFrame') 
            # y is already defined as the difference of observed outcomes
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_did_obj = dml.DoubleMLDID(obj_dml_data, ml_g, ml_m)
            print(dml_did_obj.fit())


Repeated cross-sections
~~~~~~~~~~~~~~~~~~~~~~~~~

For repeated cross-sections, the observations are assumed to be iid. of form :math:`(Y_{i}, D_i, X_i, T_i)`,
where :math:`T_i` is a dummy variable if unit :math:`i` is observed pre- or post-treatment period, such 
that the observed outcome can be defined as 

.. math::

    Y_i = T_i Y_{i1} + (1-T_i) Y_{i0}.

Further, treatment and covariates are assumed to be stationary, such that the joint distribution of :math:`(D,X)` is invariant to :math:`T`.

``DoubleMLIDIDCS`` implements difference-in-differences models for repeated cross-sections.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            import doubleml as dml
            from doubleml.did.datasets import make_did_SZ2020
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=5)
            ml_m = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=5)
            np.random.seed(42)
            data = make_did_SZ2020(n_obs=500, cross_sectional_data=True, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd', t_col='t')
            dml_did_obj = dml.DoubleMLDIDCS(obj_dml_data, ml_g, ml_m)
            print(dml_did_obj.fit())
