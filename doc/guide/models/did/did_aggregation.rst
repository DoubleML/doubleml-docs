The following section considers the aggregation of different :math:`ATT(\mathrm{g},t)` to summary measures based on `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_.
All implemented aggregation schemes take the form of a weighted average of the :math:`ATT(\mathrm{g},t)` estimates

.. math::
    \theta = \sum_{\mathrm{g}\in \mathcal{G}} \sum_{t=2}^{\mathcal{T}} \omega(\mathrm{g},t) \cdot ATT(\mathrm{g},t)

where :math:`\omega(\mathrm{g},t)` is a weight function based on the treatment group :math:`\mathrm{g}` and time period :math:`t`.
The aggragation schemes are implmented via the ``aggregate()`` method of the ``DoubleMLDIDMulti`` class.


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
            dml_did_obj.fit()

            agg_did_obj = dml_did_obj.aggregate(aggregation="group")
            agg_did_obj.aggregated_frameworks.bootstrap()
            print(agg_did_obj)

The method ``aggregate()`` requires the ``aggregation`` argument to be set to one of the following values:

* ``'group'``: aggregates :math:`ATT(\mathrm{g},t)` estimates by the treatment group :math:`\mathrm{g}`.
* ``'time'``: aggregates :math:`ATT(\mathrm{g},t)` estimates by the time period :math:`t` (based on group size).
* ``'eventstudy'``: aggregates :math:`ATT(\mathrm{g},t)` estimates based on time difference to first treatment assignment like an event study (based on group size).
* ``dictionary``: a dictionary with values containing the aggregation weights (as ``numpy.ma.MaskedArray``).

.. note::
    A more detailed example on effect aggregation is available in the :ref:`example gallery <did_examplegallery>`.
    For a detailed discussion on different aggregation schemes, we refer to of `Callaway and Sant'Anna (2021) <https://doi.org/10.1016/j.jeconom.2020.12.001>`_.
