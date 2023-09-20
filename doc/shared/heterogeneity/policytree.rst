**Policy Learning** considers to find an optimal decision policy. We consider deterministic binary policies, which are defined as mapping

.. math::

    \pi: X\mapsto \{0,1\}.

Using the score component :math:`\psi_b(W_i,\hat{\eta})` of the :ref:`IRM <irm-model>` score, 
we can find the optimal treatment policy by solving the weighted classification problem

.. math::

    \mathop{\arg \min}\limits_{\pi\in\Pi} = \frac{1}{n}\sum_{i=1}^n(2\pi(X_i)-1)\hat{\psi_b(W_i,\hat{\eta})},

where :math:`\Pi` denotes a policy class, which we define as depth-:math:`m` classification trees.
Thus, we estimate splits in the features :math:`X` that reflect the heterogeneity of the treatment effect 
and consequently maximize the sum of the estimated individual treatment effects of all individuals by assigning different treatments.
