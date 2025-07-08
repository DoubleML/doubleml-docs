As in the description of the :ref:`DiD model <did-cs-model>`, the required nuisance elements are

.. math::
    \begin{align}
    g^{\text{treat}}_{0,\mathrm{g}, t, \text{eval} + \delta}(X_i) &:= \mathbb{E}[Y_{i,t} |X_i, G_i^{\mathrm{g}}=1, T_i=t], \\
    g^{\text{control}}_{0,\mathrm{g}, t, \text{eval} + \delta}(X_i) &:= \mathbb{E}[Y_{i,t} |X_i, C_{i,t_\text{eval} + \delta}^{(\cdot)}=1, T_i=t], \\
    m_{0, \mathrm{g}, t_\text{eval} + \delta}(X_i) &:= P(G_i^{\mathrm{g}}=1|X_i, G_i^{\mathrm{g}} + C_{i,t_\text{eval} + \delta}^{(\cdot)}=1).
    \end{align}

for :math:`t\in\{t_\text{pre}, t_\text{eval}\}` and a certain choice of :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval})` and :math:`\delta` and control group :math:`C_{i,t_\text{eval} + \delta}^{(\cdot)}`.

For notational purposes, we will omit the subscripts :math:`\mathrm{g}, t_\text{pre}, t_\text{eval}, \delta` in the following and use the notation 

* :math:`g_0(1, 0, X_i) \equiv g^{\text{treat}}_{0,\mathrm{g}, t_\text{pre}, \text{eval} + \delta}(X_i)` (pop. outcome regr. function for treatment group in :math:`t_\text{pre}`)
* :math:`g_0(1, 1, X_i) \equiv g^{\text{treat}}_{0,\mathrm{g}, t_\text{eval}, \text{eval} + \delta}(X_i)` (pop. outcome regr. function for treatment group in :math:`t_\text{eval}`)
* :math:`g_0(0, 0, X_i) \equiv g^{\text{control}}_{0,\mathrm{g}, t_\text{pre}, \text{eval} + \delta}(X_i)` (pop. outcome regr. function for control group in :math:`t_\text{pre}`)
* :math:`g_0(0, 1, X_i) \equiv g^{\text{control}}_{0,\mathrm{g}, t_\text{eval}, \text{eval} + \delta}(X_i)` (pop. outcome regr. function for control group in :math:`t_\text{eval}`)
* :math:`m_0(X_i)\equiv m_{0, \mathrm{g}, t_\text{eval} + \delta}(X_i)` (generalized propensity score).

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

    \tilde{\psi}(W,\theta,\eta) :=\; & - \frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]}\theta + \frac{G^{\mathrm{g}}}{\mathbb{E}_n[G^{\mathrm{g}}]}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{G^{\mathrm{g}}T}{\mathbb{E}_n[G^{\mathrm{g}}T]} (Y - g(1,1,X)) 

    & - \frac{G^{\mathrm{g}}(1-T)}{\mathbb{E}_n[G^{\mathrm{g}}(1-T)]}(Y - g(1,0,X))

    & - \frac{m(X) (1-G^{\mathrm{g}})T}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-G^{\mathrm{g}})T}{1-m(X)}\right]^{-1} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-G^{\mathrm{g}})(1-T)}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-G^{\mathrm{g}})(1-T)}{1-m(X)}\right]^{-1} (Y-g(0,0,X))

    =\; &\tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

where the components of the final linear score :math:`\psi` are

.. math::
    \psi_a(W; \eta) &=  \tilde{\psi}_a(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}),

    \psi_b(W; \eta) &= \tilde{\psi}_b(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

and the nuisance elements :math:`\eta=(g, m)`.

.. note::
    Remark that :math:`1-G^{\mathrm{g}}=C^{(\cdot)}` if :math:`G^{\mathrm{g}} \vee C_{t_\text{eval} + \delta}^{(\cdot)}=1`.

If ``in_sample_normalization='False'``, the score is set to

.. math::

    \tilde{\psi}(W,\theta,\eta) :=\; & - \frac{G^{\mathrm{g}}}{p}\theta + \frac{G^{\mathrm{g}}}{p}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{G^{\mathrm{g}}T}{p\lambda} (Y - g(1,1,X)) 

    & - \frac{G^{\mathrm{g}}(1-T)}{p(1-\lambda)}(Y - g(1,0,X))

    & - \frac{m(X) (1-G^{\mathrm{g}})T}{p(1-m(X))\lambda} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-G^{\mathrm{g}})(1-T)}{p(1-m(X))(1-\lambda)} (Y-g(0,0,X))

    =\; &\tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

with :math:`\eta=(g, m, p, \lambda)`, where :math:`p_0 = \mathbb{E}[G^{\mathrm{g}}]` and :math:`\lambda_0 = \mathbb{E}[T]` are estimated on the subsample.
Remark that this will result a similar score, but just uses slightly different normalization.

``score='experimental'`` assumes that the treatment probability is independent of the covariates :math:`X` and
implements the score function:

.. math::

    \tilde{\psi}(W,\theta,\eta) :=\; & - \theta + \Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{G^{\mathrm{g}}T}{\mathbb{E}_n[G^{\mathrm{g}}T]} (Y - g(1,1,X)) 

    & - \frac{G^{\mathrm{g}}(1-T)}{\mathbb{E}_n[G^{\mathrm{g}}(1-T)]}(Y - g(1,0,X))

    & - \frac{(1-G^{\mathrm{g}})T}{\mathbb{E}_n[(1-G^{\mathrm{g}})T]} (Y-g(0,1,X)) 

    & + \frac{(1-G^{\mathrm{g}})(1-T)}{\mathbb{E}_n[(1-G^{\mathrm{g}})(1-T)]} (Y-g(0,0,X))

    =\; &\tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

where the components of the final linear score :math:`\psi` are

.. math::
    \psi_a(W; \eta) &=  \tilde{\psi}_a(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}),

    \psi_b(W; \eta) &= \tilde{\psi}_b(W; \eta) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

and the nuisance elements :math:`\eta=(g, m)`.

Analogously, if ``in_sample_normalization='False'``,  the score is set to

.. math::

    \tilde{\psi}(W,\theta,\eta) :=\; & - \theta + \Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{G^{\mathrm{g}}T}{p\lambda} (Y - g(1,1,X)) 

    & - \frac{G^{\mathrm{g}}(1-T)}{p(1-\lambda)}(Y - g(1,0,X))

    & - \frac{(1-G^{\mathrm{g}})T}{(1-p)\lambda} (Y-g(0,1,X)) 

    & + \frac{(1-G^{\mathrm{g}})(1-T)}{(1-p)(1-\lambda)} (Y-g(0,0,X))

    =\; &\tilde{\psi}_a(W; \eta) \theta + \tilde{\psi}_b(W; \eta)

with :math:`\eta=(g, m, p, \lambda)`, where :math:`p_0 = \mathbb{E}[G^{\mathrm{g}}]` and :math:`\lambda_0 = \mathbb{E}[T]` are estimated on the subsample.
Remark that this will result in a similar score, but just uses slightly different normalization.