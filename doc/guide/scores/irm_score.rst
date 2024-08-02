For the IRM model implemented in ``DoubleMLIRM`` one can choose between
``score='ATE'`` and ``score='ATTE'``. Furthermore, weights :math:`\omega(Y,D,X)` and 

.. math::

    \bar{\omega}(X) = \mathbb{E}[\omega(Y,D,X)|X]

can be specified. The general score function takes the form 

.. math::

    \psi(W; \theta, \eta) :=\; &\omega(Y,D,X) \cdot (g(1,X) - g(0,X)) 
    
    & + \bar{\omega}(X)\cdot \bigg(\frac{D (Y - g(1,X))}{m(X)} - \frac{(1 - D)(Y - g(0,X))}{1 - m(X)}\bigg) - \theta

    =& \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g,m)` and where the components of the linear score are

.. math::

    \psi_a(W; \eta) =&  - 1,

    \psi_b(W; \eta) =\; &\omega(Y,D,X) \cdot (g(1,X) - g(0,X))
    
    & + \bar{\omega}(X)\cdot \bigg(\frac{D (Y - g(1,X))}{m(X)} - \frac{(1 - D)(Y - g(0,X))}{1 - m(X)}\bigg).

If no weights are specified, ``score='ATE'`` sets the weights

.. math::

    \omega(Y,D,X) &= 1

    \bar{\omega}(X) &= 1

whereas ``score='ATTE'`` changes weights to:

.. math::

    \omega(Y,D,X) &= \frac{D}{\mathbb{E}_n[D]}
    
    \omega(Y,D,X) &= \frac{m(X)}{\mathbb{E}_n[D]}.

For more details on other weight specifications, see :ref:`weighted_cates`.
