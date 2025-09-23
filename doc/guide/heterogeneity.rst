.. _heterogeneity:

Heterogeneous treatment effects
----------------------------------------

Most implemented solutions focus on the :ref:`IRM <irm-model>` or :ref:`IIVM <iivm-model>` models, as for 
the :ref:`PLR <plr-model>` and :ref:`PLIV <pliv-model>` models heterogeneous treatment effects can be usually modelled 
via feature construction.


.. _gates:

Group average treatment effects (GATEs)
++++++++++++++++++++++++++++++++++++++++++++++

The ``DoubleMLIRM`` and ``DoubleMLPLR`` classes contain the ``gate()`` method, which enables the estimation and construction of confidence intervals
for GATEs after fitting the ``DoubleML`` object. To estimate GATEs, the user has to specify a pandas ``DataFrame`` containing
the groups (dummy coded or one column with strings).
This will construct and fit a ``DoubleMLBLP`` object. Confidence intervals can then be constructed via 
the ``confint()`` method. Jointly valid confidence intervals will be based on a gaussian multiplier bootstrap.

GATEs for IRM models
*********************

.. include:: ../shared/heterogeneity/gate.rst

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
    
            import numpy as np
            import pandas as pd
            import doubleml as dml
            from doubleml.irm.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_features=5, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=5, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
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


A more detailed notebook on GATEs with ``DoubleMLIRM`` models is available in the :ref:`example gallery <examplegallery>`.

GATEs for PLR models
*********************

.. include:: ../shared/heterogeneity/gate_plr.rst

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import pandas as pd
            import doubleml as dml
            from doubleml.plm.datasets import make_plr_CCDDHNR2018
            from sklearn.ensemble import RandomForestRegressor

            ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            dml_data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=500, dim_x=20)
            dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_g, ml_m)
            _ = dml_plr_obj.fit()

            # define groups
            np.random.seed(42)
            groups = pd.DataFrame(np.random.choice(3, 500), columns=['Group'], dtype=str)
            print(groups.head())

            gate_obj = dml_plr_obj.gate(groups=groups)
            ci = gate_obj.confint()
            print(ci)

A more detailed notebook on GATEs with ``DoubleMLPLR`` models is available in the :ref:`example gallery <examplegallery>`.

.. _cates:

Conditional average treatment effects (CATEs)
++++++++++++++++++++++++++++++++++++++++++++++

The ``DoubleMLIRM`` and ``DoubleMLPLR`` classes contain the ``cate()`` method, which enables the estimation and construction of confidence intervals
for CATEs after fitting the ``DoubleML`` object. To estimate CATEs, the user has to specify a pandas ``DataFrame`` containing
the basis (e.g. B-splines) for the conditional treatment effects.
This will construct and fit a ``DoubleMLBLP`` object. Confidence intervals can then be constructed via 
the ``confint()`` method. Jointly valid confidence intervals will be based on a gaussian multiplier bootstrap.

CATEs for IRM models
*********************

.. include:: ../shared/heterogeneity/cate.rst

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import pandas as pd
            import patsy

            import doubleml as dml
            from doubleml.irm.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor

            ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
            _ = dml_irm_obj.fit()

            # define a basis with respect to the first variable
            design_matrix = patsy.dmatrix("bs(x, df=5, degree=2)", {"x":obj_dml_data.data["X1"]})
            spline_basis = pd.DataFrame(design_matrix)
            print(spline_basis.head())

            cate_obj = dml_irm_obj.cate(basis=spline_basis)
            ci = cate_obj.confint(basis=spline_basis)
            print(ci.head())

A more detailed notebook on CATEs for ``DoubleMLIRM`` models is available in the :ref:`example gallery <examplegallery>`. 
The examples also include the construction of a two-dimensional basis with B-splines.

CATEs for PLR models
*********************

.. include:: ../shared/heterogeneity/cate_plr.rst

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import pandas as pd
            import patsy

            import doubleml as dml
            from doubleml.plm.datasets import make_plr_CCDDHNR2018
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            dml_data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=500, dim_x=20)
            dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_g, ml_m)
            _ = dml_plr_obj.fit()

            # define a basis with respect to the first variable
            design_matrix = patsy.dmatrix("bs(x, df=5, degree=2)", {"x":obj_dml_data.data["X1"]})
            spline_basis = pd.DataFrame(design_matrix)
            print(spline_basis.head())

            cate_obj = dml_plr_obj.cate(basis=spline_basis)
            ci = cate_obj.confint(basis=spline_basis)
            print(ci.head())

A more detailed notebook on CATEs for ``DoubleMLPLR`` models is available in the :ref:`example gallery <examplegallery>`. 

**Theory:** In the model above, it holds

.. math::

    \mathbb{E}[Y|X] &= \mathbb{E}[\theta_0(X) D|X] + \mathbb{E}[g_0(X)|X] + \underbrace{\mathbb{E}[\varepsilon|X]}_{=\mathbb{E}[\mathbb{E}[\varepsilon|D, X]|X]=0}\\
    &=\theta_0(X) \mathbb{E}[D|X] + g_0(X)

such that 

.. math::

    \underbrace{Y - \mathbb{E}[Y|X]}_{=:\tilde{Y}} = \theta_0(X) (\underbrace{D - \mathbb{E}[D|X]}_{=:\tilde{D}}) + \varepsilon.

Remark that for the generated :math:`\sigma`-agebras :math:`\sigma(\tilde{D})\subseteq \sigma(D,X)` implying

.. math::

    \mathbb{E}[\epsilon|\tilde{D}] = \mathbb{E}[\mathbb{E}[\epsilon|X, D]|\tilde{D}] = 0

and consequently

.. math::

    \mathbb{E}[\tilde{Y}|\tilde{D}] = \theta_0(X)\tilde{D}.

Consequently, :math:`\theta_0(X)` can be estimated by regressing :math:`\tilde{Y}` on :math:`\tilde{D}`:

.. math::

    \theta_0(X) = \arg\min_{\theta(X) \in \Theta}\mathbb{E}[(\tilde{Y} - \theta(X)\tilde{D})^2]

The :ref:`DoubleML <doubleml_package>` implementation approximates the effect :math:`\theta_0(X)` by a linear projection on a supplied basis :math:`\phi(X)`:

.. math::

    \theta_0(X) \approx \beta_0^T \phi(X)

where :math:`\beta_0` are coefficients to be estimated. 
The coverage of the confidence intervals is meant to include the the approximation :math:`\beta_0^T\phi(X)`.

.. _weighted_cates:

Weighted Average Treatment Effects
+++++++++++++++++++++++++++++++++++

The ``DoubleMLIRM`` class allows to specify weights via the ``weights`` argument in the initialization of the ``DoubleMLIRM`` object.
Given some weights, :math:`\omega(Y,D,X)` the model identifies the weighted average treatment effect

.. math::

    \theta_0 = \mathbb{E}[(g_0(1,X) - g_0(0,X))\omega(Y,D,X)].

The interpretation depends on the choice of weights. The simplest examples include

- :math:`\omega(Y,D,X) = 1` which corresponds to the average treatment effect (ATE)
- :math:`\omega(Y,D,X) = \frac{1\{X\in G\}}{P(X\in G)}` which corresponds to the group average treatment effect (GATE) for group :math:`G`
- :math:`\omega(Y,D,X) = \pi(X)` which corresponds to the average value of policy :math:`\pi`, where :math:`0\le \pi \le 1`

where the weights :math:`\omega(Y,D,X)` only depend on the features :math:`X`.

In these cases the weights can be specified as an array via the ``weights`` argument in the initialization of the ``DoubleMLIRM`` object.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import pandas as pd

            import doubleml as dml
            from doubleml.irm.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor

            ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            weights = np.ones(500)
            dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m, weights=weights)
            _ = dml_irm_obj.fit()
            print(dml_irm_obj.summary)

If the weights do not only depend on the features :math:`X`, but e.g. also on the treatment :math:`D` estimation becomes more involved.
To identifiy the correct parameter not only the weights :math:`\omega(Y,D,X)` but also their conditional expectation 

.. math::

    \bar{\omega}(X) = \mathbb{E}[\omega(Y,D,X)|X]

has to be specified. A common example is the average treatment effect on the treated (ATTE) which can be identified by setting

- :math:`\omega(Y,D,X) = \frac{D}{P(D=1)}`
- :math:`\bar{\omega}(X) = \frac{\mathbb{E}[D|X]}{P(D=1)} = \frac{m_0(X)}{P(D=1)}`

which depends on the propensity score :math:`m_0(X)`. 
In this case the weights can be specified as a ``dictionary`` the ``weights`` argument in the initialization of the ``DoubleMLIRM`` object.

One other important example would be the sensitivity analysis for group average treatment effects on the treated (GATET).
In this case the weights would take the following form

- :math:`\omega(Y,D,X) = \frac{1\{D=1, X\in G\}}{P(D=1, X\in G)}= \frac{D \cdot 1\{X\in G\}}{P(D=1, X\in G)}`
- :math:`\bar{\omega}(X) = \frac{\mathbb{E}[D|X]1\{X\in G\}}{P(D=1, X\in G)} = \frac{m_0(X)1\{X\in G\}}{P(D=1, X\in G)}.`

To simplify the specification of the weights, the ``DoubleMLIRM`` with ``score='ATTE'`` accepts binary weights, which should correspond to :math:`1\{X\in G\}`. 
This automatically relies on the propensity score :math:`m(X)` to construct the weights mentioned above (e.g. for weights equal to one this refers to the average treatment effect on the treated).

A more detailed notebook on weighted average treatment effects for on GATE sensitivity analysis is available in the :ref:`example gallery <examplegallery>`. 

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
            from doubleml.irm.datasets import make_irm_data
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
            from doubleml.irm.datasets import make_iivm_data
            from sklearn.ensemble import RandomForestClassifier
            np.random.seed(3141)
            ml_g = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=10, min_samples_leaf=2)
            data = make_iivm_data(theta=0.5, n_obs=2000, dim_x=20, return_type='DataFrame')
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
            from doubleml.irm.datasets import make_irm_data
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
            from doubleml.irm.datasets import make_irm_data
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
            from doubleml.irm.datasets import make_irm_data
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
            from doubleml.irm.datasets import make_irm_data
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
            np.random.seed(3333)
            data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
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




