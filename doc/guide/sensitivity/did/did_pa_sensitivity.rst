For a detailed description of the scores and nuisance elements, see :ref:`did-pa-score`.

In the :ref:`did-pa-model` with ``score='observational'`` and ``in_sample_normalization=True`` the score function implies the following representations

.. math::

    m(W,g) &= \big(g(1,X) - g(0,X)\big)\cdot \frac{G^{\mathrm{g}}}{\mathbb{E}[G^{\mathrm{g}}]}

    \alpha(W) &= \left(\frac{G^{\mathrm{g}}}{\mathbb{E}[G^{\mathrm{g}}]} - \frac{\frac{m(X)(1-G^{\mathrm{g}})}{1-m(X)}}{\mathbb{E}\left[\frac{m(X)(1-G^{\mathrm{g}})}{1-m(X)}\right]}\right) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

If instead ``in_sample_normalization=False``, the Riesz representer changes to 

.. math::

    \alpha(W) = \left(\frac{G^{\mathrm{g}}}{\mathbb{E}[G^{\mathrm{g}}]} - \frac{m(X)(1-G^{\mathrm{g}})}{\mathbb{E}[G^{\mathrm{g}}](1-m(X))}\right) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

For ``score='experimental'`` implies the score function implies the following representations

.. math::

    m(W,g) &= \big(g(1,X) - g(0,X)\big)\cdot \max(G^{\mathrm{g}}, C^{(\cdot)})

    \alpha(W) &= \left(\frac{G^{\mathrm{g}}}{\mathbb{E}[G^{\mathrm{g}}]} - \frac{1-G^{\mathrm{g}}}{1-\mathbb{E}[G^{\mathrm{g}}]}\right) \cdot \max(G^{\mathrm{g}}, C^{(\cdot)}).

The ``nuisance_elements`` are then computed with plug-in versions according to the general :ref:`sensitivity_implementation`.

.. note::
    Remark that the elements are only non-zero for units in the corresponding treatment group :math:`\mathrm{g}` and control group :math:`C^{(\cdot)}`, as :math:`1-G^{\mathrm{g}}=C^{(\cdot)}` if :math:`G^{\mathrm{g}} \vee C_{t_\text{eval} + \delta}^{(\cdot)}=1`.
