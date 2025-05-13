In the :ref:`irm-model` the target parameter can be written as

.. math::

    \theta_0 = \mathbb{E}[(g_0(1,X) - g_0(0,X))\omega(Y,D,X)]

where :math:`\omega(Y,D,X)` are weights (e.g. set to :math:`1` for the ATE).
This implies the following representations

.. math::

    m(W,g) &= \big(g(1,X) - g(0,X)\big)\omega(Y,D,X)

    \alpha(W) &= \bigg(\frac{D}{m(X)} - \frac{1-D}{1-m(X)}\bigg)  \mathbb{E}[\omega(Y,D,X)|X].


.. note::

    In the :ref:`irm-model` with for the ATE (weights equal to :math:`1`), the form and interpretation of ``cf_y`` is the same as in the :ref:`plr-model`.

    - ``cf_y`` has the interpretation as the *nonparametric partial* :math:`R^2` *of* :math:`A` *with* :math:`Y` *given* :math:`(D,X)`
    
    .. math:: 
        
        \frac{\textrm{Var}(\mathbb{E}[Y|D,X,A]) - \textrm{Var}(\mathbb{E}[Y|D,X])}{\textrm{Var}(Y)-\textrm{Var}(\mathbb{E}[Y|D,X])}
    
    - ``cf_d`` takes the following form
    
    .. math:: 
        
        \small{\frac{\mathbb{E}\Big[\big(P(D=1|X,A)(1-P(D=1|X,A))\big)^{-1}\Big] - \mathbb{E}\Big[\big(P(D=1|X)(1-P(D=1|X))\big)^{-1}\Big]}{\mathbb{E}\Big[\big(P(D=1|X,A)(1-P(D=1|X,A))\big)^{-1}\Big]}}

    where the numerator measures the *gain in average conditional precision to predict* :math:`D` *by using* :math:`A` *in addition to* :math:`X`.
    The denominator is the *average conditional precision to predict* :math:`D` *by using* :math:`A` *and* :math:`X`. Consequently ``cf_d`` measures the *relative gain in average conditional precision*.

    Remark that :math:`P(D=1|X,A)(1-P(D=1|X,A))` denotes the variance of the conditional distribution of :math:`D` given :math:`(X,A)`, such that the inverse measures the precision of
    predicting :math:`D` conditional on :math:`(X,A)`.
    
    Since :math:`C_D^2=\frac{cf_d}{1 - cf_d}`, this corresponds to

    .. math:: 

        C_D^2= \small{\frac{\mathbb{E}\Big[\big(P(D=1|X,A)(1-P(D=1|X,A))\big)^{-1}\Big] - \mathbb{E}\Big[\big(P(D=1|X)(1-P(D=1|X))\big)^{-1}\Big]}{\mathbb{E}\Big[\big(P(D=1|X)(1-P(D=1|X))\big)^{-1}\Big]}}
    
    which has the same numerator but is instead relative to the *average conditional precision to predict* :math:`D` *by using only* :math:`X`.

    Including weights changes only the definition of ``cf_d`` to 

    .. math::

        \frac{\mathbb{E}\left[\frac{\mathbb{E}[\omega(Y,D,X)|X,A]^2}{P(D=1|X,A)(1-P(D=1|X,A))}\right] - \mathbb{E}\left[\frac{\mathbb{E}[\omega(Y,D,X)|X]^2}{P(D=1|X)(1-P(D=1|X))}\right]}{\mathbb{E}\left[\frac{\mathbb{E}[\omega(Y,D,X)|X,A]^2}{P(D=1|X,A)(1-P(D=1|X,A))}\right]}

    which has a interpretation as the *relative weighted gain in average conditional precision*.

The ``nuisance_elements`` are then computed with plug-in versions according to the general :ref:`sensitivity_implementation`. 
For ``score='ATE'``, the weights are set to one 

.. math::

    \omega(Y,D,X) = 1,

wheras for ``score='ATTE'``

.. math::

    \omega(Y,D,X) = \frac{D}{\mathbb{E}[D]},

such that

.. math::

    \mathbb{E}[\omega(Y,D,X)|X] = \frac{m(X)}{\mathbb{E}[D]}.
