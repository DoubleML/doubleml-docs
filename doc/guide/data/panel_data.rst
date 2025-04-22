The ``DoubleMLPanelData`` class serves as data-backend for :ref:`DiD models <did-models>` and can be initialized from a dataframe.
The class is a subclass of :ref:`DoubleMLData <dml_data>` and inherits all methods and attributes.
Furthermore, it provides additional methods and attributes to handle panel data ()

* ``id_col``: column to with unique identifiers for each unit
* ``t_col``: column to specify the time periods of the observation
* ``datetime_unit``: unit of the time periods (e.g. 'Y', 'M', 'D', 'h', 'm', 's')

.. note::
    The ``t_col`` can contain ``float``, ``int`` or ``datetime`` values.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            from doubleml.did.datasets import make_did_CS2021

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
            print(dml_data)
