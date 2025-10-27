**Logistic partially linear regression (LPLR)** models take the form

.. math::

    \mathbb{E} [Y | D, X] = \mathbb{P} (Y=1 | D, X) = \text{expit} \{\beta_0 D + r_0 (X) \}

where :math:`Y` is the binary outcome variable and :math:`D` is the policy variable of interest.
The high-dimensional vector :math:`X = (X_1, \ldots, X_p)` consists of other confounding covariates.
:math:`\text{expit}` is the logistic link function

.. math::
    \text{expit} ( X ) = \frac{1}{1 + e^{-x}}

