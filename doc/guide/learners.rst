.. _learners:

Learners, hyperparameters and hyperparameter tuning
-----------------------------------------------------------

The estimation of a double/debiased machine learning model involves the estimation of several nuisance function with
machine learning estimators.
Such learners are implemented in various Python and R packages.
The implementation of :ref:`DoubleML <doubleml_package>` is based on the meta-packages
`scikit-learn <https://scikit-learn.org/>`_ for Python and `mlr3 <https://mlr3.mlr-org.com/>`_ for R.
The interfaces to specify the learners, set hyperparameters and tune hyperparameters are described in the following
separately for :ref:`Python <learners_python>` and :ref:`R <learners_r>`.

.. _learners_python:

Python: Learners and hyperparameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: learners/python/learners_overview.inc


.. _learners_r:

R: Learners and hyperparameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include::  learners/r/learners_overview.inc


