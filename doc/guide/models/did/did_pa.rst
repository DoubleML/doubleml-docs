For the estimation of the target parameters :math:`ATT(\mathrm{g},t)` the following nuisance functions are required:

.. math::
    \begin{align}
    g_{0, \mathrm{g}, t_\text{pre}, t_\text{eval}, \delta}(X_i) &:= \mathbb{E}[Y_{i,t_\text{eval}} - Y_{i,t_\text{pre}}|X_i, C_{i,t_\text{eval} + \delta}^{(\cdot)} = 1], \\
    m_{0, \mathrm{g}, t_\text{eval} + \delta}(X_i) &:= P(G_i^{\mathrm{g}}=1|X_i, G_i^{\mathrm{g}} + C_{i,t_\text{eval} + \delta}^{(\cdot)}=1).
    \end{align}

where :math:`g_{0, \mathrm{g}, t_\text{pre}, t_\text{eval},\delta}(\cdot)` denotes the population outcome change regression function and :math:`m_{0, \mathrm{g}, t_\text{eval} + \delta}(\cdot)` the generalized propensity score.

.. note::
    Remark that the nuisance functions depend on the control group used for the estimation of the target parameter.
    By slight abuse of notation we use the same notation for both control groups :math:`C_{i,t}^{(\text{nev})}` and :math:`C_{i,t}^{(\text{nyt})}`. More specifically, the
    control group only depends on :math:`\delta` for *not yet treated* units.

For a given tuple :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval})` the target parameter :math:`ATT(\mathrm{g},t)` is estimated by solving the empirical version of the the following linear moment condition:

.. math::
    ATT(\mathrm{g}, t_\text{pre}, t_\text{eval}):= -\frac{\mathbb{E}[\psi_b(W,\eta_0)]}{\mathbb{E}[\psi_a(W,\eta_0)]}

with nuisance elements :math:`\eta_0=(g_{0, \mathrm{g}, t_\text{pre}, t_\text{eval}}, m_{0, \mathrm{g}, t_\text{eval}})` and score function :math:`\psi(W,\theta, \eta)` being defined in the :ref:`DiD Score Section<did-pa-score>`.

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
                ml_g=RandomForestRegressor(min_samples_split=10),
                ml_m=RandomForestClassifier(min_samples_split=10),
                gt_combinations="standard",
                control_group="never_treated",
            )
            print(dml_did_obj.fit())

.. note::
    Remark that the output contains two different outcome regressions :math:`g(0,X)` and :math:`g(1,X)`. As in the :ref:`IRM model <irm-model>`
    the outcome regression :math:`g(0,X)` refers to the control group, whereas :math:`g(1,X)` refers to the outcome change regression for the treatment group, i.e.

    .. math::
        \begin{align}
        g(0,X) &\approx g_{0, \mathrm{g}, t_\text{pre}, t_\text{eval}, \delta}(X_i) = \mathbb{E}[Y_{i,t_\text{eval}} - Y_{i,t_\text{pre}}|X_i, C_{i,t_\text{eval} + \delta}^{(\cdot)} = 1],\\
        g(1,X) &\approx \mathbb{E}[Y_{i,t_\text{eval}} - Y_{i,t_\text{pre}}|X_i, G_i^{\mathrm{g}} = 1].
        \end{align}

    Further, :math:`g(1,X)` is only required for :ref:`Sensitivity Analysis <sensitivity-did-pa>` and is not used for the estimation of the target parameter.

.. note::
    A more detailed example is available in the :ref:`Example Gallery <did_examplegallery>`.
