For a detailed description of the scores and nuisance elements, see :ref:`did-cs-score`.

In the :ref:`did-cs-model` with ``score='observational'`` and ``in_sample_normalization=True`` the score function implies the following representations

.. math::

    m(W,g) &= \Big(\big(g(1,1,X) - g(1,0,X)\big) - \big(g(0,1,X) - g(0,0,X)\big)\Big) \frac{G^{\mathrm{g}}}{\mathbb{E}[G^{\mathrm{g}}]} \cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

    \alpha(W) &= \Bigg(\frac{G^{\mathrm{g}}T}{\mathbb{E}[G^{\mathrm{g}}T]} - \frac{G^{\mathrm{g}}(1-T)}{\mathbb{E}[G^{\mathrm{g}}(1-T)]}

    &\quad - \frac{m(X)(1-G^{\mathrm{g}})T}{1-m(X)}\mathbb{E}\left[\frac{m(X)(1-G^{\mathrm{g}})T}{1-m(X)}\right]^{-1}

    &\quad + \frac{m(X)(1-G^{\mathrm{g}})(1-T)}{1-m(X)}\mathbb{E}\left[\frac{m(X)(1-G^{\mathrm{g}})(1-T)}{1-m(X)}\right]^{-1} \Bigg) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

If instead ``in_sample_normalization=False``, the Riesz representer changes to 

.. math::

    \alpha(W) = \left(\frac{T}{\mathbb{E}[G^{\mathrm{g}}]\mathbb{E}[T]} + \frac{1-T}{\mathbb{E}[G^{\mathrm{g}}](1-\mathbb{E}[T])}\right)\left(G^{\mathrm{g}} - (1-G^{\mathrm{g}})\frac{m(X)}{1-m(X)}\right) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

For ``score='experimental'`` the score function implies the following representations

.. math::

    m(W,g) &= \big(g(1,1,X) - g(1,0,X)\big) - \big(g(0,1,X) - g(0,0,X)\big) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

    \alpha(W) &= \left(\frac{G^{\mathrm{g}}T}{\mathbb{E}[G^{\mathrm{g}}T]} - \frac{G^{\mathrm{g}}(1-T)}{\mathbb{E}[G^{\mathrm{g}}(1-T)]} - \frac{(1-G^{\mathrm{g}})T}{\mathbb{E}[(1-G^{\mathrm{g}})T]} + \frac{(1-G^{\mathrm{g}})(1-T)}{\mathbb{E}[(1-G^{\mathrm{g}})(1-T)]}\right) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

And again, if instead ``in_sample_normalization=False``, the Riesz representer changes to 

.. math::

    \alpha(W) = \left(\frac{G^{\mathrm{g}}T}{\mathbb{E}[G^{\mathrm{g}}]\mathbb{E}[T]} - \frac{G^{\mathrm{g}}(1-T)}{\mathbb{E}[G^{\mathrm{g}}](1-\mathbb{E}[T])} - \frac{(1-G^{\mathrm{g}})T}{(1-\mathbb{E}[G^{\mathrm{g}}])\mathbb{E}[T]} + \frac{(1-G^{\mathrm{g}})(1-T)}{(1-\mathbb{E}[G^{\mathrm{g}}])(1-\mathbb{E}[T])}\right) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

The ``nuisance_elements`` are then computed with plug-in versions according to the general :ref:`sensitivity_implementation`, but the scores :math:`\psi_{\sigma^2}` and :math:`\psi_{\nu^2}` are scaled according to the sample size of the subset, i.e. with scaling factor :math:`c=\frac{n_{\text{obs}}}{n_{\text{subset}}}`.

.. note::
    Remark that the elements are only non-zero for units in the corresponding treatment group :math:`\mathrm{g}` and control group :math:`C^{(\cdot)}`, as :math:`1-G^{\mathrm{g}}=C^{(\cdot)}` if :math:`\max(G^{\mathrm{g}}, C^{(\cdot)})=1`.