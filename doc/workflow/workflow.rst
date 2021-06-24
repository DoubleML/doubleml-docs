:parenttoc: True

DoubleML Workflow
=================

TODO: Highlight of General vs. Example-Specific Part

The following steps, which we call the DoubleML workflow, are intended to provide a rough structure for causal analyses
with the :ref:`DoubleML <doubleml_package>`. After a short explanation of the idea of each step, we illustrate their meaning in the 401(k)
example. In case you are interested in more details of the 401(k) example, you can visit the Python and R Notebooks that
are available online.

TODO: insert links to notebooks

0. Problem Formulation
----------------------

The initial step of the DoubleML workflow is to formulate the causal problem at hand. Before we start our statistical
analysis, we have to explicitly state the conditions required for a causal interpretation of the estimator, which will
be computed later. In many cases, directed acyclical graphs (DAGs) are helpful to formulate the causal problem,
illustrate the involved causal channels and the critical parts of the inferential framework. At this stage, a precise
argumentation and discussion of the research question is crucial.

TODO: Set up and insert a DAG for the 401(k) Example: IV-based argumentation (eligibility - participation - outcome)

In the 401(k) study, we are interested in estimating the causal effect of participation in so-called 401(k) pension
plans on employees' net financial assets. To do so, we use observational data. Thus, we cannot rely on a properly conducted
randomized control study and have to argue that the treatment (= an employee's participation in a 401(k) plan)
is as good as randomly assigned once we credibly control for observable characteristics. A complication that arises
in the 401(k) example is due to so-called endogeneity of the treatment assignment: Participation is a decision made by employees and
unobservable effects may generally affect this decision. However, it is possible to justify that eligibility, in other words
access to the treatment, can be considered as exogenous, once we control for confounding variables. Earlier studies in this context
argue that if characteristics that are related to saving preferences are taken into account, eligibility can be considered
as good as randomly assigned. For example, is seems reasonable that persons with higher income have a stronger preference
to save and also to participate in a pension plan. Rather than focusing on the instrumental variable analysis for the sake of brevity,
we will focus on a so-called intent-to-treat effect. This quantity corresponds to the causal effect of eligibility on participation
and is of great interest in many applications.

TODO: Polish formulations

pension plan participation
**Description of the Case Study and Data**

* 401(k) plans are pension accounts sponsored by employers
* **Estimate the effect of 401(k) eligibility and participation on accumulated assets**
* Problems: **Saver heterogeneity** and the fact that the **decision to enroll** in a 401(k) **is non-random**
* **Conventional estimates** that do not account for saver heterogeneity and endogeneity of participation **will be biased**

TO BE CONTINUED

1. Data-Backend
---------------

We use data from the 1991 Survey of Income and Program Participation which is available via ...

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

