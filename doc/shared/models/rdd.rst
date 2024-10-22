**Regression Discontinuity Designs (RDD)** are causal inference methods used when treatment assignment is determined by a continuous running variable ("score") crossing a known threshold ("cutoff"). These designs exploit discontinuities in the probability of receiving treatment at the cutoff to estimate local treatment effects. RDDs are divided into two main types: **Sharp** and **Fuzzy**.

The key idea behind RDD is that units just above and just below the threshold are assumed to be comparable, differing only in the treatment assignment. This allows to estimate the causal effect at the threshold by comparing outcomes of treated and untreated units.

Let :math:`S_i` represent the score, and let :math:`c` denote the cutoff point. Further, let :math:`Y_i(1)` and :math:`Y_i(0)` denote the potential outcomes with and without treatment, respectively.

The parameter of interest in an RDD is the **Local Average Treatment Effect (LATE)** at the cutoff:

.. math::

   \theta_{0} = \mathbb[Y(1)-Y(0)\mid S = c]

Our implementation follows work from `Noack, Olma and Rothe (2024) <https://arxiv.org/abs/2107.07942>`_, however, our notation is slightly different to be consistent with the package.

By using a set of additional covariates :math:`X_i` for each observation, :math:`Y_i` and :math:`D_i` can be adjusted in a first stage, to reduce the standart deviation in estimation of $\theta$.

Sharp Regression Discontinuity Design
*************************************

In a **Sharp RDD**, the treatment is deterministically assigned at the cutoff (:math:`D_i = \mathbb{1}\{S_i \geq c\}`).

The LATE is identified as the difference in the conditional expectation of :math:`Y_i` at the cutoff from both sides:

.. math::

   \theta_{0} = \mathbb[Y(1)-Y(0)\mid S = c]

The assumptions for identifying the LATE in a sharp RDD are

- **Continuity:** The potential outcomes :math:`Y_i(1)` and :math:`Y_i(0)` are continuous around the cutoff, meaning no other factors besides treatment change discontinuously at the threshold.
  
- **Exogeneity of the Score:** Units cannot perfectly manipulate their value of :math:`S_i` to either receive or avoid treatment exactly at the cutoff.

Without the use of covariates, :math:`\theta` is typically estimated by running seperate local linear regressions on  each side of the cutoff, yielding an estimator of the form

.. math::

   \hat{\theta}_{\text{base}}(h) = \sum_{i=1}^n w_i(h)Y_i,

where the :math:`w_i(h)` are local linear regression weights that depend on the data through the realizations of the running variable only and :math:`h > 0` is a bandwidth.

Under standard conditions, which include that the running variable is continuously distributed, and that the bandwidth :math:`h` tends to zero at an appropriate rate, the estimator :math:`\hat{\theta}_{\text{base}}(h)` is approximately normally distributed in large samples, with bias of order :math:`h^2` and variance of order :math:`(nh)^{-1}`:

.. math::
   \hat{\tau}_{\text{base}}(h) \stackrel{a}{\sim} N\left(\tau + h^2  B_{\text{base}},(nh)^{-1}V_{\text{base}}\right).

If covariates are available, they can be used to improve the accuracy of empirical RD estimates. The most popular strategy is to include them linearly and without kernel localization in the local linear regression. By simple least squares algebra, this "linear adjustment" estimator can be written as a no-covariates estimator with the covariate-adjusted outcome :math:`Y_i - Z_i^{\top} \widehat{\gamma}_h`, where :math:`\widehat{\gamma}_h` is a minimizer:

.. math::
   \widehat{\tau}_{\text{lin}}(h) = \sum w_i(h)\left(Y_i - X_i^{\top} \widehat{\gamma}_h\right).

If :math:`\mathbb{E}[X_i | S_i = s]` is twice continuously differentiable around the cutoff, then the distribution of :math:`\widehat{\tau}_{\text{lin}}(h)` is similar to the one of the base estimator with potentially smaller variance termin.

As this linear adjustment might not exploit the available covariate information efficiently, DoubleML features an RDD estimator with flexible covariate adjustment based on potentially nonlinear adjustment functions :math:`\eta`. The estimator takes the following form:

.. math::
   \widehat{\theta}_{\text{RDFlex}}(h; \eta) = \sum w_i(h) M_i(\eta), \quad M_i(\eta) = Y_i - \eta(Z_i).

.. math::
   \widehat{\theta}_{\text{RDFlex}}(h; \eta) \stackrel{a}{\sim} N\left(\tau + h^2 B_{\text{base}}, (nh)^{-1} V(\alpha)\right).

.. math::
   V(\eta) \geq V(\eta_0) \text{ for all } \eta.




Fuzzy Regression Discontinuity Design
*************************************

In a **Fuzzy RDD**, treatment assignment is identical to the sharp RDD (:math:`T_i = \mathbb{1}\{S_i \geq c\}`), however, compliance is limited around the cutoff which leads to a different treatment received than assigned (:math:`D_i \neq T_i`) for some units.

The **LATE** is identified by comparing the jump in the probability of receiving treatment with the jump in the outcome. 

The parameter of interest in the Fuzzy RDD is the average treatment effect on the treated:

.. math::
   \theta_{0} = \mathbb[Y(1, 1)-Y(0, 0)\mid S = c, \{i\in \text{compliers}\}]

with :math:`Y_i(T_i, D_i(T_i))` being the potential outcome under the potential treatments. The assumptions for identifying the ATT in a fuzzy RDD are

- **Continuity of Potential Outcomes:** Similar to sharp RDD, the potential outcomes :math:`Y_i(1)` and :math:`Y_i(0)` must be continuous at the cutoff.
  
- **Continuity of Treatment Assignment Probability:** The probability of receiving treatment :math:`\mathbb{E}[D_i | S_i]` must change discontinuously at the cutoff, but there should be no other jumps in the probability.

- **Monotonicity:** There must be no "defiers", meaning individuals for whom the treatment assignment goes in the opposite direction of the score.

