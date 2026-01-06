**Partially linear panel regression (PLPR)** models by `Clarke and Polselli (2025) <https://doi.org/10.1093/ectj/utaf011>` take the form

.. math::

    Y_{it} = \theta_0 D_{it} + g_0(X_{it}) + \alpha_i + U_{it}, & &\mathbb{E}(U_{it} | D_{it}, X_{it}, \alpha_i) = 0,

    D_{it} = m_0(X_{it}) + \gamma_i + V_{it}, & &\mathbb{E}(V_{it} | X_{it}, \gamma_i) = 0,

where :math:`Y_{it}` is the outcome variable and :math:`D_{it}` is the policy variable of interest.
The high-dimensional vector :math:`X_{it} = (X_{it,1}, \ldots, X_{it,p})` consists of other confounding covariates. 
:math:`\alpha_i` and :math:`\gamma_i` represent unobserved individual heterogeneity terms, correlated with the covariates
and :math:`U_{it}` and :math:`V_{it}` are stochastic errors.