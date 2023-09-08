.. _heterogeneity:

Heterogeneous treatment effects
----------------------------------------

All implemented solutions focus on the :ref:`IRM <irm-model>` or :ref:`IIVM <iivm-model>` models, as for 
the :ref:`PLR <plr-model>` and :ref:`PLIV <pliv-model>` models heterogeneous treatment effects can be usually modelled 
via feature construction.


.. _gates:

Group average treatment effects (GATEs)
++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/heterogeneity/gate.rst

The ``DoubleMLIRM`` class contains the ``gate()`` method, which enables the estimation and construction of confidence intervals
for GATEs after fitting the ``DoubleMLIRM`` object. To estimate GATEs, the user has to specify a pandas ``DataFrame`` containing
the groups (dummy coded or one column with strings).
This will construct and fit a ``DoubleMLBLP`` object. Confidence intervals can then be constructed via 
the ``confint()`` method. Jointly valid confidence intervals will be based on a gaussian multiplier bootstrap.

.. tab-set::

    .. tab-item:: Python
        :sync: py

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

Conditional average treatment effects (CATEs)
++++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/heterogeneity/cate.rst

The ``DoubleMLIRM`` class contains the ``cate()`` method, which enables the estimation and construction of confidence intervals
for CATEs after fitting the ``DoubleMLIRM`` object. To estimate CATEs, the user has to specify a pandas ``DataFrame`` containing
the basis (e.g. B-splines) for the conditional treatment effects.
This will construct and fit a ``DoubleMLBLP`` object. Confidence intervals can then be constructed via 
the ``confint()`` method. Jointly valid confidence intervals will be based on a gaussian multiplier bootstrap.

.. tab-set::

    .. tab-item:: Python
        :sync: py

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

The :ref:`DoubleML <doubleml_package>` package includes (local) quantile estimation for potential outcomes for
:ref:`IRM <irm-model>` and :ref:`IIVM <iivm-model>` models.

Potential quantiles (PQs)
*******************************************

.. include:: ../shared/heterogeneity/pq.rst

``DoubleMLPQ`` implements potential quantile estimation. Estimation is conducted via its ``fit()`` method: 

.. tab-set::

    .. tab-item:: Python
        :sync: py

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

``DoubleMLLPQ`` implements local potential quantile estimation, where the argument ``treatment`` indicates the potential outcome.
Estimation is conducted via its ``fit()`` method: 

.. tab-set::

    .. tab-item:: Python
        :sync: py

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


Quantile treatment effects (QTEs)
*******************************************

.. include:: ../shared/heterogeneity/qte.rst

``DoubleMLQTE`` implements quantile treatment effect estimation. Estimation is conducted via its ``fit()`` method: 

.. tab-set::

    .. tab-item:: Python
        :sync: py

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
            dml_qte_obj = dml.DoubleMLQTE(obj_dml_data, ml_g, ml_m, score='PQ', quantiles=[0.25, 0.5, 0.75])
            dml_qte_obj.fit().summary

To estimate local quantile effects the ``score`` argument has to be set to ``'LPQ'``.
A detailed notebook on PQs and QTEs is available in the :ref:`example gallery <examplegallery>`. 

Conditional value at risk (CVaR)
++++++++++++++++++++++++++++++++++++++++++++

The :ref:`DoubleML <doubleml_package>` package includes conditional value at risk estimation for
:ref:`IRM <irm-model>` models.

CVaR of potential outcomes
*******************************************

.. include:: ../shared/heterogeneity/cvar.rst

``DoubleMLCVAR`` implements conditional value at risk estimation for potential outcomes, where the argument ``treatment`` indicates the potential outcome.
Estimation is conducted via its ``fit()`` method: 

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.datasets import make_irm_data
            from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
            np.random.seed(3141)
            ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_cvar_obj = dml.DoubleMLCVAR(obj_dml_data, ml_g, ml_m, treatment=1, quantile=0.5)
            dml_cvar_obj.fit().summary


CVaR treatment effects
*******************************************

.. include:: ../shared/heterogeneity/cvar_qte.rst

``DoubleMLQTE`` implements CVaR treatment effect estimation, if the ``score`` argument has been set to ``'CVaR'`` (default is ``'PQ'``).
Estimation is conducted via its ``fit()`` method: 

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.datasets import make_irm_data
            from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
            np.random.seed(3141)
            ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_cvar_obj = dml.DoubleMLQTE(obj_dml_data, ml_g, ml_m, score='CVaR', quantiles=[0.25, 0.5, 0.75])
            dml_cvar_obj.fit().summary

A detailed notebook on CVaR estimation for potential outcomes and treatment effects
is available in the :ref:`example gallery <examplegallery>`. 

Policy Learning with Trees
++++++++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/heterogeneity/policytree.rst

The ``DoubleMLIRM`` class contains the ``policy_tree()`` method, which enables the estimation of a policy tree 
using weighted classification after fitting the ``DoubleMLIRM`` object. To estimate a policy tree, the user has to specify a pandas ``DataFrame`` containing
the covariates on based on which the policy will make treatment decisions. These can be either the original covariates used in the
``DoubleMLIRM`` estimation, or a subset, or new covariates.
This will construct and fit a ``DoubleMLPolicyTree`` object. A plot of the decision rules can be displayed by the
``plot_tree()`` method. The ``predict()`` method enables the application of the estimated policy on new data.
The ``depth`` parameter, which defaults to ``2``, can be used to adjust the maximum depth of the tree.

.. tab-set::

    .. tab-item:: Python
        :sync: py

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

            # define features to learn policy on 
            np.random.seed(42)
            features = data[["X1","X2","X3"]]
            print(features.head())

            # fits a tree of depth 2
            policy_tree_obj = dml_irm_obj.policy_tree(features=features)
            policy_tree_obj.plot_tree();

A more detailed notebook on Policy Trees is available in the :ref:`example gallery <examplegallery>`.




