For the estimation of the target parameters :math:`ATT(\mathrm{g},t)` the following nuisance functions are required:

.. math::
    \begin{align}
    g_{0, \mathrm{g}, t_{pre}, t_{eval}, \delta}(X_i) &:= \mathbb{E}[Y_{i,t_{eval}} - Y_{i,t_{pre}}|X_i, C_{i,t_{eval} + \delta}^{(\cdot)} = 1], \\
    m_{0, \mathrm{g}, t_{eval} + \delta}(X_i) &:= P(G_i^{\mathrm{g}}=1|X_i, G_i^{\mathrm{g}} + C_{i,t_{eval} + \delta}^{(\cdot)}=1).
    \end{align}

where :math:`g_{0, \mathrm{g}, t_{pre}, t_{eval},\delta}(\cdot)` denotes the population outcome regression function and :math:`m_{0, \mathrm{g}, t_{eval} + \delta}(\cdot)` the generalized propensity score.
The interpretation of the parameters is as follows:

* :math:`\mathrm{g}` is the first post-treatment period of interest, i.e. the treatment group.
* :math:`t_{pre}` is the pre-treatment period, i.e. the time period from which the conditional parallel trends are assumed.
* :math:`t_{eval}` is the time period of interest or evaluation period, i.e. the time period where the treatment effect is evaluated.
* :math:`\delta` is number of anticipation periods, i.e. the number of time periods for which units are assumed to anticipate the treatment.

.. note::
    Remark that the nuisance functions depend on the control group used for the estimation of the target parameter.
    By slight abuse of notation we use the same notation for both control groups :math:`C_{i,t}^{(nev)}` and :math:`C_{i,t}^{(nyt)}`. More specifically, the
    control group only depends on :math:`\delta` for *not yet treated* units.

Under these assumptions the target parameter :math:`ATT(\mathrm{g},t_{eval})` can be estimated by choosing a suitable combination
of :math:`(\mathrm{g}, t_{pre}, t_{eval}, \delta)` if :math:`t_{eval} - t_{pre} \ge 1 + \delta`, i.e. the parallel trends are assumed to hold at least one period more than the anticipation period.

.. note::
    The choice :math:`t_{pre}= \min(\mathrm{g},t_\text{eval}) -\delta-1` corresponds to the definition of :math:`ATT_{dr}(\mathrm{g},t_\text{eval};\delta)` from `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_.

In the following, we will omit the subscript :math:`\delta` in the notation of the nuisance functions and the control group (implicitly assuming :math:`\delta=0`).

For a given tuple :math:`(\mathrm{g}, t_{pre}, t_{eval})` the target parameter :math:`ATT(\mathrm{g},t)` is estimated by solving the empirical version of the the following linear moment condition:

.. math::
    ATT(\mathrm{g}, t_{pre}, t_{eval}):= -\frac{\mathbb{E}[\psi_b(W,\eta_0)]}{\mathbb{E}[\psi_a(W,\eta_0)]}

with nuisance elements :math:`\eta_0=(g_{0, \mathrm{g}, t_{pre}, t_{eval}}, m_{0, \mathrm{g}, t_{eval}})` and score function :math:`\psi(W,\theta, \eta)` being defined in section :ref:`did-pa-score`.
Under the identifying assumptions above 

.. math::
    ATT(\mathrm{g}, t_{pre}, t_{eval}) = ATT(\mathrm{g},t).

``DoubleMLDIDMulti`` implements the estimation of :math:`ATT(\mathrm{g}, t_{pre}, t_{eval})` for multiple time periods and requires :ref:`DoubleMLPanelData <dml_panel_data>` as input.
Setting ``gt_combinations='standard'`` will estimate the target parameter for all (possible) combinations of :math:`(\mathrm{g}, t_{pre}, t_{eval})` with :math:`\mathrm{g}\in\{2,\dots,\mathcal{T}\}` and :math:`(t_{pre}, t_{eval})` with :math:`t_{eval}\in\{2,\dots,\mathcal{T}\}` and
:math:`t_{pre}= \min(\mathrm{g},t_\text{eval}) -\delta-1`.
This corresponds to the setting where all trends are set as short as possible, but still respecting the anticipation period. 

Estimation is conducted via its ``fit()`` method:

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            :okwarning:

            import numpy as np
            import doubleml as dml
            from doubleml.did.datasets import make_did_CS2021
            from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

            np.random.seed(42)
            df = make_did_CS2021(n_obs=500) 
            dml_data = dml.data.DoubleMLPanelData(
                df,
                y_col="y",
                d_cols="d",
                id_col="id",
                t_col="t",
                x_cols=["Z1", "Z2", "Z3", "Z4"],
                datetime_unit="M"
            )
            dml_did_obj = dml.did.DoubleMLDIDMulti(
                obj_dml_data=dml_data,
                ml_g=ml_g,
                ml_m=ml_m,
                gt_combinations="standard",
                control_group="never_treated",
            )
            print(dml_did_obj.fit())

.. note::
    Remark that the output contains two different outcome regressions :math:`g(0,X)` and :math:`g(1,X)`. As in the :ref:`IRM model <irm-model>`
    the outcome regression :math:`g(0,X)` refers to the control group, whereas :math:`g(1,X)` refers to the outcome regression for the treatment group, i.e.

    .. math::
        \begin{align}
        g(0,X) &\approx g_{0, \mathrm{g}, t_{pre}, t_{eval}, \delta}(X_i) = \mathbb{E}[Y_{i,t_{eval}} - Y_{i,t_{pre}}|X_i, C_{i,t_{eval} + \delta}^{(\cdot)} = 1],\\
        g(1,X) &\approx \mathbb{E}[Y_{i,t_{eval}} - Y_{i,t_{pre}}|X_i, G_i^{\mathrm{g}} = 1].
        \end{align}

    Further, :math:`g(1,X)` is only required for :ref:`Sensitivity Analysis <sensitivity-did-pa>` and is not used for the estimation of the target parameter.

.. note::
    A more detailed example is available in the :ref:`Example Gallery <examplegallery>`.
