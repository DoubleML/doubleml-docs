In the :ref:`irm-model` the (weighted) average potential outcome for the treatment level :math:`d` can be written as

.. math::

    \theta_0 = \mathbb{E}[g_0(d,X)\omega(Y,D,X)]

where :math:`\omega(Y,D,X)` are weights (e.g. set to :math:`1` for the APO).
This implies the following representations

.. math::

    m(W,g) &= g(d,X)\omega(Y,D,X)

    \alpha(W) &= \frac{1\lbrace D = d\rbrace }{m(X)}\cdot\mathbb{E}[\omega(Y,D,X)|X].

.. note::

    In the :ref:`irm-model` the form and interpretation of ``cf_y`` only depends on the conditional expectation :math:`\mathbb{E}[Y|D,X]`.

    - ``cf_y`` has the interpretation as the *nonparametric partial* :math:`R^2` *of* :math:`A` *with* :math:`Y` *given* :math:`(D,X)`
    
    .. math:: 
        
        \frac{\textrm{Var}(\mathbb{E}[Y|D,X,A]) - \textrm{Var}(\mathbb{E}[Y|D,X])}{\textrm{Var}(Y)-\textrm{Var}(\mathbb{E}[Y|D,X])}
    
    - ``cf_d`` takes the following form
    
    .. math:: 
        
        \frac{\mathbb{E}\left[\frac{1}{P(D=d|X,A)}\right] - \mathbb{E}\left[\frac{1}{P(D=d|X)}\right]}{\mathbb{E}\left[\frac{1}{P(D=d|X,A)}\right]}

    where the numerator measures the *average change in inverse propensity weights for* :math:`D=d` *conditional on* :math:`A` *in addition to* :math:`X`.
    The denominator is the *average inverse propensity weights for* :math:`D=d` *conditional on* :math:`A` *and* :math:`X`. Consequently ``cf_d`` measures the *relative change in inverse propensity weights*.
    Including weights changes only the definition of ``cf_d`` to 

    .. math::

        \frac{\mathbb{E}\left[\frac{1}{P(D=d|X,A)}\mathbb{E}[\omega(Y,D,X)|X,A]^2\right] - \mathbb{E}\left[\frac{1}{P(D=d|X)}\mathbb{E}[\omega(Y,D,X)|X]^2\right]}{\mathbb{E}\left[\frac{1}{P(D=d|X,A)}\mathbb{E}[\omega(Y,D,X)|X,A]^2\right]}

    which has a interpretation as the *relative weighted change in inverse propensity weights*.

The ``nuisance_elements`` are then computed with plug-in versions according to the general :ref:`sensitivity_implementation`. 
The default weights are set to one 

.. math::

    \omega(Y,D,X) = 1,

whereas 

.. math::

    \bar{\omega}(X) := \mathbb{E}[\omega(Y,D,X)|X],

have to be supplied for weights which depend on :math:`Y` or :math:`D`.
