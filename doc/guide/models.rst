.. _models:

Models
----------

The :ref:`DoubleML <doubleml_package>` includes the following models.

.. _plr-model:

Partially linear regression model (PLR)
+++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/plr.rst

.. include:: ../shared/causal_graphs/plr_irm_causal_graph.rst

``DoubleMLPLR`` implements PLR models.
Estimation is conducted via its ``fit()`` method:

.. tabbed:: Python

    .. ipython:: python

        import numpy as np
        import doubleml as dml
        from doubleml.datasets import make_plr_CCDDHNR2018
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.base import clone

        learner = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_l = clone(learner)
        ml_m = clone(learner)
        np.random.seed(1111)
        data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m)
        print(dml_plr_obj.fit())

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)
        lgr::get_logger("mlr3")$set_threshold("warn")

        learner = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        ml_l = learner$clone()
        ml_m = learner$clone()
        set.seed(1111)
        data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=500, dim_x=20, return_type='data.table')
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
        dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)
        dml_plr_obj$fit()
        print(dml_plr_obj)


.. _pliv-model:

Partially linear IV regression model (PLIV)
+++++++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/pliv.rst

.. include:: ../shared/causal_graphs/pliv_iivm_causal_graph.rst

``DoubleMLPLIV`` implements PLIV models.
Estimation is conducted via its ``fit()`` method:

.. tabbed:: Python

    .. ipython:: python
        :okwarning:

        import numpy as np
        import doubleml as dml
        from doubleml.datasets import make_pliv_CHS2015
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.base import clone

        learner = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_l = clone(learner)
        ml_m = clone(learner)
        ml_r = clone(learner)
        np.random.seed(2222)
        data = make_pliv_CHS2015(alpha=0.5, n_obs=500, dim_x=20, dim_z=1, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd', z_cols='Z1')
        dml_pliv_obj = dml.DoubleMLPLIV(obj_dml_data, ml_l, ml_m, ml_r)
        print(dml_pliv_obj.fit())

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)

        learner = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        ml_l = learner$clone()
        ml_m = learner$clone()
        ml_r = learner$clone()
        set.seed(2222)
        data = make_pliv_CHS2015(alpha=0.5, n_obs=500, dim_x=20, dim_z=1, return_type="data.table")
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_col = "d", z_cols= "Z1")
        dml_pliv_obj = DoubleMLPLIV$new(obj_dml_data, ml_l, ml_m, ml_r)
        dml_pliv_obj$fit()
        print(dml_pliv_obj)


.. _irm-model:

Interactive regression model (IRM)
++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/irm.rst

.. include:: ../shared/causal_graphs/plr_irm_causal_graph.rst

``DoubleMLIRM`` implements IRM models.
Estimation is conducted via its ``fit()`` method:

.. tabbed:: Python

    .. ipython:: python

        import numpy as np
        import doubleml as dml
        from doubleml.datasets import make_irm_data
        from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

        ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        np.random.seed(3333)
        data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
        print(dml_irm_obj.fit())

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)

        set.seed(3333)
        ml_g = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        ml_m = lrn("classif.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type="data.table")
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
        dml_irm_obj = DoubleMLIRM$new(obj_dml_data, ml_g, ml_m)
        dml_irm_obj$fit()
        print(dml_irm_obj)


.. _iivm-model:

Interactive IV model (IIVM)
+++++++++++++++++++++++++++

.. include:: ../shared/models/iivm.rst

.. include:: ../shared/causal_graphs/pliv_iivm_causal_graph.rst

``DoubleMLIIVM`` implements IIVM models.
Estimation is conducted via its ``fit()`` method:

.. tabbed:: Python

    .. ipython:: python
        :okwarning:

        import numpy as np
        import doubleml as dml
        from doubleml.datasets import make_iivm_data
        from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

        ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_r = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        np.random.seed(4444)
        data = make_iivm_data(theta=0.5, n_obs=1000, dim_x=20, alpha_x=1.0, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd', z_cols='z')
        dml_iivm_obj = dml.DoubleMLIIVM(obj_dml_data, ml_g, ml_m, ml_r)
        print(dml_iivm_obj.fit())

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        library(mlr3)
        library(mlr3learners)
        library(data.table)

        set.seed(4444)
        ml_g = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        ml_m = lrn("classif.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
        ml_r = ml_m$clone()
        data = make_iivm_data(theta=0.5, n_obs=1000, dim_x=20, alpha_x=1, return_type="data.table")
        obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d", z_cols="z")
        dml_iivm_obj = DoubleMLIIVM$new(obj_dml_data, ml_g, ml_m, ml_r)
        dml_iivm_obj$fit()
        print(dml_iivm_obj)


Difference-in-Differences Models (DID)
++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/did.rst

Panel data
**********

If panel data are available, the observations are assumed to be iid. of form :math:`(Y_{i0}, Y_{i1}, D_i, X_i)`.
Remark that the difference :math:`\Delta Y_i= Y_{i1}-Y_{i0}` has to be defined as the outcome ``y`` in the ``DoubleMLData`` object.

``DoubleMLIDID`` implements difference-in-differences models for panel data.
Estimation is conducted via its ``fit()`` method:


.. ipython:: python
    :okwarning:

    import numpy as np
    import doubleml as dml
    from doubleml.datasets import make_did_SZ2020
    from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

    ml_g = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=5)
    ml_m = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=5)
    np.random.seed(42)
    data = make_did_SZ2020(n_obs=500, return_type='DataFrame') 
    # y is already defined a the difference of observed outcomes
    obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
    dml_did_obj = dml.DoubleMLDID(obj_dml_data, ml_g, ml_m)
    print(dml_did_obj.fit())

Repeated cross-section data
****************************

For repeated cross-sections, the observations are assumed to be iid. of form :math:`(Y_{i}, D_i, X_i, T_i)`,
where :math:`T_i` is a dummy variable if unit :math:`i` is observed pre- or post-treatment period, such 
that the observed outcome can be defined as 

.. math::

    Y_i = T_i Y_{i1} + (1-T_i) Y_{i0}.

Further, treatment and covariates are assumed to be stationary, such that the joint distribution of :math:`(D,X)` is invariant to :math:`T`.

``DoubleMLIDIDCS`` implements difference-in-differences models for repeated cross-sections.
Estimation is conducted via its ``fit()`` method:

.. ipython:: python
    :okwarning:

    import numpy as np
    import doubleml as dml
    from doubleml.datasets import make_did_SZ2020
    from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

    ml_g = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=5)
    ml_m = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=5)
    np.random.seed(42)
    data = make_did_SZ2020(n_obs=500, cross_sectional_data=True, return_type='DataFrame')
    obj_dml_data = dml.DoubleMLData(data, 'y', 'd', t_col='t')
    dml_did_obj = dml.DoubleMLDIDCS(obj_dml_data, ml_g, ml_m)
    print(dml_did_obj.fit())