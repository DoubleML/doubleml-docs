For ``DoubleMLPQ`` the only valid option is ``score='PQ'``. For ``treatment=d`` with :math:`d\in\{0,1\}` and
a quantile :math:`\tau\in (0,1)` this implements the nonlinear score function:

.. math::

    \psi(W; \theta, \eta) := g_{d}(X, \tilde{\theta}) + \frac{1\{D=d\}}{m(X)}(1\{Y\le \theta\} - g_d(X, \tilde{\theta})) - \tau


where :math:`\eta=(g_d,m)` with true values

.. math::

    g_{d,0}(X, \theta_0) &= \mathbb{E}[1\{Y\le \theta_0\}|X, D=d]

    m_0(X) &= P(D=d|X).

Remark that :math:`g_{d,0}(X,\theta_0)` depends on the target parameter :math:`\theta_0`, such that
the score is estimated with a preliminary estimate :math:`\tilde{\theta}`. For further details, see `Kallus et al. (2019) <https://arxiv.org/abs/1912.12945>`_. 
