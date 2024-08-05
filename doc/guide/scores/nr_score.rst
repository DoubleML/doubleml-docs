For ``DoubleMLSSM`` the ``score='nonignorable'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) := \tilde{\psi}_1(W; \eta) - \tilde{\psi}_0(W; \eta) - \theta

where

.. math::

    \tilde{\psi}_1(W; \eta) &= \frac{D \cdot S \cdot [Y - g(1,1,X,\Pi)]}{m(X, \Pi) \cdot \pi(1,X,Z)} + g(1,1,X,\Pi)

    \tilde{\psi}_0(W; \eta) &= \frac{(1-D) \cdot S \cdot [Y - g(0,1,X,\Pi)]}{(1-m(X,\Pi)) \cdot \pi(0,X,Z)} + g(0,1,X,\Pi)

for :math:`d\in\{0,1\}` and :math:`\eta=(g, m, \pi, \Pi)` with true values

.. math::

    \pi_0(d, X, Z) &= P(S=1|D=d, X, Z)

    \Pi_0 &:= \pi_0(D, Z, X) = P(S=1|D,X,Z)
    
    g_0(d,s,X) &= \mathbb{E}[Y|D=d, S=s, X, \Pi_0]

    m_0(X, \Pi_0) &= P(D=1|X, \Pi_0).

The estimate of :math:`\Pi_0` is constructed via a preliminary estimate of :math:`\pi_0(D,X,Z)` via nested cross-fitting.

For further details, see `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.
