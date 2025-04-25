For the PLIV model implemented in ``DoubleMLPLIV`` one can choose between
``score='IV-type'`` and ``score='partialling out'``.

``score='partialling out'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - \ell(X) - \theta (D - r(X))] [Z - m(X)]

    &= - (D - r(X)) (Z - m(X)) \theta + (Y - \ell(X)) (Z - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(\ell, m, r)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - (D - r(X)) (Z - m(X)),

    \psi_b(W; \eta) &= (Y - \ell(X)) (Z - m(X)).

``score='IV-type'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) &:= [Y - D \theta - g(X)] [Z - m(X)]

    &= - D (Z - m(X)) \theta + (Y - g(X)) (Z - m(X))

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - D (Z - m(X)),

    \psi_b(W; \eta) &= (Y - g(X)) (Z - m(X)).