.. _python_api:

API reference
=============

Double machine learning data class
----------------------------------

.. currentmodule:: doubleml

.. autosummary::
    :toctree: generated/
    :template: class.rst

    DoubleMLData
    DoubleMLClusterData

Double machine learning models
------------------------------

.. currentmodule:: doubleml

.. autosummary::
    :toctree: generated/
    :template: class.rst

    DoubleMLPLR
    DoubleMLPLIV
    DoubleMLIRM
    DoubleMLAPO
    DoubleMLAPOS
    DoubleMLIIVM
    DoubleMLDID
    DoubleMLDIDCS
    DoubleMLSSM
    DoubleMLPQ
    DoubleMLLPQ
    DoubleMLCVAR
    DoubleMLQTE

Datasets module
---------------


Dataset loaders
~~~~~~~~~~~~~~~

.. currentmodule:: doubleml

.. autosummary::
   :toctree: generated/

   datasets.fetch_401K
   datasets.fetch_bonus

Dataset generators
~~~~~~~~~~~~~~~~~~

.. currentmodule:: doubleml

.. autosummary::
   :toctree: generated/

   datasets.make_plr_CCDDHNR2018
   datasets.make_pliv_CHS2015
   datasets.make_irm_data
   datasets.make_iivm_data
   datasets.make_plr_turrell2018
   datasets.make_pliv_multiway_cluster_CKMS2021
   datasets.make_did_SZ2020
   datasets.make_ssm_data
   datasets.make_confounded_plr_data
   datasets.make_confounded_irm_data
   datasets.make_heterogeneous_data
   datasets.make_irm_data_discrete_treatments

Utility classes and functions
-----------------------------

Utility classes
~~~~~~~~~~~~~~~

.. currentmodule:: doubleml

.. autosummary::
    :toctree: generated/
    :template: class.rst

    utils.DMLDummyRegressor
    utils.DMLDummyClassifier
    utils.DoubleMLBLP
    utils.DoubleMLPolicyTree
    utils.DoubleMLResampling
    utils.DoubleMLClusterResampling

Utility functions
~~~~~~~~~~~~~~~~~

.. currentmodule:: doubleml

.. autosummary::
    :toctree: generated/

    utils.gain_statistics

Score mixin classes for double machine learning models
------------------------------------------------------

.. currentmodule:: doubleml

.. autosummary::
    :toctree: generated/
    :template: class.rst

    double_ml_score_mixins.LinearScoreMixin
    double_ml_score_mixins.NonLinearScoreMixin
