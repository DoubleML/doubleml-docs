In the :ref:`did-pa-model` with ``score='observational'`` and ``in_sample_normalization=True`` the score function implies the following representations

.. math::

    m(W,g) &= \big(g(1,X) - g(0,X))\frac{D}{\mathbb{E}[D]}

    \alpha(W) &= \frac{D}{\mathbb{E}[D]} - \frac{\frac{m(X)(1-D)}{1-m(X)}}{\mathbb{E}\left[\frac{m(X)(1-D)}{1-m(X)}\right]}.

If instead ``in_sample_normalization=False``, the Riesz representer changes to 

.. math::

    \alpha(W) = \frac{D}{\mathbb{E}[D]} - \frac{m(X)(1-D)}{\mathbb{E}[D](1-m(X))}.

For ``score='experimental'`` implies the score function implies the following representations

.. math::

    m(W,g) &= g(1,X) - g(0,X)

    \alpha(W) &= \frac{D}{\mathbb{E}[D]} - \frac{1-D}{1-\mathbb{E}[D]}.

The ``nuisance_elements`` are then computed with plug-in versions according to the general :ref:`sensitivity_implementation`.