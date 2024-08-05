For ``DoubleMLLPQ`` the only valid option is ``score='LPQ'``. For ``treatment=d`` with :math:`d\in\{0,1\}`, instrument :math:`Z` and
a quantile :math:`\tau\in (0,1)` this implements the nonlinear score function:

.. math::

    \psi(W; \theta, \eta) :=& \Big(g_{d, Z=1}(X, \tilde{\theta}) - g_{d, Z=0}(X, \tilde{\theta}) + \frac{Z}{m(X)}(1\{D=d\} \cdot 1\{Y\le \theta\} - g_{d, Z=1}(X, \tilde{\theta}))

    &\quad - \frac{1-Z}{1-m(X)}(1\{D=d\} \cdot 1\{Y\le \theta\} - g_{d, Z=0}(X, \tilde{\theta}))\Big) \cdot \frac{2d -1}{\gamma} - \tau


where :math:`\eta=(g_{d,Z=1}, g_{d,Z=0}, m, \gamma)` with true values

.. math::

    g_{d,Z=z,0}(X, \theta_0) &= \mathbb{E}[1\{D=d\} \cdot 1\{Y\le \theta_0\}|X, Z=z],\quad z\in\{0,1\}

    m_{Z=z,0}(X) &= P(D=d|X, Z=z),\quad z\in\{0,1\}

    m_0(X) &= P(Z=1|X)

    \gamma_0 &= \mathbb{E}[P(D=d|X, Z=1) - P(D=d|X, Z=0)].

Further, the compliance probability :math:`\gamma_0` is estimated with the two additional nuisance components 

.. math::

    m_{Z=z,0}(X) = P(D=d|X, Z=z),\quad z\in\{0,1\}.

Remark that :math:`g_{d,Z=z,0}(X, \theta_0)` depends on the target parameter :math:`\theta_0`, such that
the score is estimated with a preliminary estimate :math:`\tilde{\theta}`. For further details, see `Kallus et al. (2019) <https://arxiv.org/abs/1912.12945>`_.
