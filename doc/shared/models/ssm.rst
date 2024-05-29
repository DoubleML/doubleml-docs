**Sample Selection Models (SSM)** implemented in the package focus on the the binary treatment case when outcomes are only observed for a subpopulation
due to sample selection or outcome attrition.

The implementation and notation is based on `Bia, Huber and Lafférs (2023) <https://doi.org/10.1080/07350015.2023.2271071>`_.
Let :math:`D_i` be the binary treatment indicator and :math:`Y_{i}(d)` the potential outcome under treatment value :math:`d`. Further, define
:math:`Y_{i}:=Y_{i}(D)` to be the realized outcome and :math:`S_{i}` as a binary selection indicator. The outcome :math:`Y_{i}` is only observed if :math:`S_{i}=1`.
Finally, let :math:`X_i` be a vector of observed covariates, measures prior to treatment assignment.

Target parameter of interest is the average treatment effect (ATE)

.. math::

    \theta_0 = \mathbb{E}[Y_{i}(1)- Y_{i}(0)].

The corresponding identifying assumption is

- **Cond. Independence of Treatment:** :math:`Y_i(d) \perp D_i|X_i\quad a.s.` for :math:`d=0,1`

where further assmputions are made in the context of the respective sample selection model.

.. note::
    A more detailed example can be found in the :ref:`Example Gallery <_examplegallery>`.
