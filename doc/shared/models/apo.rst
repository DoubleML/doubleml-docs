For general discrete-values treatments :math:`D \in \lbrace d_0, \dots, d_l \rbrace` the model can be generalized to

.. math::

    Y = g_0(D, X) + U, & &\mathbb{E}(U | X, D) = 0,

    A_j = m_{0,j}(X) + V, & &\mathbb{E}(V | X) = 0,

where :math:`A_j := I\lbrace D = d_j\rbrace` is an indicator variable for treatment level :math:`d_j` and :math:`m_{0,j}(X)` denotes
the corresponding propensity score.

Possible target parameters of interest in this model are the average potential outcomes (APOs)

.. math::

    \theta_{0,j} = \mathbb{E}[g_0(d_j, X)].