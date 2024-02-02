**Conditional Average Treatment Effects (CATEs)** for ``DoubleMLIRM`` models consider the target parameters

.. math::

    \theta_{0}(x) = \mathbb{E}[Y(1) - Y(0)| X=x]

for a low-dimensional feature :math:`X`, where :math:`Y(d)` the potential outcome with :math:`d \in \{0, 1\}`.

Point estimates and confidence intervals can be obtained via the ``gate()`` and ``confint()`` methods.