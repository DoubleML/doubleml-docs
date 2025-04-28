.. _sensitivity:

Sensitivity analysis
------------------------

The :ref:`DoubleML <doubleml_package>` package implements sensitivity analysis with respect to omitted variable bias
based on `Chernozhukov et al. (2022) <https://www.nber.org/papers/w30302>`_.

.. _sensitivity_general:

General algorithm
+++++++++++++++++

The section :ref:`sensitivity_theory` contains a general summary and the relevant defintions, whereas :ref:`sensitivity_implementation` considers
the general part of the implementation.

.. _sensitivity_theory:

Theory
~~~~~~

.. include:: ./sensitivity/theory.rst

.. _sensitivity_implementation:

Implementation
~~~~~~~~~~~~~~

.. include:: ./sensitivity/implementation.rst

.. _sensitivity_benchmark:

Benchmarking
~~~~~~~~~~~~

.. include:: ./sensitivity/benchmarking.rst

.. _sensitivity_models:

Model-specific implementations
+++++++++++++++++++++++++++++++++++

This section contains the implementation details for each specific model and model specific interpretations.

.. _plm-sensitivity:

Partially linear models (PLM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: sensitivity/plm/plm_sensitivity.inc


.. _irm-sensitivity:

Interactive regression models (IRM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: sensitivity/irm/irm_sensitivity.inc


.. _did-sensitivity:

Difference-in-Differences Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: sensitivity/did/did_sensitivity.inc
