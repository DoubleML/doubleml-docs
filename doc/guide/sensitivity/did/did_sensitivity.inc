The following difference-in-differences models implemented.

.. note::
    Remark that :ref:`sensitivity_benchmark` is only relevant for ``score='observational'``, since no effect of :math:`X` on treatment assignment is assumed.
    Generally, we recommend ``score='observational'``, if unobserved confounding seems plausible.


.. _sensitivity-did-pa:

Difference-in-Differences for Panel Data
========================================

.. include:: /guide/sensitivity/did/did_pa_sensitivity.rst


.. _sensitivity-did-cs:

Difference-in-Differences for repeated cross-sections
=====================================================

.. include:: /guide/sensitivity/did/did_cs_sensitivity.rst


.. _sensitivity-did-binary:

Two treatment periods
======================


.. warning::
    This documentation refers to the deprecated implementation for two time periods. 
    This functionality will be removed in a future version. The generalized version are :ref:`sensitivity-did-pa` and :ref:`sensitivity-did-cs`.


.. _sensitivity-did-pa-binary:

Panel Data
""""""""""

.. include:: /guide/sensitivity/did/did_pa_binary_sensitivity.rst


.. _sensitivity-did-cs-binary:

Repeated Cross-Sectional Data
"""""""""""""""""""""""""""""

.. include:: /guide/sensitivity/did/did_cs_binary_sensitivity.rst