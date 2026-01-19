.. _api_datasets:

Datasets
---------

Dataset Loaders
~~~~~~~~~~~~~~~

.. currentmodule:: doubleml.datasets

.. autosummary::
   :toctree: generated/

   fetch_401K
   fetch_bonus

Dataset Generators
~~~~~~~~~~~~~~~~~~

.. currentmodule:: doubleml

.. autosummary::
   :toctree: generated/

   irm.datasets.make_irm_data
   irm.datasets.make_iivm_data
   irm.datasets.make_heterogeneous_data
   irm.datasets.make_irm_data_discrete_treatments
   irm.datasets.make_confounded_irm_data
   irm.datasets.make_ssm_data

   plm.datasets.make_plr_CCDDHNR2018
   plm.datasets.make_plr_turrell2018
   plm.datasets.make_lplr_LZZ2020
   plm.datasets.make_plpr_CP2025
   plm.datasets.make_pliv_CHS2015
   plm.datasets.make_pliv_multiway_cluster_CKMS2021
   plm.datasets.make_confounded_plr_data

   did.datasets.make_did_SZ2020
   did.datasets.make_did_CS2021
   did.datasets.make_did_cs_CS2021

   rdd.datasets.make_simple_rdd_data
