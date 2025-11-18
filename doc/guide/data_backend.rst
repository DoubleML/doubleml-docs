.. _data_backend:

Data Backend
------------

:ref:`DoubleML <doubleml_package>` provides a unified data interface via the :mod:`doubleml.data` module.
It supports both :py:class:`pandas.DataFrame` objects and :py:class:`numpy.ndarray` arrays and now allows
clustered data to be handled directly via :class:`~doubleml.data.DoubleMLData`.

.. _dml_data:

DoubleMLData
~~~~~~~~~~~~

.. include:: data/base_data.rst


.. _dml_data_types:

Special Data Types
~~~~~~~~~~~~~~~~~~

The :ref:`DoubleMLData <dml_data>` class is extended by the following classes to support special data
types or allow for additional parameters.

.. _dml_did_data:

DoubleMLDIDData
^^^^^^^^^^^^^^^

.. include:: data/did_data.rst


.. _dml_panel_data:

DoubleMLPanelData
^^^^^^^^^^^^^^^^^

.. include:: data/panel_data.rst


.. _dml_rdd_data:

DoubleMLRDDData
^^^^^^^^^^^^^^^

.. include:: data/rdd_data.rst


.. _dml_ssm_data:

DoubleMLSSMData
^^^^^^^^^^^^^^^

.. include:: data/ssm_data.rst

