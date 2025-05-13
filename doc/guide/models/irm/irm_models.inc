The interactive regression model (IRM) take the form

.. math::

    Y = g_0(D, X) + U,

where treatment effects are fully heterogeneous.

.. _irm-model:

Binary Interactive Regression Model (IRM)
*****************************************

.. include:: /guide/models/irm/irm.rst

.. include:: /shared/causal_graphs/plr_irm_causal_graph.rst

``DoubleMLIRM`` implements IRM models.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
            print(dml_irm_obj.fit())

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            library(DoubleML)
            library(mlr3)
            library(mlr3learners)
            library(data.table)

            set.seed(3333)
            ml_g = lrn("regr.ranger", num.trees = 100, mtry = 10, min.node.size = 2, max.depth = 5)
            ml_m = lrn("classif.ranger", num.trees = 100, mtry = 10, min.node.size = 2, max.depth = 5)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type="data.table")
            obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
            dml_irm_obj = DoubleMLIRM$new(obj_dml_data, ml_g, ml_m)
            dml_irm_obj$fit()
            print(dml_irm_obj)

.. _irm-apo-model:

Average Potential Outcomes (APOs)
*********************************

.. include:: /guide/models/irm/apo.rst

``DoubleMLAPO`` implements the estimation of average potential outcomes.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_apo_obj = dml.DoubleMLAPO(obj_dml_data, ml_g, ml_m, treatment_level=0)
            print(dml_apo_obj.fit())


.. _irm-apos-model:

Average Potential Outcomes (APOs) for Multiple Treatment Levels
***************************************************************

.. include:: /guide/models/irm/apos.rst

``DoubleMLAPOS`` implements the estimation of average potential outcomes for multiple treatment levels.
Estimation is conducted via its ``fit()`` method. The ``causal_contrast()`` method allows to estimate causal contrasts between treatment levels:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_apos_obj = dml.DoubleMLAPOS(obj_dml_data, ml_g, ml_m, treatment_levels=[0, 1])
            print(dml_apos_obj.fit())

            causal_contrast_model = dml_apos_obj.causal_contrast(reference_levels=0)
            print(causal_contrast_model.summary)


.. _iivm-model:

Interactive IV model (IIVM)
***************************

.. include:: /guide/models/irm/iivm.rst

.. include:: /shared/causal_graphs/pliv_iivm_causal_graph.rst

``DoubleMLIIVM`` implements IIVM models.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

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

    .. tab-item:: R
        :sync: r

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