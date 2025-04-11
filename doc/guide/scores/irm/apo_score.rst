For the average potential outcomes (APO) models implemented in ``DoubleMLAPO`` and ``DoubleMLAPOS``
the ``score='APO'`` is implemented. Furthermore, weights :math:`\omega(Y,D,X)` and

.. math::

    \bar{\omega}(X) = \mathbb{E}[\omega(Y,D,X)|X]

can be specified. For a given treatment level :math:`d` the general score function takes the form 

.. math::

    \psi(W; \theta, \eta) :=\; &\omega(Y,D,X) \cdot g(d,X) + \bar{\omega}(X)\cdot \frac{1\lbrace D = d\rbrace }{m(X)}(Y - g(d,X)) - \theta

    =& \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)`, where the true nuisance elements are 

.. math::

    g_0(D, X) &= \mathbb{E}[Y | D, X],

    m_{0,d}(X) &= \mathbb{E}[1\lbrace D = d\rbrace | X] = P(D=d|X).

The components of the linear score are

.. math::

    \psi_a(W; \eta) =&  - 1,

    \psi_b(W; \eta) =\; &\omega(Y,D,X) \cdot g(d,X) + \bar{\omega}(X)\cdot \frac{1\lbrace D = d\rbrace }{m(X)}(Y - g(d,X)).


If no weights are specified, the weights are set to

.. math::

    \omega(Y,D,X) &= 1

    \bar{\omega}(X) &= 1.
