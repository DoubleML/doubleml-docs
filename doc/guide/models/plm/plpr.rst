Suppose a panel study observes each of :math:`N` individuals over :math:`T` time periods (or waves).
For each individual :math:`i=1,\dots,N` and each period :math:`t=1,\dots,T`, the data consists of the
triple :math:`(Y_it, D_it, X_it)`. Let :math:`\{(Y_it, D_it, X_it) : t = 1, \dots , T\}_{i=1}^N`
denote :math:`N` independent and identically distributed (iid) random vectors, where each vector
corresponds to individual :math:`i` observed across all T waves.

.. note::
    The notation and identifying assumptions are based on `Clarke and Polselli (2025) <https://doi.org/10.1093/ectj/utaf011>`_, with some small adjustments to better fit into the general package documentation conventions, sometimes slightly abusing notation.
    See also the R package `xtdml <https://github.com/POLSEAN/XTDML>`_ implementation and corresponding reference `Polselli (2025) <https://arxiv.org/abs/2512.15965>`_ for further details. 

**Partially linear panel regression (PLPR)** models `(Clarke and Polselli, 2025) <https://doi.org/10.1093/ectj/utaf011>`_ take the form

.. math::

    Y_{it} = \theta_0 D_{it} + g_1(X_{it}) + \alpha_i^* + U_{it}, & &\mathbb{E}(U_{it} | D_{it}, X_{it}, \alpha_i^*) = 0,

    D_{it} = m_1(X_{it}) + \gamma_i + V_{it}, & &\mathbb{E}(V_{it} | X_{it}, \gamma_i) = 0,

where :math:`Y_{it}` is the outcome variable and :math:`D_{it}` is the policy variable of interest.
Further note that :math:`\mathbb{E}[\alpha_i^* | D_{it}, X_{it}] \neq 0`. The high-dimensional
vector :math:`X_{it} = (X_{it,1}, \ldots, X_{it,p})` consists of other confounding covariates. 
:math:`\alpha_i^*` and :math:`\gamma_i` represent unobserved individual heterogeneity terms,
correlated with the covariates. :math:`U_{it}` and :math:`V_{it}` are stochastic errors.

Alternatively one can write the *partialling-out* PLPR model as

.. math::

    Y_{it} = \theta_0 V_{it} + \ell_1(X_{it}) + \alpha_i + U_{it},

    V_{it} = D_{it} - m_1(X_{it}) - \gamma_i,

where :math:`\alpha_i` is a fixed effect. 

To account for the presence of unobserved heterogeneity, `Clarke and Polselli (2025) <https://doi.org/10.1093/ectj/utaf011>`_
use different panel data approaches, under the following assumptions.

Define potential outcomes :math:`Y_{it}(d)` for individual :math:`i` at wave :math:`t`, where realizations are
linked to the observed outcome by the consistency assumption :math:`Y_{it}(d_{it}) = Y_{it}`. 

:math:`\xi_i` represent time-invariant heterogeneity terms influencing outcome and treatment.
Further, define :math:`L_{t-1}(W_i) = \{W_{i1}, \dots, W_{it-1}\}` as lags of a random variable :math:`W_{it}`
at wave :math:`t`.

Assumptions `(Clarke and Polselli, 2025) <https://doi.org/10.1093/ectj/utaf011>`_:

- **No feedback to predictors**
    :math:`X_{it} \perp L_{t-1} (Y_i, D_i) | L_{t-1} (X_i), \xi_i`

- **Static panel**
    :math:`Y_{it}, D_{it} \perp L_{t-1} (Y_i, X_i, D_i) | X_{it}, \xi_i`

- **Selection on observables and omitted time-invariant variables**
    :math:`Y_{it} (.) \perp D_{it} | X_{it}, \xi_i`

- **Homogeneity and linearity of the treatment effect**
    :math:`\mathbb{E} [Y_{it}(d) - Y_{it}(0) | X_{it}, \xi_i] = d \theta_0`

- **Additive Separability**
    :math:`\mathbb{E} [Y_{it}(0) | X_{it}, \xi_i] &= g_1(X_{it}) + \alpha^*_i, & &\alpha^*_i = \alpha^*(\xi_i)`,
    
    :math:`\mathbb{E} [D_{it} | X_{it}, \xi_i] &= m_1(X_{it}) + \gamma_i, & &\gamma_i = \gamma(\xi_i)`


**Correlated Random Effect (CRE) Approaches**

These approaches convert the fixed-effects model into a random-effects specification using the
Mundlak device `(Mundlak, 1978) <https://doi.org/10.2307/1913646>`_. 

Given the set of assumptions, the PLPR model under the CRE approaches take the form

.. math::

    Y_{it} = \theta_0 D_{it} + \tilde{g}_1 (X_{it}, \bar{X}_i) + a_i + U_{it},

    D_{it} = \tilde{m}_1(X_{it}, \bar{X}_i) + c_i + V_{it}.

For the *partialling-out* PLPR

.. math::

    Y_{it} = \theta_0 V_{it} + \tilde{\ell}_1(X_{it}, \bar{X}_i) + a_i + U_{it},

    V_{it} = D_{it} - \tilde{m}_1(X_{it}, \bar{X}_i) - c_i,

where :math:`a_i`, :math:`c_i` are random effects and covariate unit means
:math:`\bar{X}_i = T^{-1} \sum_{t=1}^{T} X_{it}`.

**Transformation Approaches**

These approaches remove individual heterogeneity from the model by transforming the data.
For some random variable :math:`W_{it}`, define the First-Difference (FD) transformation
:math:`Q(W_{it}) = W_{it} - W_{it-1}` (for :math:`t=2, \dots, T`), and the Within-Group (WG)
transformation :math:`Q(W_{it}) = X_{it} - \bar{X}_{i}`, where :math:`\bar{W}_{i} = T^{-1} \sum_{t=1}^T W_{it}`.

The PLPR model under the transformation approaches takes the form

.. math::

    Q(Y_{it}) = \theta_0 Q(D_{it}) + Q(g_1(X_{it})) + Q(U_{it}),

    Q(D_{it}) = Q(m_1(X_{it})) + Q(V_{it}).

For the *partialling-out* PLPR

.. math::

    Q(Y_{it}) = \theta_0 Q(V_{it}) + Q(\ell_1(X_{it})) + Q(U_{it}),

    Q(V_{it}) = Q(D_{it}) - Q(m_1(X_{it})).

These transformations remove the fixed effect terms, as :math:`Q(\alpha_i^*)=Q(\alpha_i)=Q(\gamma_i)=0`.

**Implementation**

``DoubleMLPLPR`` implements the estimation and requires :ref:`DoubleMLPanelData <dml_panel_data>` with parameter ``static_panel=True`` as input.
Unit identifier and time period columns are set with ``id_col`` and ``t_col`` in :ref:`DoubleMLPanelData <dml_panel_data>`.

The model described in `Clarke and Polselli (2025) <https://doi.org/10.1093/ectj/utaf011>`_ uses block-k-fold sample splitting, where the entire time series 
of the sampled unit is allocated to one fold to allow for possible serial correlation within each unit, which is often the case for panel data. Furthermore, 
cluster robust standard error are employed. ``DoubleMLPLPR`` implements both of these aspects by using ``id_col`` as the cluster variable internally, see the example notebook
`Python: Cluster Robust Double Machine Learning <https://docs.doubleml.org/stable/examples/py_double_ml_multiway_cluster.html>`_.

The ``DoubleMLPLPR`` model inlcudes four different estimation approaches. The first two are correlated random effects (CRE) variants, the latter
two are transformation approaches. This can be selected with the ``approach`` parameter.

``approach='cre_general'``:

- Learn :math:`\tilde{\ell}_1 (X_{it}, \bar{X}_i)` from :math:`\{ Y_{it}, X_{it}, \bar{X}_i : t=1,\dots, T \}_{i=1}^N`,

- First learn :math:`\tilde{m}_1(X_{it}, \bar{X}_i)` from :math:`\{ D_{it}, X_{it}, \bar{X}_i : t=1,\dots, T \}_{i=1}^N`, with predictions :math:`\hat{m}_{1,it} = \tilde{m}_1 (X_{it}, \bar{X}_i)`

    - Calculate :math:`\hat{\bar{m}}_i = T^{-1} \sum_{t=1}^T \hat{m}_{1,it}`,

    - Calculate final nuisance part as :math:`\hat{m}^*_1 (X_{it}, \bar{X}_i, \bar{D}_i) = \hat{m}_{1,it} + \bar{D}_i - \hat{\bar{m}}_i`, 

  where :math:`\hat{m}^*_1 (X_{it}, \bar{X}_i, \bar{D}_i) = \mathbb{E}[D_{it} | X_{it}, \bar{X}_i] + c_i`. 

- :math:`g_1` can be learnt iteratively from :math:`\{ Y_{it}, X_{it}, \bar{X}_i : t=1,\dots, T \}_{i=1}^N` using estimates for :math:`\tilde{\ell}_1, \tilde{m}_1`.

``approach='cre_normal'``

Under the assumption that the conditional distribution :math:`D_{i1}, \dots, D_{iT} | X_{i1}, \dots X_{iT}` is multivariate normal (see `Clarke and Polselli (2025) <https://doi.org/10.1093/ectj/utaf011>`_ for further details):

- Learn :math:`\tilde{\ell}_1 (X_{it}, \bar{X}_i)` from :math:`\{ Y_{it}, X_{it}, \bar{X}_i : t=1,\dots, T \}_{i=1}^N`,

- Learn :math:`m^*_{1}` from :math:`\{ D_{it}, X_{it}, \bar{X}_i, \bar{D}_i: t=1,\dots, T \}_{i=1}^N`,

- :math:`g_1` can be learnt iteratively from :math:`\{ Y_{it}, X_{it}, \bar{X}_i : t=1,\dots, T \}_{i=1}^N` using estimates for :math:`\tilde{\ell}_1, \tilde{m}_1`.

``approach='fd_exact'``

Consider First-Difference (FD) transformation :math:`Q(W_{it})= W_{it} - W_{it-1}`, under the assumptions from above,
`Clarke and Polselli (2025) <https://doi.org/10.1093/ectj/utaf011>`_ show that :math:`\mathbb{E}[Y_{it}-Y_{it-1} | X_{it-1},X_{it}] =\Delta \ell_1 (X_{it-1}, X_{it})` and
:math:`\mathbb{E}[D_{it}-D_{it-1} | X_{it-1},X_{it}] =\Delta m_1 (X_{it-1}, X_{it})`. Therefore, the transformed nuisance function can be learnt as

- Learn :math:`\Delta \ell_1 (X_{it-1}, X_{it})` from :math:`\{ Y_{it}-Y_{it-1}, X_{it-1}, X_{it} : t=2, \dots , T \}_{i=1}^N`,

- Learn :math:`\Delta m_1 (X_{it-1}, X_{it})` from :math:`\{ D_{it}-D_{it-1}, X_{it-1}, X_{it} : t=2, \dots , T \}_{i=1}^N`,

- :math:`\Delta g_1 (X_{it-1}, X_{it})` can be learnt iteratively from :math:`\{ Y_{it}-Y_{it-1}, X_{it-1}, X_{it} : t=2, \dots , T \}_{i=1}^N` using estimates for :math:`\Delta \ell_1, \Delta m_1`.

``approach='wg_approx'``

For the Within-Group (WG) transformation :math:`Q(W_{it})= W_{it} - \bar{W}_{i}`, where :math:`\bar{W}_{i} = T^{-1} \sum_{t=1}^T W_{it}`.
Approximating the model gives

.. math::
    \begin{align*}
    Q(Y_{it}) &\approx \theta_0 Q(D_{it}) + g_1 (Q(X_{it})) + Q(U_{it}), \\
    Q(D_{it}) &\approx m_1 (Q(X_{it})) + Q(V_{it}).
    \end{align*}

Similarly,

.. math::
    Q(Y_{it}) &\approx \theta_0 Q(V_{it}) + \ell_1 (Q(X_{it})) + Q(U_{it}).

- Learn :math:`\ell_1` from transformed data :math:`\{ Q(Y_{it}), Q(X_{it}) : t=1,\dots,T \}_{i=1}^N`,

- Learn :math:`m_1` from transformed data :math:`\{ Q(D_{it}), Q(X_{it}) : t=1,\dots,T \}_{i=1}^N`,

- :math:`g_1` can be learnt iteratively from :math:`\{ Q(Y_{it}), Q(X_{it}) : t=1,\dots,T \}_{i=1}^N`, using estimates for :math:`\ell_1, m_1`.
