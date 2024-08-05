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

.. _sensitivity_plr:

Partially linear regression model (PLR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./sensitivity/plr_sensitivity.rst

.. _sensitivity_irm:

Interactive regression model (IRM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./sensitivity/irm_sensitivity.rst

.. _sensitivity_apo:

Average Potential Outcomes (APOs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./sensitivity/apo_sensitivity.rst

.. _sensitivity_did:

Difference-in-Differences for Panel Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./sensitivity/did_sensitivity.rst

.. _sensitivity_did_cs:

Difference-in-Differences for repeated cross-sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ./sensitivity/did_cs_sensitivity.rst