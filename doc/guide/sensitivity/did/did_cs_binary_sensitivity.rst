In the :ref:`did-cs-model` with ``score='observational'`` and ``in_sample_normalization=True`` the score function implies the following representations

.. math::

    m(W,g) &= \Big(\big(g(1,1,X) - g(1,0,X)\big) - \big(g(0,1,X) - g(0,0,X)\big)\Big) \frac{D}{\mathbb{E}[D]}

    \alpha(W) &= \frac{DT}{\mathbb{E}[DT]} - \frac{D(1-T)}{\mathbb{E}[D(1-T)]}

    &\quad - \frac{m(X)(1-D)T}{1-m(X)}\mathbb{E}\left[\frac{m(X)(1-D)T}{1-m(X)}\right]^{-1}

    &\quad + \frac{m(X)(1-D)(1-T)}{1-m(X)}\mathbb{E}\left[\frac{m(X)(1-D)(1-T)}{1-m(X)}\right]^{-1}.

If instead ``in_sample_normalization=False``, the Riesz representer (after simplifications) changes to 

.. math::

    \alpha(W) = \left(\frac{T}{\mathbb{E}[D]\mathbb{E}[T]} + \frac{1-T}{\mathbb{E}[D](1-\mathbb{E}[T])}\right)\left(D - (1-D)\frac{m(X)}{1-m(X)}\right).

For ``score='experimental'`` and ``in_sample_normalization=True`` implies the score function implies the following representations

.. math::

    m(W,g) &= \big(g(1,1,X) - g(1,0,X)\big) - \big(g(0,1,X) - g(0,0,X)\big)

    \alpha(W) &= \frac{DT}{\mathbb{E}[DT]} - \frac{D(1-T)}{\mathbb{E}[D(1-T)]} - \frac{(1-D)T}{\mathbb{E}[(1-D)T]} + \frac{(1-D)(1-T)}{\mathbb{E}[(1-D)(1-T)]}.

And again, if instead ``in_sample_normalization=False``, the Riesz representer (after simplifications) changes to 

.. math::

    \alpha(W) = \frac{DT}{\mathbb{E}[D]\mathbb{E}[T]} - \frac{D(1-T)}{\mathbb{E}[D](1-\mathbb{E}[T])} - \frac{(1-D)T}{(1-\mathbb{E}[D])\mathbb{E}[T]} + \frac{(1-D)(1-T)}{(1-\mathbb{E}[D])(1-\mathbb{E}[T])}.


The ``nuisance_elements`` are then computed with plug-in versions according to the general :ref:`sensitivity_implementation`.