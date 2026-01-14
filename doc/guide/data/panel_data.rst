The ``DoubleMLPanelData`` class serves as data-backend for :ref:`DiD models <did-models>`, as well as the :ref:`DoubleMLPLPR model <plm-models>`, and can be initialized from a dataframe.
The class is a subclass of :ref:`DoubleMLData <dml_data>` and inherits all methods and attributes.
Furthermore, it provides additional methods and attributes to handle panel data.

Key arguments
"""""""""""""

* ``id_col``: column to with unique identifiers for each unit
* ``t_col``: column to specify the time periods of the observation
* ``static_panel``: Indicates whether the data model corresponds to a static panel data approach (``True``, used for the ``DoubleMLPLPR`` model) or to staggered adoption panel data (``False``, for :ref:`DiD models <did-models>`) which is the default option.
* ``datetime_unit``: unit of the time periods (e.g. 'Y', 'M', 'D', 'h', 'm', 's')

.. note::
    The ``t_col`` can contain ``float``, ``int`` or ``datetime`` values.

Example usage
"""""""""""""

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
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


.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.plm.datasets import make_plpr_CP2025

            np.random.seed(42)
            df = make_plpr_CP2025(num_id=100, num_t=5, dim_x=5) 
            dml_data = dml.data.DoubleMLPanelData(
                df,
                y_col="y",
                d_cols="d",
                id_col="id",
                t_col="time",
                x_cols=["x1", "x2", "x3", "x4", "x5"],
                static_panel=True
            )

            print(dml_data)
