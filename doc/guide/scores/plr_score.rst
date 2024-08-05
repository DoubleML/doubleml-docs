For the PLR model implemented in ``DoubleMLPLR`` one can choose between
``score='partialling out'`` and ``score='IV-type'``.

``score='partialling out'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - \ell(X) - \theta (D - m(X))] [D - m(X)]

    &= - (D - m(X)) (D - m(X)) \theta + (Y - \ell(X)) (D - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(\ell,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - (D - m(X)) (D - m(X)),

    \psi_b(W; \eta) &= (Y - \ell(X)) (D - m(X)).

``score='IV-type'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - D \theta - g(X)] [D - m(X)]

    &= - D (D - m(X)) \theta + (Y - g(X)) (D - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - D (D - m(X)),

    \psi_b(W; \eta) &= (Y - g(X)) (D - m(X)).