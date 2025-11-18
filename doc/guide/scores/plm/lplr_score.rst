For the LPLR model implemented in ``DoubleMLLPLR`` one can choose between
``score='nuisance_space'`` and ``score='instrument'``. For the LPLR model let ``treatment=d`` and :math:`Y\in\{0,1\}`

``score='nuisance_space'`` implements the score function:

.. math::

    \psi(W, \beta, \eta) := \psi(X) \{Y e^{\beta D} -(1-Y)e^{r_0(X)} \} \{ D - m_0(X)\}

with :math:`\eta = { r(\cdot), m(\cdot), \psi(\cdot) }`, where

.. math::

    \r_0(X) = t_0(X) - \breve \beta a_0(X),

    m_0(X) = \mathbb{E} [D | X, Y=0],

    \psi(X) = \text{expit} (-r_0(X)).

For the estimation of :math:`r_0(X)`, we further need to obtain the following estimates as well as a preliminary estimate
:math:`\breve \beta` as described in `Liu et al. (2021) <https://academic.oup.com/ectj/article/24/3/559/6296639>`_

.. math::

    t_0(X) = \mathbb{E} [\text{logit} M (D, X) | X],

    a_0(X) = \mathbb{E} [D | X].



``score='instrument'`` implements the score function:

.. math::

    \psi(W; \beta, \eta) &:=  \mathbb E [ \{Y - \text{expit} (\beta_0 D + r_0(X )) \} Z_0 ]


with :math:`Z_0=D-m(X)` and :math:`\eta = { r(\cdot), m(\cdot), \psi(\cdot) }`, where

.. math::

    \r_0(X) = t_0(X) - \breve \beta a_0(X),

    m_0(X) = \mathbb{E} [D | X].

and :math:`r_0(X)` is computed as for ``score='nuisance_space'``.