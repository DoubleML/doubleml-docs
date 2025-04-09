.. _models:

Models
----------

The :ref:`DoubleML <doubleml_package>` includes the following models.

Partially linear models (PLM)
+++++++++++++++++++++++++++++

The partially linear models (PLM) take the form

.. math::

    Y = D \theta_0 + g_0(X) + \zeta,

where treatment effects are additive with some sort of linear form.

.. _plr-model:

Partially linear regression model (PLR)
***************************************

.. include:: ../shared/models/plr.rst

.. include:: ../shared/causal_graphs/plr_irm_causal_graph.rst

``DoubleMLPLR`` implements PLR models.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

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
            set.seed(1111)
            data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=500, dim_x=20, return_type='data.table')
            obj_dml_data = DoubleMLData$new(data, y_col="y", d_cols="d")
            dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m)
            dml_plr_obj$fit()
            print(dml_plr_obj)


.. _pliv-model:

Partially linear IV regression model (PLIV)
*******************************************

.. include:: ../shared/models/pliv.rst

.. include:: ../shared/causal_graphs/pliv_iivm_causal_graph.rst

``DoubleMLPLIV`` implements PLIV models.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

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

    .. tab-item:: R
        :sync: r

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


Interactive regression models (IRM)
++++++++++++++++++++++++++++++++++++

The interactive regression model (IRM) take the form

.. math::

    Y = g_0(D, X) + U,

where treatment effects are fully heterogeneous.

.. _irm-model:

Binary Interactive Regression Model (IRM)
*****************************************

.. include:: ../shared/models/irm.rst

.. include:: ../shared/causal_graphs/plr_irm_causal_graph.rst

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

.. include:: ../shared/models/apo.rst

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

.. include:: ../shared/models/apos.rst

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

.. include:: ../shared/models/iivm.rst

.. include:: ../shared/causal_graphs/pliv_iivm_causal_graph.rst

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


.. _did-model:

Difference-in-Differences Models (DID)
++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/did.rst


.. _did-pa-model:

Panel data
**********

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
            from doubleml.datasets import make_did_SZ2020
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
            from doubleml.datasets import make_did_SZ2020
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            ml_g = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_leaf=5)
            ml_m = RandomForestClassifier(n_estimators=100, max_depth=5, min_samples_leaf=5)
            np.random.seed(42)
            data = make_did_SZ2020(n_obs=500, cross_sectional_data=True, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd', t_col='t')
            dml_did_obj = dml.DoubleMLDIDCS(obj_dml_data, ml_g, ml_m)
            print(dml_did_obj.fit())

.. _ssm-model:

Sample Selection Models (SSM)
++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/ssm.rst

.. _ssm-mar-model:

Missingness at Random
*********************

Consider the following two additional assumptions for the sample selection model:

- **Cond. Independence of Selection:** :math:`Y_i(d) \perp S_i|D_i=d, X_i\quad a.s.` for :math:`d=0,1`
- **Common Support:** :math:`P(D_i=1|X_i)>0` and :math:`P(S_i=1|D_i=d, X_i)>0` for :math:`d=0,1`

such that outcomes are missing at random (for the score see :ref:`Scores <ssm-mar-score>`).

``DoubleMLSSM`` implements sample selection models. The score ``score='missing-at-random'`` refers to the correponding score
relying on the assumptions above. The ``DoubleMLData`` object has to be defined with the additional argument ``s_col`` for the selection indicator.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            from sklearn.linear_model import LassoCV, LogisticRegressionCV
            from doubleml.datasets import make_ssm_data
            import doubleml as dml

            np.random.seed(42)
            n_obs = 2000
            df = make_ssm_data(n_obs=n_obs, mar=True, return_type='DataFrame')
            dml_data = dml.DoubleMLData(df, 'y', 'd', s_col='s')

            ml_g = LassoCV()
            ml_m = LogisticRegressionCV(penalty='l1', solver='liblinear')
            ml_pi = LogisticRegressionCV(penalty='l1', solver='liblinear')
            
            dml_ssm = dml.DoubleMLSSM(dml_data, ml_g, ml_m, ml_pi, score='missing-at-random')
            dml_ssm.fit()
            print(dml_ssm)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            library(DoubleML)
            library(mlr3)
            library(data.table)

            set.seed(3141)
            n_obs = 2000
            df = make_ssm_data(n_obs=n_obs, mar=TRUE, return_type="data.table")
            dml_data = DoubleMLData$new(df, y_col="y", d_cols="d", s_col="s")
            dml_ssm = DoubleMLSSM$new(dml_data, ml_g, ml_m, ml_pi, score="missing-at-random")
            dml_ssm$fit()
            print(dml_ssm)

.. _ssm-nr-model:

Nonignorable Nonresponse
************************

When sample selection or outcome attriction is realated to unobservables, identification generally requires an instrument for the selection indicator :math:`S_i`.
Consider the following additional assumptions for the instrumental variable:

- **Cond. Correlation:** :math:`\exists Z: \mathbb{E}[Z\cdot S|D,X] \neq 0`
- **Cond. Independence:** :math:`Y_i(d,z)=Y_i(d)` and :math:`Y_i \perp Z_i|D_i=d, X_i\quad a.s.` for :math:`d=0,1`

This requires the instrumental variable :math:`Z_i`, which must not affect :math:`Y_i` or be associated
with unobservables affecting :math:`Y_i` conditional on :math:`D_i` and :math:`X_i`. Further, the selection is determined via 
a (unknown) threshold model:

- **Threshold:** :math:`S_i = 1\{V_i \le \xi(D,X,Z)\}` where :math:`\xi` is a general function and :math:`V_i` is a scalar with strictly monotonic cumulative distribution function conditional on :math:`X_i`.
- **Cond. Independence:** :math:`Y_i \perp (Z_i, D_i)|X_i`.

Let :math:`\Pi_i := P(S_i=1|D_i, X_i, Z_i)` denote the selection probability.
Additionally, the following assumptions are required:

- **Common Support for Treatment:** :math:`P(D_i=1|X_i, \Pi)>0`
- **Cond. Effect Homogeneity:** :math:`\mathbb{E}[Y_i(1)-Y_i(0)|S_i=1, X_i=x, V_i=v] = \mathbb{E}[Y_i(1)-Y_i(0)|X_i=x, V_i=v]`
- **Common Support for Selection:** :math:`P(S_i=1|D_i=d, X_i=x, Z_i=z)>0\quad a.s.` for :math:`d=0,1`

For further details, see `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.

.. figure:: figures/py_ssm.svg
   :width: 400
   :alt: DAG
   :align: center

   Causal paths under nonignorable nonresponse
    

``DoubleMLSSM`` implements sample selection models. The score ``score='nonignorable'`` refers to the correponding score
relying on the assumptions above. The ``DoubleMLData`` object has to be defined with the additional argument ``s_col`` for the selection indicator
and ``z_cols`` for the instrument.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            from sklearn.linear_model import LassoCV, LogisticRegressionCV
            from doubleml.datasets import make_ssm_data
            import doubleml as dml

            np.random.seed(42)
            n_obs = 2000
            df = make_ssm_data(n_obs=n_obs, mar=False, return_type='DataFrame')
            dml_data = dml.DoubleMLData(df, 'y', 'd', z_cols='z', s_col='s')

            ml_g = LassoCV()
            ml_m = LogisticRegressionCV(penalty='l1', solver='liblinear')
            ml_pi = LogisticRegressionCV(penalty='l1', solver='liblinear')
            
            dml_ssm = dml.DoubleMLSSM(dml_data, ml_g, ml_m, ml_pi, score='nonignorable')
            dml_ssm.fit()
            print(dml_ssm)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            library(DoubleML)
            library(mlr3)
            library(data.table)

            set.seed(3141)
            n_obs = 2000
            df = make_ssm_data(n_obs=n_obs, mar=FALSE, return_type="data.table")
            dml_data = DoubleMLData$new(df, y_col="y", d_cols="d", z_cols = "z", s_col="s")
            dml_ssm = DoubleMLSSM$new(dml_data, ml_g, ml_m, ml_pi, score="nonignorable")
            dml_ssm$fit()
            print(dml_ssm)


Regression Discontinuity Designs (RDD)
++++++++++++++++++++++++++++++++++++++

.. include:: ../shared/models/rdd.rst
