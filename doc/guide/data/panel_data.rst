The ``DoubleMLPanelData`` class serves as data-backend for :ref:`DiD models <did-models>` and can be initialized from a dataframe.
The class is a subclass of :ref:`DoubleMLData <dml_data>` and inherits all methods and attributes.
Furthermore, it provides additional methods and attributes to handle panel data ()

* ``id_col``: column to identify the individual units
* ``t_col``: column to specify the time periods
* ``datetime_unit``: unit of the time periods (e.g. 'Y', 'M', 'D', 'h', 'm', 's')

.. note::
    The ``t_col`` can contain either 