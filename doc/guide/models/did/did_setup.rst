**Difference-in-Differences Models (DID)** implemented in the package focus on the the binary treatment case with staggered adoption.

.. note::
    The notation and identifying assumptions are based on `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_, but adjusted to better fit into the general package documentation conventions, sometimes slightly abusing notation.
    The underlying score functions are based on `Sant'Anna and Zhao (2020) <https://doi.org/10.1016/j.jeconom.2020.06.003>`_, `Zimmert (2018) <https://arxiv.org/abs/1809.01643>`_ and `Chang (2020) <https://doi.org/10.1093/ectj/utaa001>`_.
    For a more detailed introduction and recent developments of the difference-in-differences literature see e.g. `Roth et al. (2022) <https://arxiv.org/abs/2201.01194>`_.

We consider :math:`n` observed units at time periods :math:`t=1,\dots, \mathcal{T}`.
The treatment status for unit :math:`i` at time period :math:`t` is denoted by the binary variable :math:`D_{i,t}=1`. The package considers the staggered adoption setting,
where a unit stays treated after it has been treated once (*Irreversibility of Treatment*).

Let :math:`G^{\mathrm{g}}_i` be an indicator variable that takes value one if unit :math:`i` is treated at time period :math:`t=\mathrm{g}`, :math:`G^{\mathrm{g}}_i=1\{G_i=\mathrm{g}\}` with :math:`G_i` refering to the first post-treatment period.
I units are never exposed to the treatment, define :math:`G_i=\infty`.

The target parameters are defined in terms of differences in potential outcomes. The observed and potential outcome for each unit :math:`i` at time period :math:`t` are assumed to be of the form

.. math::
    Y_{i,t} = Y_{i,t}(0) + \sum_{\mathrm{g}=2}^{\mathcal{T}} (Y_{i,t}(\mathrm{g}) - Y_{i,t}(0)) \cdot G^{\mathrm{g}}_i,

such that we observe one consistent potential outcome for each unit at each time period.

The corresponding target parameters are the average causal effects of the treatment 

.. math::
    ATT(\mathrm{g},t):= \mathbb{E}[Y_{i,t}(\mathrm{g}) - Y_{i,t}(0)|G^{\mathrm{g}}_i=1].

This target parameter quantifies the average change in potential outcomes for units that are treated the first time in period :math:`\mathrm{g}` with the difference in outcome being evaluated for time period :math:`t`.
The corresponding control groups, defined by an indicator :math:`C`, can be typically set as either the *never treated* or *not yet treated* units.
Let

.. math::
    \begin{align}
    C_{i,t}^{(nev)} \equiv C_{i}^{(nev)} &:= 1\{G_i=\infty\} \quad \text{(never treated)}, \\
    C_{i,t}^{(nyt)} &:= 1\{G_i > t\} \quad \text{(not yet treated)}.
    \end{align}

The corresponding identifying assumptions are:

1. **Irreversibility of Treatment:** 
    :math:`D_{i,1} = 0 \quad a.s.`
    For all :math:`t=2,\dots,\mathcal{T}`, :math:`D_{i,t-1} = 1` implies :math:`D_{i,t} = 1 \quad a.s.`

2. **Panel Data (Random Sampling):** 
    :math:`(Y_{i,1},\dots, Y_{i,\mathcal{T}}, X_i, D_{i,1}, \dots, D_{i,\mathcal{T}})_{i=1}^n` is independent and identically distributed.

3. **Limited Treatment Anticipation:**
    There is a known :math:`\delta\ge 0` such that
    :math:`\mathbb{E}[Y_{i,t}(\mathrm{g})|X_i, G_i^{\mathrm{g}}=1] = \mathbb{E}[Y_{i,t}(0)|X_i, G_i^{\mathrm{g}}=1]\quad a.s.` for all :math:`\mathrm{g}\in\mathcal{G}, t\in\{1,\dots,\mathcal{T}\}` such that :math:`t< \mathrm{g}-\delta`.

4. **Conditional Parallel Trends:** 
    Let :math:`\delta` be defined as in Assumption 3.\\
    For each :math:`\mathrm{g}\in\mathcal{G}` and :math:`t\in\{2,\dots,\mathcal{T}\}` such that :math:`t\ge \mathrm{g}-\delta`:

    a. **Never Treated:**
        :math:`\mathbb{E}[Y_{i,t}(0) - Y_{i,t-1}(0)|X_i, G_i^{\mathrm{g}}=1] = \mathbb{E}[Y_{i,t}(0) - Y_{i,t-1}(0)|X_i,C_{i}^{(nev)}=1] \quad a.s.`

    b. **Not Yet Treated:**
        :math:`\mathbb{E}[Y_{i,t}(0) - Y_{i,t-1}(0)|X_i, G_i^{\mathrm{g}}=1] = \mathbb{E}[Y_{i,t}(0) - Y_{i,t-1}(0)|X_i,C_{i,t+\delta}^{(nyt)}=1] \quad a.s.`

5. **Overlap:** 
    For each time period :math:`t=2,\dots,\mathcal{T}` and :math:`\mathrm{g}\in\mathcal{G}` there exists a :math:`\epsilon > 0` such that
    :math:`P(G_i^{\mathrm{g}}=1) > \epsilon` and :math:`P(G_i^{\mathrm{g}}=1|X_i, G_i^{\mathrm{g}} + C_{i,t}^{(nyt)}=1) < 1-\epsilon\quad a.s.`

.. note:: 
    For a detailed discussion of the assumptions see `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_.

Under the assumptions above (either Assumption 4.a or 4.b), the target parameter :math:`ATT(\mathrm{g},t)` is identified see Theorem 1. `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_.