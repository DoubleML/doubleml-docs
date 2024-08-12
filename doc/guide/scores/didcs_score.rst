For the difference-in-differences model implemented in ``DoubleMLDIDCS`` one can choose between
``score='observational'`` and ``score='experimental'``.

``score='observational'`` implements the score function (dropping the unit index :math:`i`):

.. math::

    \psi(W,\theta,\eta) :=\; & - \frac{D}{\mathbb{E}_n[D]}\theta + \frac{D}{\mathbb{E}_n[D]}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{m(X) (1-D)T}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)T}{1-m(X)}\right]^{-1} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-D)(1-T)}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)(1-T)}{1-m(X)}\right]^{-1} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) =\; &- \frac{D}{\mathbb{E}_n[D]},

    \psi_b(W; \eta) =\; &\frac{D}{\mathbb{E}_n[D]}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{m(X) (1-D)T}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)T}{1-m(X)}\right]^{-1} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-D)(1-T)}{1-m(X)} \mathbb{E}_n\left[\frac{m(X) (1-D)(1-T)}{1-m(X)}\right]^{-1} (Y-g(0,0,X))

and the nuisance elements :math:`\eta=(g)` are defined as

.. math::

    g_{0}(d, t, X) = \mathbb{E}[Y|D=d, T=t, X].

If ``in_sample_normalization='False'``, the score is set to

.. math::

    \psi(W,\theta,\eta) :=\; & - \frac{D}{p}\theta + \frac{D}{p}\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{p\lambda} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{p(1-\lambda)}(Y - g(1,0,X))

    & - \frac{m(X) (1-D)T}{p(1-m(X))\lambda} (Y-g(0,1,X)) 

    & + \frac{m(X) (1-D)(1-T)}{p(1-m(X))(1-\lambda)} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, p, \lambda)`, where :math:`p_0 = \mathbb{E}[D]` and :math:`\lambda_0 = \mathbb{E}[T]` are estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.

``score='experimental'`` assumes that the treatment probability is independent of the covariates :math:`X` and
implements the score function:

.. math::

    \psi(W,\theta,\eta) :=\; & - \theta + \Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{(1-D)T}{\mathbb{E}_n[(1-D)T]} (Y-g(0,1,X)) 

    & + \frac{(1-D)(1-T)}{\mathbb{E}_n[(1-D)(1-T)]} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

where the components of the linear score are

.. math::

    \psi_a(W; \eta) \;=  &- 1,

    \psi_b(W; \eta) \;= &\Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{\mathbb{E}_n[DT]} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{\mathbb{E}_n[D(1-T)]}(Y - g(1,0,X))

    & - \frac{(1-D)T}{\mathbb{E}_n[(1-D)T]} (Y-g(0,1,X)) 

    & + \frac{(1-D)(1-T)}{\mathbb{E}_n[(1-D)(1-T)]} (Y-g(0,0,X))

and the nuisance elements :math:`\eta=(g, m)` are defined as

.. math::

    g_{0}(d, t, X) &= \mathbb{E}[Y|D=d, T=t, X]

    m_0(X) &= P(D=1|X).

Analogously, if ``in_sample_normalization='False'``,  the score is set to

.. math::

    \psi(W,\theta,\eta) :=\; & - \theta + \Big(g(1,1,X) - g(1,0,X) - (g(0,1,X) - g(0,0,X))\Big)

    & + \frac{DT}{p\lambda} (Y - g(1,1,X)) 

    & - \frac{D(1-T)}{p(1-\lambda)}(Y - g(1,0,X))

    & - \frac{(1-D)T}{(1-p)\lambda} (Y-g(0,1,X)) 

    & + \frac{(1-D)(1-T)}{(1-p)(1-\lambda)} (Y-g(0,0,X))

    =\; &\psi_a(W; \eta) \theta + \psi_b(W; \eta)

with :math:`\eta=(g, m, p, \lambda)`, where :math:`p_0 = \mathbb{E}[D]` and :math:`\lambda_0 = \mathbb{E}[T]` are estimated on the cross-fitting folds.
Remark that this will result in the same score, but just uses slightly different normalization.
