To estimate the target parameter :math:`ATT(\mathrm{g},t_\text{eval})`, the implementation (both for panel data or repeated cross sections) is based on the following parameters:

* :math:`\mathrm{g}` is the first post-treatment period of interest, i.e. the treatment group.
* :math:`t_\text{pre}` is the pre-treatment period, i.e. the time period from which the conditional parallel trends are assumed.
* :math:`t_\text{eval}` is the time period of interest or evaluation period, i.e. the time period where the treatment effect is evaluated.
* :math:`\delta` is number of anticipation periods, i.e. the number of time periods for which units are assumed to anticipate the treatment.


Under the assumptions above the target parameter :math:`ATT(\mathrm{g},t_\text{eval})` can be estimated by choosing a suitable combination
of :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval}, \delta)` if :math:`t_\text{eval} - t_\text{pre} \ge 1 + \delta`, i.e. the parallel trends are assumed to hold at least one period more than the anticipation period.

.. note::
    The choice :math:`t_\text{pre}= \min(\mathrm{g},t_\text{eval}) -\delta-1` corresponds to the definition of :math:`ATT_{dr}(\mathrm{g},t_\text{eval};\delta)` from `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_.

    As an example, if the target parameter is the effect on the group receiving treatment in :math:`2006` but evaluated in :math:`2007` with an anticipation period of :math:`\delta=1`, then the pre-treatment period is :math:`2004`.
    The parallel trend assumption is slightly stronger with anticipation as the trends have to parallel for a longer periods, i.e. :math:`ATT_{dr}(2006,2007;1)=ATT(2006,2004;2006)`.

In the following, we will omit the subscript :math:`\delta` in the notation of the nuisance functions and the control group (implicitly assuming :math:`\delta=0`).

For a given tuple :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval})` the target parameter :math:`ATT(\mathrm{g},t)` is estimated by solving the empirical version of the the following linear moment condition:

.. math::
    ATT(\mathrm{g}, t_\text{pre}, t_\text{eval}):= -\frac{\mathbb{E}[\psi_b(W,\eta_0)]}{\mathbb{E}[\psi_a(W,\eta_0)]}

with nuisance elements :math:`\eta_0` which depend on the parameter combination :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval})` and score function :math:`\psi(W,\theta, \eta)` (for details, see :ref:`Panel Data Details <did-pa-model>` or :ref:`Repeated Cross-Section Details <did-cs-model>`).
Under the identifying assumptions above 

.. math::
    ATT(\mathrm{g}, t_\text{pre}, t_\text{eval}) = ATT(\mathrm{g},t).

``DoubleMLDIDMulti`` implements the estimation of :math:`ATT(\mathrm{g}, t_\text{pre}, t_\text{eval})` for multiple time periods and requires :ref:`DoubleMLPanelData <dml_panel_data>` as input.

Setting ``gt_combinations='standard'`` will estimate the target parameter for all (possible) combinations of :math:`(\mathrm{g}, t_\text{pre}, t_\text{eval})` with :math:`\mathrm{g}\in\{2,\dots,\mathcal{T}\}` and :math:`(t_\text{pre}, t_\text{eval})` with :math:`t_\text{eval}\in\{2,\dots,\mathcal{T}\}` and
:math:`t_\text{pre}= \min(\mathrm{g},t_\text{eval}) -\delta-1`.
This corresponds to the setting where all trends are set as short as possible, but still respecting the anticipation period.
