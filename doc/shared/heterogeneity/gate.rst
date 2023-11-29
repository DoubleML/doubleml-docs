**Group Average Treatment Effects (GATEs)** for ``DoubleMLIRM`` models consider the target parameters

.. math::

    \theta_{0,k} = \mathbb{E}[Y(1) - Y(0)| G_k],\quad k=1,\dots, K.

where :math:`G_k` denotes a group indicator and :math:`Y(d)` the potential outcome with :math:`d \in \{0, 1\}`.

Point estimates and confidence intervals can be obtained via the ``gate()`` and ``confint()`` methods.
Remark that the groups should be mutually exclusive.