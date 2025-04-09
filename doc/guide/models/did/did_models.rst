.. include:: /guide/models/did/did.rst

.. _did-pa-model:

Panel data
**********

Multi Period
^^^^^^^^^^^^

test

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            import doubleml as dml
            from doubleml.did.datasets import make_did_CS2021
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            np.random.seed(42)
            df = make_did_CS2021(n_obs=500) 
            dml_data = dml.data.DoubleMLPanelData(
                df,
                y_col="y",
                d_cols="d",
                id_col="id",
                t_col="t",
                x_cols=["Z1", "Z2", "Z3", "Z4"],
                datetime_unit="M"
            )
            dml_did_obj = dml.did.DoubleMLDIDMulti(
                obj_dml_data=dml_data,
                ml_g=ml_g,
                ml_m=ml_m,
                gt_combinations="standard",
                control_group="never_treated",
            )
            print(dml_did_obj.fit())

Single Period
^^^^^^^^^^^^^

.. include:: /guide/models/did/did_binary.rst

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

.. _did-cs-model:

Repeated cross-sections
***********************

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
