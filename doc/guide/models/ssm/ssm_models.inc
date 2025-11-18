.. include:: /guide/models/ssm/ssm.rst

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
            from doubleml.irm.datasets import make_ssm_data
            import doubleml as dml

            np.random.seed(42)
            n_obs = 2000
            df = make_ssm_data(n_obs=n_obs, mar=True, return_type='DataFrame')
            dml_data = dml.DoubleMLSSMData(df, 'y', 'd', s_col='s')

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

            ml_g = lrn("regr.cv_glmnet", nfolds = 5, s = "lambda.min")
            ml_m = lrn("classif.cv_glmnet", nfolds = 5, s = "lambda.min")
            ml_pi = lrn("classif.cv_glmnet", nfolds = 5, s = "lambda.min")
            
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
- **Cond. Independence:** :math:`V_i \perp (Z_i, D_i)|X_i`.

Let :math:`\Pi_i := P(S_i=1|D_i, X_i, Z_i)` denote the selection probability.
Additionally, the following assumptions are required:

- **Common Support for Treatment:** :math:`P(D_i=1|X_i, \Pi)>0`
- **Cond. Effect Homogeneity:** :math:`\mathbb{E}[Y_i(1)-Y_i(0)|S_i=1, X_i=x, V_i=v] = \mathbb{E}[Y_i(1)-Y_i(0)|X_i=x, V_i=v]`
- **Common Support for Selection:** :math:`P(S_i=1|D_i=d, X_i=x, Z_i=z)>0\quad a.s.` for :math:`d=0,1`

For further details, see `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.

.. figure:: /guide/figures/py_ssm.svg
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
            from doubleml.irm.datasets import make_ssm_data
            import doubleml as dml

            np.random.seed(42)
            n_obs = 2000
            df = make_ssm_data(n_obs=n_obs, mar=False, return_type='DataFrame')
            dml_data = dml.DoubleMLSSMData(df, 'y', 'd', z_cols='z', s_col='s')

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
            
            ml_g = lrn("regr.cv_glmnet", nfolds = 5, s = "lambda.min")
            ml_m = lrn("classif.cv_glmnet", nfolds = 5, s = "lambda.min")
            ml_pi = lrn("classif.cv_glmnet", nfolds = 5, s = "lambda.min")
            
            dml_ssm = DoubleMLSSM$new(dml_data, ml_g, ml_m, ml_pi, score="nonignorable")
            dml_ssm$fit()
            print(dml_ssm)