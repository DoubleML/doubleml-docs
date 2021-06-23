:parenttoc: True

DoubleML Workflow
=================

0. Problem Formulation
----------------------

**Description of the Case Study and Data**

* 401(k) plans are pension accounts sponsored by employers
* **Estimate the effect of 401(k) eligibility and participation on accumulated assets**
* Problems: **Saver heterogeneity** and the fact that the **decision to enroll** in a 401(k) **is non-random**
* **Conventional estimates** that do not account for saver heterogeneity and endogeneity of participation **will be biased**

TO BE CONTINUED

1. Data-Backend
---------------

.. tabbed:: Python

    .. ipython:: python

        from doubleml import DoubleMLData
        from doubleml.datasets import fetch_401K
        data = fetch_401K(return_type='DataFrame')
        # Construct DoubleMLData object
        dml_data = DoubleMLData(data, y_col='net_tfa', d_cols='e401',
                                x_cols=['age', 'inc', 'educ', 'fsize', 'marr',
                                        'twoearn', 'db', 'pira', 'hown'])

.. tabbed:: R

    .. jupyter-execute::

        library(DoubleML)
        data = fetch_401k(return_type='data.table')
        # Construct DoubleMLData object from data.table
        dml_data = DoubleMLData$new(data, y_col='net_tfa', d_cols='e401',
                                x_cols=c('age', 'inc', 'educ', 'fsize',
                                         'marr', 'twoearn', 'db', 'pira',
                                         'hown'))

        data_frame = fetch_401k(return_type='data.frame')
        # Construct DoubleMLData object from data.frame
        dml_data_df = double_ml_data_from_data_frame(data_frame,
                                                     y_col='net_tfa',
                                                     d_cols='e401',
                                                     x_cols=c('age', 'inc',
                                                              'educ', 'fsize',
                                                              'marr', 'twoearn',
                                                              'db', 'pira',
                                                              'hown'))

2. Causal Model
---------------


3. ML Methods
-------------


4. DML Specifications
---------------------

5. Estimation
-------------


6. Inference
------------

