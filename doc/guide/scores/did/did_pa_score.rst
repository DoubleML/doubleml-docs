For the difference-in-differences model implemented in ``DoubleMLDIDMulti`` one can choose between
``score='observational'`` and ``score='experimental'``.

``score='observational'`` implements the score function (dropping the unit index :math:`i`):

.. math::

    \psi(W,\theta, \eta) 
    :&= -\frac{D}{\mathbb{E}_n[D]}\theta + \left(\frac{D}{\mathbb{E}_n[D]} - \frac{\frac{m(X) (1-D)}{1-m(X)}}{\mathbb{E}_n\left[\frac{m(X) (1-D)}{1-m(X)}\right]}\right) \left(Y_1 - Y_0 - g(0,X)\right)

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) &=  - \frac{D}{\mathbb{E}_n[D]},

    \psi_b(W; \eta) &= \left(\frac{D}{\mathbb{E}_n[D]} - \frac{\frac{m(X) (1-D)}{1-m(X)}}{\mathbb{E}_n\left[\frac{m(X) (1-D)}{1-m(X)}\right]}\right) \left(Y_1 - Y_0 - g(0,X)\right)

and the nuisance elements :math:`\eta=(g, m)` are defined as

.. math::

    g_{0}(0, X) &= \mathbb{E}[Y_1 - Y_0|D=0, X]

    m_0(X) &= P(D=1|X).

If ``in_sample_normalization='False'``, the score is set to

.. math::

    \psi(W,\theta,\eta) &= - \frac{D}{p}\theta + \frac{D - m(X)}{p(1-m(X))}\left(Y_1 - Y_0 -g(0,X)\right)

    &= \psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, p)`, where :math:`p_0 = \mathbb{E}[D]` is estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.

``score='experimental'`` assumes that the treatment probability is independent of the covariates :math:`X` and
implements the score function:

.. math::

    \psi(W,\theta, \eta) 
    :=\; &-\theta + \left(\frac{D}{\mathbb{E}_n[D]} - \frac{1-D}{\mathbb{E}_n[1-D]}\right)\left(Y_1 - Y_0 -g(0,X)\right)

    &+ \left(1 - \frac{D}{\mathbb{E}_n[D]}\right) \left(g(1,X) - g(0,X)\right)

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) \;=  &- 1,

    \psi_b(W; \eta) \;= &\left(\frac{D}{\mathbb{E}_n[D]} - \frac{1-D}{\mathbb{E}_n[1-D]}\right)\left(Y_1 - Y_0 -g(0,X)\right)

    &+  \left(1 - \frac{D}{\mathbb{E}_n[D]}\right) \left(g(1,X) - g(0,X)\right)

and the nuisance elements :math:`\eta=(g)` are defined as

.. math::

    g_{0}(0, X) &= \mathbb{E}[Y_1 - Y_0|D=0, X]

    g_{0}(1, X) &= \mathbb{E}[Y_1 - Y_0|D=1, X]

Analogously, if ``in_sample_normalization='False'``,  the score is set to

.. math::

    \psi(W,\theta, \eta) 
    :=\; &-\theta +  \frac{D - p}{p(1-p)}\left(Y_1 - Y_0 -g(0,X)\right)

    &+ \left(1 - \frac{D}{p}\right) \left(g(1,X) - g(0,X)\right)

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, p)`, where :math:`p_0 = \mathbb{E}[D]` is estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.
