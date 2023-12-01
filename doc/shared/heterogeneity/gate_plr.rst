**Group Average Treatment Effects (GATEs)** for ``DoubleMLPLR`` models consider a slightly adjusted version of the ``DoubleMLPLR`` model. 
Instead of considering a constant treatment effect :math:`\theta_0` for all observations, the adjusted model allows for a different effect based on groups.

.. math::

    Y = D \theta_0(G_k) + g_0(X) + \zeta, & &\mathbb{E}(\zeta | D,X) = 0,

    D = m_0(X) + V, & &\mathbb{E}(V | X) = 0,

where :math:`G_k` for :math:`k=1,\dots, K` denotes a group indicator where the groups can depend on the counfounding features :math:`X`.

Point estimates and confidence intervals can be obtained via the ``gate()`` and ``confint()`` methods.
