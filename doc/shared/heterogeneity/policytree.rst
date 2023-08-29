**Policy Learning** considers to find the optimal decision policy

.. math::

    \mathop{\arg \min}\limits_{\pi\in\Pi} = \frac{1}{n}\sum_{i=1}^n(2\pi(X_i)-1)\hat{\psi_b(W_i,\hat{\eta})}

where :math:`\Pi` denotes a policy class, which we define as depth-:math:`m` classification trees and :math:`\psi_b(W_i,\hat{\eta})` is a component of the IRM score.
