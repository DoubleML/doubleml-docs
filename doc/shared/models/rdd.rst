**Regression Discontinuity Designs (RDD)** are causal inference methods used when treatment assignment is determined by a continuous running variable ("score") crossing a known threshold ("cutoff"). These designs exploit discontinuities in the probability of receiving treatment at the cutoff to estimate local treatment effects. RDDs are divided into two main types: **Sharp** and **Fuzzy**.

The key idea behind RDD is that units just above and just below the threshold are assumed to be comparable, differing only in the treatment assignment. This allows estimating the causal effect at the threshold by comparing outcomes of treated and untreated units.

Let :math:`S_i` represent the score, and let :math:`c` denote the cutoff point. Further, let :math:`Y_i(1)` and :math:`Y_i(0)` denote the potential outcomes with and without treatment, respectively.

The parameter of interest in an RDD is the **Local Average Treatment Effect (LATE)** at the cutoff:

.. math::

   \theta_{0} = \mathbb[Y(1)-Y(0)\mid S = c]

Our implementation follows work from `Noack, Olma and Rothe (2024) <https://arxiv.org/abs/2107.07942>`_, however, our notation is slightly different to be consistent with the package.

By using a set of additional covariates :math:`X_i` for each observation, :math:`Y_i` and :math:`D_i` can be adjusted in a first stage, to reduce the standard deviation in the estimation of :math:`\theta`.

Sharp Regression Discontinuity Design
*************************************

In a **Sharp RDD**, the treatment is deterministically assigned at the cutoff (:math:`D_i = \mathbb{1}\{S_i \geq c\}`).

The LATE is identified as the difference in the conditional expectation of :math:`Y_i` at the cutoff from both sides:

.. math::

   \theta_{0} = \mathbb[Y(1)-Y(0)\mid S = c]

The assumptions for identifying the LATE in a sharp RDD are:

- **Continuity:** The potential outcomes :math:`Y_i(1)` and :math:`Y_i(0)` are continuous around the cutoff, meaning no other factors besides treatment change discontinuously at the threshold.
  
- **Exogeneity of the Score:** Units cannot perfectly manipulate their value of :math:`S_i` to either receive or avoid treatment exactly at the cutoff.

Without the use of covariates, :math:`\theta` is typically estimated by running separate local linear regressions on each side of the cutoff, yielding an estimator of the form:

.. math::

   \hat{\theta}_{\text{base}}(h) = \sum_{i=1}^n w_i(h)Y_i,

where the :math:`w_i(h)` are local linear regression weights that depend on the data through the realizations of the running variable only and :math:`h > 0` is a bandwidth.

Under standard conditions, which include that the running variable is continuously distributed, and that the bandwidth :math:`h` tends to zero at an appropriate rate, the estimator :math:`\hat{\theta}_{\text{base}}(h)` is approximately normally distributed in large samples, with bias of order :math:`h^2` and variance of order :math:`(nh)^{-1}`:

.. math::
   \hat{\tau}_{\text{base}}(h) \stackrel{a}{\sim} N\left(\tau + h^2  B_{\text{base}},(nh)^{-1}V\right).

If covariates are available, they can be used to improve the accuracy of empirical RD estimates. The most popular strategy is to include them linearly and without kernel localization in the local linear regression. By simple least squares algebra, this "linear adjustment" estimator can be written as a no-covariates estimator with the covariate-adjusted outcome :math:`Y_i - Z_i^{\top} \widehat{\gamma}_h`, where :math:`\widehat{\gamma}_h` is a minimizer:

.. math::
   \widehat{\tau}_{\text{lin}}(h) = \sum w_i(h)\left(Y_i - X_i^{\top} \widehat{\gamma}_h\right).

If :math:`\mathbb{E}[X_i | S_i = s]` is twice continuously differentiable around the cutoff, then the distribution of :math:`\widehat{\tau}_{\text{lin}}(h)` is similar to the one of the base estimator with potentially smaller variance term.

As this linear adjustment might not exploit the available covariate information efficiently, DoubleML features an RDD estimator with flexible covariate adjustment based on potentially nonlinear adjustment functions :math:`\eta`. The estimator takes the following form:

.. math::
   \widehat{\theta}_{\text{RDFlex}}(h; \eta) = \sum w_i(h) M_i(\eta), \quad M_i(\eta) = Y_i - \eta(X_i).

Similar to other algorithms in DoubleML, :math:`\eta` is estimated by ML methods and with crossfitting. Different than in other models, there is no orthogonal score, we rather adjust the outcome variable by the influence of the covariates.

This reduces the variance in the estimation potentially even further to:

.. math::
   V(\eta) = \frac{\bar{\kappa}}{f_X(0)} \left( \mathbb{V}[M_i(\eta) | S_i = 0^+] + \mathbb{V}[M_i(\eta) | S_i = 0^-] \right).

with :math:`\bar{\kappa}` being a kernel constant. To maximize the precision of the estimator :math:`\wh\tau(h;\eta)` for any particular bandwidth :math:`h`, :math:`\eta` has to be chosen such that :math:`V(\eta)` is as small as possible. Usually, the equally-weighted average of the left and right limits of the conditional expectation function :math:`\mathbb{E}[Y_i|S_i=s,X_i=x]` at the cutoff achieves this goal. It can be shown:

.. math::
   V(\eta) \geq V(\eta_0) \text{ for all } \eta,

where:

.. math::
   \eta_0(x) = \frac{1}{2} \left( \mu_0^+(x) + \mu_0^-(x) \right), \quad \mu_0^\star(x) = \mathbb{E}[Y_i | S_i = 0^\star, X_i = x] \text{ for } \star \in \{+, -\}.

``RDFlex`` implements this regression discontinuity design with :math:`\eta_0` being estimated by user-specified ML methods. The indicator ``fuzzy=False`` indicates a sharp design. The ``DoubleMLData`` object has to be defined with the argument ``s_col`` for the score and ``x_cols`` for the covariates. ``y_col`` refers to the observed outcome, on which we want to estimate the effect at the cutoff and ``d_cols`` is an indicator of whether an observation is treated or not. In the sharp design, this should be identical to an indicator of whether an observation is left or right of the cutoff (:math:`D_i = \mathbb{I}[S_i > c]`).
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            from sklearn.linear_model import LassoCV
            from doubleml.rdd.datasets import make_simple_rdd_data
            import doubleml as dml

            np.random.seed(42)
            data_dict = make_simple_rdd_data(n_obs=1000, fuzzy=False)
            cov_names = ['x' + str(i) for i in range(data_dict['X'].shape[1])]
            df = pd.DataFrame(
               np.column_stack((data_dict['Y'], data_dict['D'], data_dict['score'], data_dict['X'])),
               columns=['y', 'd', 'score'] + cov_names,
            )
            
            dml_data = dml.DoubleMLData(df, y_col='y', d_cols='d', x_cols=cov_names, s_col='score')

            ml_g = LassoCV()

            rdflex_obj = RDFlex(dml_data, ml_g, fuzzy=False)
            rdflex_obj.fit()

            print(rdflex_obj)


Fuzzy Regression Discontinuity Design
*************************************

In a **Fuzzy RDD**, treatment assignment is identical to the sharp RDD (:math:`T_i = \mathbb{1}\{S_i \geq c\}`), however, compliance is limited around the cutoff which leads to a different treatment received than assigned (:math:`D_i \neq T_i`) for some units.

A treatment effect can be identified by comparing the jump in the probability of receiving treatment with the jump in the outcome. 

The parameter of interest in the Fuzzy RDD is the average treatment effect on the treated:

.. math::
   \theta_{0} = \mathbb[Y(1, 1)-Y(0, 0)\mid S = c, \{i\in \text{compliers}\}]

with :math:`Y_i(T_i, D_i(T_i))` being the potential outcome under the potential treatments. The assumptions for identifying the ATT in a fuzzy RDD are:

- **Continuity of Potential Outcomes:** Similar to sharp RDD, the potential outcomes :math:`Y_i(1)` and :math:`Y_i(0)` must be continuous at the cutoff.
  
- **Continuity of Treatment Assignment Probability:** The probability of receiving treatment :math:`\mathbb{E}[D_i | S_i]` must change discontinuously at the cutoff, but there should be no other jumps in the probability.

- **Monotonicity:** There must be no "defiers", meaning individuals for whom the treatment assignment goes in the opposite direction of the score.

Under similar considerations as in the sharp case, an estimator using flexible covariate adjustment can be derived as:

.. math::
   \hat{\theta}(h; \widehat{\eta}_Y, \widehat{\eta}_D) = \frac{\hat{\tau}_Y(h; \widehat{\eta}_Y)}{\hat{\tau}_D(h; \widehat{\eta}_D)} 
   = \frac{\sum w_{i}(h) (Y_i - \widehat{\eta}_{Y}(X_i))}{\sum w_{i}(h) (T_i - \widehat{\eta}_{D}(X_i))}.

``RDFlex`` implements this fuzzy RDD with flexible covariate adjustment. The indicator ``fuzzy=True`` indicates a fuzzy design. The ``DoubleMLData`` object has to be defined with the argument ``s_col`` for the score and ``x_cols`` for the covariates. ``y_col`` refers to the observed outcome, on which we want to estimate the effect at the cutoff and ``d_cols`` is an indicator of whether an observation is treated or not.
Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            from sklearn.linear_model import LassoCV, LogisticRegressionCV
            from doubleml.rdd.datasets import make_simple_rdd_data
            import doubleml as dml

            np.random.seed(42)
            data_dict = make_simple_rdd_data(n_obs=1000, fuzzy=True)
            cov_names = ['x' + str(i) for i in range(data_dict['X'].shape[1])]
            df = pd.DataFrame(
               np.column_stack((data_dict['Y'], data_dict['D'], data_dict['score'], data_dict['X'])),
               columns=['y', 'd', 'score'] + cov_names,
            )
            
            dml_data = dml.DoubleMLData(df, y_col='y', d_cols='d', x_cols=cov_names, s_col='score')

            ml_g = LassoCV()

            rdflex_obj = RDFlex(dml_data, ml_g, ml_m, fuzzy=True)
            rdflex_obj.fit()

            print(rdflex_obj)

Implementation Details
*************************************

There are some specialities in the ``RDFlex`` implementation, that differ from the rest of the package and thus deserve to be pointed out here.

#. **Bandwidth Selection**: The bandwidth is a crucial tuning paramter for RDD algorithms. By default, our implementation uses the ``rdbwselect`` method from the ``rdrobust`` library for an initial selection. This can be overwritten by the user using the parameter ``h_fs``. Since covariate adjustment and RDD fitting are iteracting, by default, we repeat the bandwidth selection and nuisance estimation once in the ``fit()`` method. This can be adjusted by ``n_iterations``. 
#. **Kernel Selection**: Another crucial decision when estimating with RDD is the kernel, that weights observations around the cutoff. For this, the parameters ``fs_kernel`` and ``kernel`` are important. The letter is a kwarg and is used in the RDD estimation, while the ``fs_kernel`` specifies the kernel used in the nuisance estimation. By default, both of them are ``triangular``.
#. **Local and Global Learners**: ``RDFlex`` estimates the nuisance functions locally around the cutoff. In certain scenarios, it can be desirable to rather perform a global fit on the full support of the score :math:`S`. For this, the ``Global Learners`` in ``doubleml.utils`` can be used.
#. **First Stage Specifications**: In nuisance estimation, we have to add variable(s) to add information about the location of the observation left or right of the cutoff. In the default case ``fs_specification="cutoff"``, this is an indicator whether the observation is left or right. If ``fs_specification="cutoff and score"``, additionally the score is added. In case of ``fs_specification="interacted cutoff and score"``, also an interaction term of the cutoff indicator and the score is added. 
#. **Intention-to-Treat Effects**: Above, we demonstrated how to estimate the ATT in a fuzzy RDD. To estimate an Intention-to-Treat effect instead, the parameter ``fuzzy=False`` can be selected. 
#. **Key-worded Arguments**: ``rdrobust`` as the underlying RDD library has additional paramters to tune the estimation. You can use ``**kwargs`` to add them via ``RDFlex``