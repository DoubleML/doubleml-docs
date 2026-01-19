For the PLPR model implemented in ``DoubleMLPLPR`` one can choose between
``score='partialling out'`` and ``score='IV-type'``.

``score='partialling out'`` implements the score function:

For correlated random effect (cre) approaches ``approach='cre_general'`` and ``approach='cre_normal'``

.. math::

    \psi(W_{it}; \theta, \eta) &:= [Y_{it} - \tilde{\ell}(X_{it},\bar{X}_i) - \theta (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i)] [D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i]

    &= - (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i) (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i) \theta + (Y_{it} - \tilde{\ell}(X_{it},\bar{X}_i)) (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i)

    &= \psi_a(W_{it}; \eta) \theta + \psi_b(W_{it}; \eta)

with :math:`\eta=(\tilde{\ell},\tilde{m})`, where

.. math::

    \tilde{\ell}_0(X_{it},\bar{X}_i) &:= \mathbb{E}[Y_{it} \mid X_{it}, \bar{X}_i] = \theta_0\mathbb{E}[D_{it} \mid X_{it}, \bar{X}_i] + g(X_{it}, \bar{X}_i),

    \tilde{m}_0(X_{it},\bar{X}_i) + c_i &:= \mathbb{E}[D_{it} \mid X_{it}, \bar{X}_i].

The components of the linear score are

.. math::

    \psi_a(W_{it}; \eta) &= - (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i) (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i),

    \psi_b(_{it}W; \eta) &= (Y_{it} - \tilde{\ell}(X_{it},\bar{X}_i)) (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i).


For transformation approaches ``approach='fd_exact'`` and ``approach='wg_approx'``, where :math:`Q(W_{it})` indicates a transformated variable :math:`W_{it}`

.. math::

    \psi(Q(W_{it}); \theta, \eta) &:= [Q(Y_{it}) - Q(\ell(X_{it})) - \theta (Q(D_{it}) - Q(m(X_{it})))] [Q(D_{it}) - Q(m(X_{it}))]

    &= - (Q(D_{it}) - Q(m(X_{it}))) (Q(D_{it}) - Q(m(X_{it}))) \theta + (Q(Y_{it}) - Q(\ell(X_{it}))) (Q(D_{it}) - Q(m(X_{it})))

    &= \psi_a(Q(W_{it}); \eta) \theta + \psi_b(Q(W_{it}); \eta)

with :math:`\eta=(\ell,m)`, where

.. math::

    Q(\ell_0(X)) &:= \mathbb{E}[Q(Y_{it}) \mid Q(X_{it})] = \theta_0\mathbb{E}[Q(D_{it}) \mid Q(X_{it})] + Q(g(X_{it})),

    Q(m_0(X)) &:= \mathbb{E}[Q(D_{it}) \mid Q(X_{it})].

The components of the linear score are

.. math::

    \psi_a(Q(W_{it}); \eta) &=  - (Q(D_{it}) - Q(m(X_{it}))) (Q(D_{it}) - Q(m(X_{it}))),

    \psi_b(Q(W_{it}); \eta) &= Q(Y_{it}) - Q(\ell(X_{it})) (Q(D_{it}) - Q(m(X_{it}))).

``score='IV-type'`` implements the score function:

For correlated random effect (cre) approaches ``approach='cre_general'`` and ``approach='cre_normal'``

.. math::

    \psi(W_{it}; \theta, \eta) &:= [Y_{it} - D_{it} \theta - \tilde{g}(X_{it},\bar{X}_i)] [D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i]

    &= - D_{it} (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i) \theta + (Y_{it} - \tilde{g}(X_{it},\bar{X}_i)) (D_{it} - \tilde{m}(X_{it},\bar{X}_i) - c_i)

    &= \psi_a(W_{it}; \eta) \theta + \psi_b(W_{it}; \eta)

with :math:`\eta=(\tilde{g},\tilde{m})`, where

.. math::

    \tilde{g}_0(X_{it},\bar{X}_i) &:= \mathbb{E}[Y_{it} - D_{it} \theta_0 \mid X_{it},\bar{X}_i],

    \tilde{m}_0(X_{it},\bar{X}_i) + c_i &:= \mathbb{E}[D_{it} \mid X_{it}, \bar{X}_i].

The components of the linear score are

.. math::

    \psi_a(W_{it}; \eta) &=  - D_{it} (D_{it} - \tilde{m}(X_{it},\bar{X}_i)),

    \psi_b(W_{it}; \eta) &= (Y_{it} - \tilde{g}(X_{it},\bar{X}_i)) (D_{it} - \tilde{m}(X_{it},\bar{X}_i)).

For transformation scores ``approach='fd_exact'`` and ``approach='wg_approx'``, where :math:`Q(W_{it})` indicates a transformated variable :math:`W_{it}`

.. math::

    \psi(Q(W_{it}); \theta, \eta) &:= [Q(Y_{it}) - Q(D_{it}) \theta - Q(g(X_{it}))] [Q(D_{it}) - Q(m(X_{it}))]

    &= - Q(D_{it}) (Q(D_{it}) - Q(m(X_{it}))) \theta + (Q(Y_{it}) - Q(g(X_{it}))) (Q(D_{it}) - Q(m(X_{it})))

    &= \psi_a(Q(W_{it}); \eta) \theta + \psi_b(Q(W_{it}); \eta)

with :math:`\eta=(g,m)`, where

.. math::

    Q(g_0(X_{it})) &:= \mathbb{E}[Q(Y_{it}) - Q(D_{it}) \theta_0 \mid Q(X_{it})],

    Q(m_0(X_{it})) &:= \mathbb{E}[Q(D_{it}) \mid Q(X_{it})].

The components of the linear score are

.. math::

    \psi_a(Q(W_{it}); \eta) &= - Q(D_{it}) (Q(D_{it}) - Q(m(X_{it}))),

    \psi_b(Q(W_{it}); \eta) &= (Q(Y_{it}) - Q(g(X_{it}))) (Q(D_{it}) - Q(m(X_{it}))).