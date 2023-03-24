.. _heterogeneity:

Heterogeneous Treatment Effects
----------------------------------------

All implemented solutions focus on the :ref:`IRM <irm-model>` or :ref:`IIVM <iivm-model>` models, as for 
the :ref:`PLR <plr-model>` and :ref:`PLIV <pliv-model>` models heterogeneous treatment effects can be usually modelled 
via feature construction.


.. _gates:

Group Average Treatment Effects (GATEs)
++++++++++++++++++++++++++++++++++++++++++++++

The ``DoubleMLIRM`` class contains the ``gate()`` method, which enables the estimation and construction of confidence intervals
for GATEs after fitting the ``DoubleMLIRM`` object. To estimate GATEs, the user has to specify a pandas ``DataFrame`` containing
the groups (dummy coded or one column with strings).
This will construct and fit a ``DoubleMLBLP`` object. Confidence intervals can then be constructed via 
the ``confint()`` method. Jointly valid confidence intervals will be based on a gaussian multiplier bootstrap.

.. tabbed:: Python

    .. ipython:: python

        import numpy as np
        import pandas as pd
        import doubleml as dml
        from doubleml.datasets import make_irm_data
        from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

        ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        np.random.seed(3333)
        data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
        _ = dml_irm_obj.fit()

        # define groups
        np.random.seed(42)
        groups = pd.DataFrame(np.random.choice(3, 500), columns=['Group'], dtype=str)
        print(groups.head())

        gate_obj = dml_irm_obj.gate(groups=groups)
        ci = gate_obj.confint()
        print(ci)


A more detailed notebook on GATEs is available in the :ref:`example gallery <examplegallery>`.

.. _cates:

Conditional Average Treatment Effects (CATEs)
++++++++++++++++++++++++++++++++++++++++++++++

The ``DoubleMLIRM`` class contains the ``cate()`` method, which enables the estimation and construction of confidence intervals
for CATEs after fitting the ``DoubleMLIRM`` object. To estimate CATEs, the user has to specify a pandas ``DataFrame`` containing
the basis (e.g. B-splines) for the conditional treatment effects.
This will construct and fit a ``DoubleMLBLP`` object. Confidence intervals can then be constructed via 
the ``confint()`` method. Jointly valid confidence intervals will be based on a gaussian multiplier bootstrap.

.. tabbed:: Python

    .. ipython:: python

        import numpy as np
        import pandas as pd
        import patsy

        import doubleml as dml
        from doubleml.datasets import make_irm_data
        from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

        ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
        np.random.seed(3333)
        data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
        _ = dml_irm_obj.fit()

        # define a basis with respect to the first variable
        design_matrix = patsy.dmatrix("bs(x, df=5, degree=2)", {"x":obj_dml_data.data["X1"]})
        spline_basis = pd.DataFrame(design_matrix)
        print(spline_basis.head())

        cate_obj = dml_irm_obj.cate(basis=spline_basis)
        ci = cate_obj.confint()
        print(ci.head())


A more detailed notebook on CATEs is available in the :ref:`example gallery <examplegallery>`. 
The examples also include the construction of a two-dimensional basis with B-splines.

.. _qtes:

Quantiles
++++++++++++++++++++++++++++++++++++++++++++++

The :ref:`DoubleML <doubleml-package>` package includes (local) quantile estimation for potential outcomes for
:ref:`IRM <irm-model>` and :ref:`IIVM <iivm-model>` models.

Potential Quantiles (PQs)
*******************************************

.. include:: ../shared/heterogeneity/pq.rst

``DoubleMLPQ`` implements potential quantile estimation. Estimation is conducted via its ``fit()`` method: 

.. tabbed:: Python

    .. ipython:: python

        import numpy as np
        import doubleml as dml
        from doubleml.datasets import make_irm_data
        from sklearn.ensemble import RandomForestClassifier
        np.random.seed(3141)
        ml_g = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
        ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
        data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
        dml_pq_obj = dml.DoubleMLPQ(obj_dml_data, ml_g, ml_m, treatment=1, quantile=0.5)
        dml_pq_obj.fit().summary

``DoubleMLLPQ`` implements local potential quantile estimation. Estimation is conducted via its ``fit()`` method: 

.. tabbed:: Python

    .. ipython:: python

        import numpy as np
        import doubleml as dml
        from doubleml.datasets import make_iivm_data
        from sklearn.ensemble import RandomForestClassifier
        np.random.seed(3141)
        ml_g = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
        ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
        data = make_iivm_data(theta=0.5, n_obs=1000, dim_x=20, return_type='DataFrame')
        obj_dml_data = dml.DoubleMLData(data, 'y', 'd', z_cols='z')
        dml_lpq_obj = dml.DoubleMLLPQ(obj_dml_data, ml_g, ml_m, treatment=1, quantile=0.5)
        dml_lpq_obj.fit().summary

Quantile Treatment Effects (QTEs)
*******************************************

A detailed notebook on PQs and QTEs is available in the :ref:`example gallery <examplegallery>`. 

Conditional Value at Risk (CVaR)
++++++++++++++++++++++++++++++++++++++++++++

All implemented solutions focus on the :ref:`IRM <irm-model>` models

CVaR of Potential Outcomes
*******************************************

CVaR Treatment Effect
*******************************************

A detailed notebook on conditional value at risk estimation
is available in the :ref:`example gallery <examplegallery>`. 




