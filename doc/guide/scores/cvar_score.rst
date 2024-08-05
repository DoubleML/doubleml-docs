For ``DoubleMLCVAR`` the only valid option is ``score='CVaR'``. For ``treatment=d`` with :math:`d\in\{0,1\}` and
a quantile :math:`\tau\in (0,1)` this implements the score function:

.. math::

    \psi(W; \theta, \eta) := g_{d}(X, \gamma) + \frac{1\{D=d\}}{m(X)}(\max(\gamma, (1 - \tau)^{-1}(Y - \tau \gamma))  - g_d(X, \gamma)) - \theta

where :math:`\eta=(g_d,m,\gamma)` with true values

.. math::

    g_{d,0}(X, \gamma_0) &= \mathbb{E}[\max(\gamma_0, (1 - \tau)^{-1}(Y - \tau \gamma_0))|X, D=d]

    m_0(X) &= P(D=d|X)

and :math:`\gamma_0` being the potential quantile of :math:`Y(d)`. As for potential quantiles, the estimate :math:`g_d` is constructed via
a preliminary estimate of :math:`\gamma_0`. For further details, see `Kallus et al. (2019) <https://arxiv.org/abs/1912.12945>`_.
