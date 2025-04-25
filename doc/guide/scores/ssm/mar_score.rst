For ``DoubleMLSSM`` the ``score='missing-at-random'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) := \tilde{\psi}_1(W; \eta) - \tilde{\psi}_0(W; \eta) - \theta

where

.. math::

    \tilde{\psi}_1(W; \eta) &= \frac{D \cdot S \cdot [Y - g(1,1,X)]}{m(X) \cdot \pi(1, X)} + g(1,1,X)

    \tilde{\psi}_0(W; \eta) &= \frac{(1-D) \cdot S \cdot [Y - g(0,1,X)]}{(1-m(X)) \cdot \pi(0, X)} + g(0,1,X)

for :math:`d\in\{0,1\}` and :math:`\eta=(g, m, \pi)` with true values

.. math::

    g_0(d,s,X) &= \mathbb{E}[Y|D=d, S=s, X]

    m_0(X) &= P(D=1|X)

    \pi_0(d, X) &= P(S=1|D=d, X).


For further details, see `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.
