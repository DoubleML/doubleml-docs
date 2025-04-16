As in the description of the :ref:`DiD model <did-pa-model>`, the required nuisance elements are

.. math::
    \begin{align}
    g_{0, \mathrm{g}, t_\text{pre}, t_\text{eval}, \delta}(X_i) &:= \mathbb{E}[Y_{i,t_\text{eval}} - Y_{i,t_\text{pre}}|X_i, C_{i,t_\text{eval} + \delta}^{(\cdot)} = 1], \\
    m_{0, \mathrm{g}, t_\text{eval} + \delta}(X_i) &:= P(G_i^{\mathrm{g}}=1|X_i, G_i^{\mathrm{g}} + C_{i,t_\text{eval} + \delta}^{(\cdot)}=1).
    \end{align}

for a certain choice of :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval})` and :math:`\delta` and control group :math:`C_{i,t_\text{eval} + \delta}^{(\cdot)}`.

For notational purposes, we will omit the subscripts :math:`\mathrm{g}, t_\text{pre}, t_\text{eval}, \delta` in the following and use the notation 

* :math:`g_0(0, X_i)\equiv g_{0, \mathrm{g}, t_\text{pre}, t_\text{eval}, \delta}(X_i)` (population outcome regression function of the control group)
* :math:`m_0(X_i)\equiv m_{0, \mathrm{g}, t_\text{eval} + \delta}(X_i)` (generalized propensity score)

All scores in the multi-period setting have the form 

.. math::

    \psi(W_i,\theta, \eta) := 
    \begin{cases}
    \tilde{\psi}(W_i,\theta, \eta) & \text{for } G_i^{\mathrm{g}} \vee C_{i,t_\text{eval} + \delta}^{(\cdot)}=1 \\
    0 & \text{otherwise}
    \end{cases}

i.e. the score is only non-zero for units in the corresponding treatment group :math:`\mathrm{g}` and control group :math:`C_{i,t_\text{eval} + \delta}^{(\cdot)}`.

For the difference-in-differences model implemented in ``DoubleMLDIDMulti`` one can choose between
``score='observational'`` and ``score='experimental'``.

``score='observational'`` implements the score function (dropping the unit index :math:`i`):

.. math::

    \tilde{\psi}(W,\theta, \eta) 
    :&= -\frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]}\theta + \left(\frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]} - \frac{\frac{m(X) (1-G^{\mathrm{g}})}{1-m(X)}}{\mathbb{E}_n\left[\frac{m(X) (1-G^{\mathrm{g}})}{1-m(X)}\right]}\right) \left(Y_{t_\text{eval}} - Y_{t_\text{pre}} - g(0,X)\right)

    &= \tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

where the components of the final linear score :math:`\psi` are

.. math::
    \psi_a(W; \eta) &=  \tilde{\psi}_a(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}),

    \psi_b(W; \eta) &= \tilde{\psi}_b(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

and the nuisance elements :math:`\eta=(g, m)`.

.. note::
    Remark that :math:`1-G^{\mathrm{g}}=C^{(\cdot)}` if :math:`G^{\mathrm{g}} \vee C_{t_\text{eval} + \delta}^{(\cdot)}=1`.

If ``in_sample_normalization='False'``, the score is set to

.. math::

    \tilde{\psi}(W,\theta,\eta) &= - \frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]}\theta + \frac{G^{\mathrm{g}} - m(X)}{\mathbb{E}_n[G^{\mathrm{g}}](1-m(X))}\left(Y_{t_\text{eval}} - Y_{t_\text{pre}} - g(0,X)\right)

    &= \tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

with :math:`\eta=(g, m)`.
Remark that this will result in the same score, but just uses slightly different normalization.

``score='experimental'`` assumes that the treatment probability is independent of the covariates :math:`X` and does not rely on the propensity score. Instead define
the population outcome regression for treated and control group as

* :math:`g_0(0, X_i)\equiv \mathbb{E}[Y_{i,t_\text{eval}} - Y_{i,t_\text{pre}}|X_i, C_{i,t_\text{eval} + \delta}^{(\cdot)} = 1]` (control group)
* :math:`g_0(1, X_i)\equiv \mathbb{E}[Y_{i,t_\text{eval}} - Y_{i,t_\text{pre}}|X_i, G_i^{\mathrm{g}} = 1]` (treated group)

``score='experimental'`` implements the score function:

.. math::

    \tilde{\psi}(W,\theta, \eta) 
    :=\; &-\theta + \left(\frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]} - \frac{1-G^{\mathrm{g}}}{\mathbb{E}_n[1-G^{\mathrm{g}}]}\right)\left(Y_{t_\text{eval}} - Y_{t_\text{pre}} - g(0,X)\right)

    &+ \left(1 - \frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]}\right) \left(g(1,X) - g(0,X)\right)

    =\; &\tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

where the components of the final linear score :math:`\psi` are

.. math::
    \psi_a(W; \eta) &=  \tilde{\psi}_a(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}),

    \psi_b(W; \eta) &= \tilde{\psi}_b(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

and the nuisance elements :math:`\eta=(g)`.

Analogously, if ``in_sample_normalization='False'``,  the score is set to

.. math::

    \tilde{\psi}(W,\theta, \eta) 
    :=\; &-\theta +  \frac{G^{\mathrm{g}} - \mathbb{E}_n[G^{\mathrm{g}}]}{\mathbb{E}_n[G^{\mathrm{g}}](1-\mathbb{E}_n[G^{\mathrm{g}}])}\left(Y_{t_\text{eval}} - Y_{t_\text{pre}} - g(0,X)\right)

    &+ \left(1 - \frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]}\right) \left(g(1,X) - g(0,X)\right)

    =\; &\tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

with :math:`\eta=(g)`.
Remark that this will result in the same score, but just uses slightly different normalization.
