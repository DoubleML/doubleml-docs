For the IIVM model implemented in ``DoubleMLIIVM``
we employ for ``score='LATE'`` the score function:

``score='LATE'`` implements the score function:

.. math::

    \psi(W; \theta, \eta) :=\; &g(1,X) - g(0,X)
    + \frac{Z (Y - g(1,X))}{m(X)} - \frac{(1 - Z)(Y - g(0,X))}{1 - m(X)}

    &- \bigg(r(1,X) - r(0,X) + \frac{Z (D - r(1,X))}{m(X)} - \frac{(1 - Z)(D - r(0,X))}{1 - m(X)} \bigg) \theta

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, r)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - \bigg(r(1,X) - r(0,X) + \frac{Z (D - r(1,X))}{m(X)} - \frac{(1 - Z)(D - r(0,X))}{1 - m(X)} \bigg),

    \psi_b(W; \eta) &= g(1,X) - g(0,X) + \frac{Z (Y - g(1,X))}{m(X)} - \frac{(1 - Z)(Y - g(0,X))}{1 - m(X)}.
