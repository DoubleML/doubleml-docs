.. _resampling:

Sample-splitting, cross-fitting and repeated cross-fitting
----------------------------------------------------------

Sample-splitting and the application of cross-fitting is a central part of double/debiased machine learning (DML).
For all DML models
``DoubleMLPLR``,
``DoubleMLPLIV``,
``DoubleMLIRM``,
and ``DoubleMLIIVM``,
the specification is done via the parameters ``n_folds`` and ``n_rep``.
Advanced resampling techniques can be obtained via the boolean parameters
``draw_sample_splitting`` and ``apply_cross_fitting`` as well as the methods
``draw_sample_splitting()`` and ``set_sample_splitting()``.

As an example we consider a partially linear regression model (PLR)
implemented in ``DoubleMLPLR``.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            import numpy as np
            from doubleml.plm.datasets import make_plr_CCDDHNR2018
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.base import clone

            learner = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_l = clone(learner)
            ml_m = clone(learner)
            np.random.seed(1234)
            obj_dml_data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=100)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            library(DoubleML)
            library(mlr3)
            lgr::get_logger("mlr3")$set_threshold("warn")
            library(mlr3learners)
            library(data.table)

            learner = lrn("regr.ranger", num.trees = 100, mtry = 20, min.node.size = 2, max.depth = 5)
            ml_l = learner
            ml_m = learner
            data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=100, return_type = "data.table")
            obj_dml_data = DoubleMLData$new(data,
                                            y_col = "y",
                                            d_cols = "d")

.. _k-fold-cross-fitting:

Cross-fitting with *K* folds
++++++++++++++++++++++++++++++++++

The default setting is ``n_folds = 5`` and ``n_rep = 1``, i.e.,
:math:`K=5` folds and no repeated cross-fitting.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m, n_folds = 5, n_rep = 1)
            print(dml_plr_obj.n_folds)
            print(dml_plr_obj.n_rep)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, n_folds = 5, n_rep = 1)
            print(dml_plr_obj$n_folds)
            print(dml_plr_obj$n_rep)

During the initialization of a DML model like ``DoubleMLPLR`` a :math:`K`-fold random
partition :math:`(I_k)_{k=1}^{K}` of observation indices is generated.
The :math:`K`-fold random partition is stored in the ``smpls`` attribute of the DML model object.

.. TODO: add more detailed describtion of the ``smpls`` list. Or refer to the attribute description.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj.smpls)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj$smpls

For each :math:`k \in [K] = \lbrace 1, \ldots, K]` the nuisance ML estimator

.. math::

    \hat{\eta}_{0,k} = \hat{\eta}_{0,k}\big((W_i)_{i\not\in I_k}\big)

is based on the observations of all other :math:`k-1` folds.
The values of the two score function components
:math:`\psi_a(W_i; \hat{\eta}_0)` and :math:`\psi_b(W_i; \hat{\eta}_0))`
for each observation index :math:`i \in I_k` are computed and
stored in the attributes ``psi_a`` and ``psi_b``.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            dml_plr_obj.fit();
            print(dml_plr_obj.psi_elements['psi_a'][:5])
            print(dml_plr_obj.psi_elements['psi_b'][:5])

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj$fit()
            print(dml_plr_obj$psi_a[1:5, ,1])
            print(dml_plr_obj$psi_b[1:5, ,1])

.. _repeated-cross-fitting:

Repeated cross-fitting with *K* folds and *M* repetitions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Repeated cross-fitting is obtained by choosing a value :math:`M>1` for the number of repetition ``n_rep``.
It results in :math:`M` random :math:`K`-fold partitions being drawn.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m, n_folds = 5, n_rep = 10)
            print(dml_plr_obj.n_folds)
            print(dml_plr_obj.n_rep)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, n_folds = 5, n_rep = 10)
            print(dml_plr_obj$n_folds)
            print(dml_plr_obj$n_rep)

For each of the :math:`M` partitions, the nuisance ML models are estimated and score functions computed as described
in :ref:`k-fold-cross-fitting`.
The resulting values of the score functions are stored in 3-dimensional arrays ``psi_a`` and ``psi_b``, where the
row index corresponds the observation index :math:`i \in [N] = \lbrace 1, \ldots, N\rbrace`
and the column index to the partition :math:`m \in [M] = \lbrace 1, \ldots, M\rbrace`.
The third dimension refers to the treatment variable and becomes non-singleton in case of multiple treatment variables.

.. TODO: decide whether we always place hints with regards to the multiple treatment case or whether we always refer to the case of one treatment variable and the multiple treatment case is handled in one section of the documentation which is solely discussing the multiple treatment case.
.. Note that in case of multiple treatment variables the score functions are 3-dimensional arrays where the third dimension
.. refers to the different treatment variables.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            dml_plr_obj.fit();
            print(dml_plr_obj.psi_elements['psi_a'][:5, :, 0])
            print(dml_plr_obj.psi_elements['psi_b'][:5, :, 0])

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj$fit()
            print(dml_plr_obj$psi_a[1:5, ,1])
            print(dml_plr_obj$psi_b[1:5, ,1])

We estimate the causal parameter :math:`\tilde{\theta}_{0,m}` for each of the :math:`M` partitions with a DML
algorithm as described in :ref:`algorithms`.
Standard errors are obtained as described in :ref:`se_confint`.
The aggregation of the estimates of the causal parameter and its standard errors is done using the median

.. math::
    \tilde{\theta}_{0} = \text{Median}\big((\tilde{\theta}_{0,m})_{m \in [M]}\big).
The estimate of the causal parameter :math:`\tilde{\theta}_{0}` is stored in the ``coef`` attribute
and the asymptotic standard error :math:`\hat{\sigma}/\sqrt{N}` in ``se``.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        In python, the confidence intervals and p-values are based on the :py:class:`doubleml.DoubleMLFramework` object.
        This class provides methods such as ``confint``, ``bootstrap`` or ``p_adjust``. For different repetitions, 
        the computations are done separately and combined via the median (based on Chernozhukov et al., 2018).

        The estimate of the asymptotic standard error :math:`\hat{\sigma}/\sqrt{N}` is then based on the median aggregated confidence intervals with crictial value :math:`1.96`, i.e.,

        .. math::

            \hat{\sigma}/\sqrt{N} = (\text{Median}\big((\tilde{\theta}_{0,m} + 1.96\cdot \tilde{\sigma}_{m}/\sqrt{N})_{m \in [M]}\big) - \text{Median}\big((\tilde{\theta}_{0,m})_{m \in [M]}\big)) / 1.96.

        Remark that methods such as methods such as ``confint``, ``bootstrap`` or ``p_adjust`` do not use the estimate of the standard error.

        .. ipython:: python

            print(dml_plr_obj.coef)
            print(dml_plr_obj.se)

    .. tab-item:: R
        :sync: r

        The aggregation of the standard errors is done using the median

        .. math::

            \hat{\sigma} = \sqrt{\text{Median}\big((\hat{\sigma}_m^2 + (\tilde{\theta}_{0,m} - \tilde{\theta}_{0})^2)_{m \in [M]}\big)}.

        .. jupyter-execute::

            print(dml_plr_obj$coef)
            print(dml_plr_obj$se)

The parameter estimates :math:`(\tilde{\theta}_{0,m})_{m \in [M]}` and asymptotic standard errors
:math:`(\hat{\sigma}_m/\sqrt{N})_{m \in [M]}` for each of the :math:`M` partitions are stored in the attributes
``_all_coef`` and ``_all_se``, respectively.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            print(dml_plr_obj._all_coef)
            print(dml_plr_obj._all_se)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            print(dml_plr_obj$all_coef)
            print(dml_plr_obj$all_se)



Externally provide a sample splitting / partition
+++++++++++++++++++++++++++++++++++++++++++++++++

All DML models allow a partition to be provided externally via the method ``set_sample_splitting()``.
In Python we can for example use the K-Folds cross-validator of sklearn :py:class:`~sklearn.model_selection.KFold` in
order to generate a sample splitting and provide it to the DML model object.
Note that by setting ``draw_sample_splitting = False`` one can prevent that a partition is drawn during initialization
of the DML model object.
The following calls are equivalent.
In the first sample code, we use the standard interface and draw the sample-splitting with :math:`K=4` folds during
initialization of the ``DoubleMLPLR`` object.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            np.random.seed(314)
            dml_plr_obj_internal = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m, n_folds = 4)
            print(dml_plr_obj_internal.fit().summary)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            set.seed(314)
            dml_plr_obj_internal = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, n_folds = 4)
            dml_plr_obj_internal$fit()
            dml_plr_obj_internal$summary()

In the second sample code, we use the K-Folds cross-validator of sklearn :py:class:`~sklearn.model_selection.KFold`
and set the partition via the ``set_sample_splitting()`` method.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            dml_plr_obj_external = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m, draw_sample_splitting = False)

            from sklearn.model_selection import KFold
            np.random.seed(314)
            kf = KFold(n_splits=4, shuffle=True)
            smpls = [(train, test) for train, test in kf.split(obj_dml_data.x)]

            dml_plr_obj_external.set_sample_splitting(smpls);
            print(dml_plr_obj_external.fit().summary)

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj_external = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m, draw_sample_splitting = FALSE)

            set.seed(314)
            # set up a task and cross-validation resampling scheme in mlr3
            my_task = Task$new("help task", "regr", data)
            my_sampling = rsmp("cv", folds = 4)$instantiate(my_task)

            train_ids = lapply(1:4, function(x) my_sampling$train_set(x))
            test_ids = lapply(1:4, function(x) my_sampling$test_set(x))
            smpls = list(list(train_ids = train_ids, test_ids = test_ids))

            dml_plr_obj_external$set_sample_splitting(smpls)
            dml_plr_obj_external$fit()
            dml_plr_obj_external$summary()

Sample-splitting without cross-fitting
++++++++++++++++++++++++++++++++++++++

The boolean flag ``apply_cross_fitting`` allows to estimate DML models without applying cross-fitting.
It results in randomly splitting the sample into two parts.
The first half of the data is used for the estimation of the nuisance ML models and the second half for estimating the
causal parameter.
Note that cross-fitting performs well empirically and is recommended to remove bias induced by overfitting, see also
:ref:`bias_overfitting`.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. note:: 
            The flag ``apply_cross_fitting`` is deprecated for the python package. To avoid cross-fitting, please use the option
            to set :ref:`external predictions <ext_pred>`.

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_obj_external = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m,
                                                n_folds = 2, apply_cross_fitting = FALSE)
            dml_plr_obj_external$fit()
            dml_plr_obj_external$summary()

        Note, that in order to split data unevenly into train and test sets the interface to externally set the sample splitting
        via ``set_sample_splitting()`` needs to be applied, like for example:

        .. jupyter-execute::

            dml_plr_obj_external = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m,
                                                    n_folds = 2, apply_cross_fitting = FALSE,
                                                    draw_sample_splitting = FALSE)

            set.seed(314)
            # set up a task and cross-validation resampling scheme in mlr3
            my_task = Task$new("help task", "regr", data)
            my_sampling = rsmp("holdout", ratio = 0.8)$instantiate(my_task)

            train_ids = list(my_sampling$train_set(1))
            test_ids = list(my_sampling$test_set(1))
            smpls = list(list(train_ids = train_ids, test_ids = test_ids))

            dml_plr_obj_external$set_sample_splitting(smpls)
            dml_plr_obj_external$fit()
            dml_plr_obj_external$summary()


Estimate DML models without sample-splitting
++++++++++++++++++++++++++++++++++++++++++++

The implementation of the DML models allows the estimation without sample splitting, i.e., all observations are used
for learning the nuisance models as well as for the estimation of the causal parameter.
Note that this approach usually results in a bias and is therefore not recommended without appropriate theoretical
justification, see also :ref:`bias_overfitting`.


.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. note:: 
            The flag ``apply_cross_fitting`` is deprecated for the python package. To avoid cross-fitting, please use the option
            to set :ref:`external predictions <ext_pred>`. Additionally, the number of folds ``n_folds`` is expected to be at least ``2``.

    .. tab-item:: R
        :sync: r

        .. jupyter-execute::

            dml_plr_no_split = DoubleMLPLR$new(obj_dml_data, ml_l, ml_m,
                                            n_folds = 1, apply_cross_fitting = FALSE)

            set.seed(314)
            dml_plr_no_split$fit()
            dml_plr_no_split$summary()


References
++++++++++

* Chernozhukov, Victor and Demirer, Mert and Duflo, Esther and Fernández-Val, Iván (2018), Generic Machine Learning Inference on Heterogeneous Treatment Effects in Randomized Experiments, with an Application to Immunization in India, National Bureau of Economic Research,  `doi: 10.3386/w24678 <https://dx.doi.org/10.3386/w24678>`_.
