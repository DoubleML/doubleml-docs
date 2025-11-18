The partially linear models (PLM) take the form

.. math::

    Y = D \theta_0 + g_0(X) + \zeta,

where treatment effects are additive with some sort of linear form.

.. _plr-model:

Partially linear regression model (PLR)
***************************************

.. include:: /guide/models/plm/plr.rst

.. include:: /shared/causal_graphs/plr_irm_causal_graph.rst

``DoubleMLPLR`` implements PLR models. Estimation is conducted via its ``fit()`` method. 

.. note::
    Remark that the standard approach with ``score='partialling out'`` does not rely on a direct estimate of :math:`g_0(X)`,
    but :math:`\ell_0(X) := \mathbb{E}[Y \mid X] = \theta_0 \mathbb{E}[D \mid X] + g(X)`.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.plm.datasets import make_plr_CCDDHNR2018
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

.. include:: /guide/models/plm/pliv.rst

.. include:: /shared/causal_graphs/pliv_iivm_causal_graph.rst

``DoubleMLPLIV`` implements PLIV models.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            import doubleml as dml
            from doubleml.plm.datasets import make_pliv_CHS2015
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

Logistic partially linear regression model (LPLR)
*************************************************

.. include:: /guide/models/plm/lplr.rst

.. include:: /shared/causal_graphs/plr_irm_causal_graph.rst

``DoubleMLLPLR`` implements LPLR models. Estimation is conducted via its ``fit()`` method.

.. note::
    Remark that the treatment effects are not additive in this model. The partial linear term enters the model through a logistic link function.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            import doubleml as dml
            from doubleml.plm.datasets import make_lplr_LZZ2020
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
            from sklearn.base import clone
            np.random.seed(3141)
            ml_t = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_m = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_M = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            obj_dml_data = make_lplr_LZZ2020(alpha=0.5, n_obs=500, dim_x=20)
            dml_lplr_obj = dml.DoubleMLPLR(obj_dml_data, ml_M, ml_t, ml_m)
            dml_lplr_obj.fit().summary



