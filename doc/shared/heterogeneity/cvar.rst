For a quantile :math:`\tau \in (0,1)` the target parameters :math:`\theta_{\tau}(d)` of interest are
the **conditional values at risk (CVaRs)** of the potential outcomes,

.. math::

    \theta_{\tau}(d) = \frac{\mathbb{E}[Y(d) 1\{F_{Y(d)}(Y(d) \ge \tau)]}{1-\tau},


where :math:`Y(d)` denotes the potential outcome with :math:`d \in \{0, 1\}` and 
:math:`F_{Y(d)}(x)` the corresponding cdf of :math:`Y(d)`. 
