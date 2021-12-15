:parenttoc: True

Release notes
=============

.. tabbed:: Python

    **DoubleML 0.4.0**

    - **Release highlight:** Clustered standard errors for double machine learning models
      `#116 <https://github.com/DoubleML/doubleml-for-py/pull/116>`_
    - Improve exception handling for missings and infinite values in the confounders, predictions, etc.
      (fixes `#120 <https://github.com/DoubleML/doubleml-for-py/issues/120>`_ by allowing null confounder values)
      `#122 <https://github.com/DoubleML/doubleml-for-py/pull/122>`_
    - Clean up dev requirements and use dev requirements on github actions
      `#121 <https://github.com/DoubleML/doubleml-for-py/pull/121>`_
    - Other updates
      `#123 <https://github.com/DoubleML/doubleml-for-py/pull/123>`_

    **DoubleML 0.3.0**

    - Always use the same bootstrap algorithm independent of ``dml1`` vs ``dml2`` and consistent with docu and paper
      `#101 <https://github.com/DoubleML/doubleml-for-py/pull/101>`_ &
      `#102 <https://github.com/DoubleML/doubleml-for-py/pull/102>`_
    - Added an exception handling to assure that an IV variable is specified when using a PLIV or IIVM model
      `#107 <https://github.com/DoubleML/doubleml-for-py/pull/107>`_
    - Improve exception handling for externally provided sample splitting
      `#110 <https://github.com/DoubleML/doubleml-for-py/pull/110>`_
    - Minor update of the str representation of ``DoubleMLData`` objects
      `#112 <https://github.com/DoubleML/doubleml-for-py/pull/112>`_
    - Code refactorings and unit test extensions
      `#103 <https://github.com/DoubleML/doubleml-for-py/pull/103>`_,
      `#105 <https://github.com/DoubleML/doubleml-for-py/pull/105>`_,
      `#106 <https://github.com/DoubleML/doubleml-for-py/pull/106>`_,
      `#111 <https://github.com/DoubleML/doubleml-for-py/pull/111>`_ &
      `#113 <https://github.com/DoubleML/doubleml-for-py/pull/113>`_

    **DoubleML 0.2.2**

    - IIVM model: Added a subgroups option to adapt to cases with and without the subgroups of always-takers and
      never-takers (`#96 <https://github.com/DoubleML/doubleml-for-py/pull/96>`_).
    - Add checks for the intersections of ``y_col``, ``d_cols``, ``x_cols``, ``z_cols``
      (`#84 <https://github.com/DoubleML/doubleml-for-py/pull/84>`_,
      `#97 <https://github.com/DoubleML/doubleml-for-py/pull/97>`_).
      This also fixes `#83 <https://github.com/DoubleML/doubleml-for-py/pull/83>`_ (with intersection
      between ``x_cols`` and ``d_cols`` a column could have been added multiple times to the covariate matrix).
    - Added checks and exception handling for duplicate entries in ``d_cols``, ``x_cols`` or ``z_cols``
      (`#100 <https://github.com/DoubleML/doubleml-for-py/pull/100>`_).
    - Check the datatype of ``data`` when initializing ``DoubleMLData`` objects. Also check for duplicate column names
      (`#100 <https://github.com/DoubleML/doubleml-for-py/pull/100>`_).
    - Fix bug `#95 <https://github.com/DoubleML/doubleml-for-py/pull/95>`_
      in `#97 <https://github.com/DoubleML/doubleml-for-py/pull/97>`_: It occurred when ``x_cols`` where inferred via
      setdiff and ``y_col`` was a string with multiple characters.
    - We updated the citation info to refer to the arXiv paper
      (`#98 <https://github.com/DoubleML/doubleml-for-py/pull/98>`_):
      Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M. (2021), DoubleML - An Object-Oriented Implementation of
      Double Machine Learning in Python, `arXiv:2104.03220 <https://arxiv.org/abs/2104.03220>`_.

    **DoubleML 0.2.1**

    - Provide an option to store & export the first-stage predictions
      `#91 <https://github.com/DoubleML/doubleml-for-py/pull/91>`_
    - Added the package logo to the doc

    **DoubleML 0.2.0**

    - Major extensions of the unit test framework which result in a coverage >98% (a summary is given in
      `#82 <https://github.com/DoubleML/doubleml-for-py/pull/82>`_)
    - In the PLR one can now also specify classifiers for ``ml_m`` in case of a binary treatment variable with values 0
      and 1 (see `#86 <https://github.com/DoubleML/doubleml-for-py/pull/86>`_ for details)
    - The joint Python and R docu and user guide is now served to
      `https://docs.doubleml.org <https://docs.doubleml.org>`_ from a separate repo
      `https://github.com/DoubleML/doubleml-docs <https://github.com/DoubleML/doubleml-docs>`_
    - Generate and upload a unit test coverage report to codecov
      `https://app.codecov.io/gh/DoubleML/doubleml-for-py <https://app.codecov.io/gh/DoubleML/doubleml-for-py>`_
      `#76 <https://github.com/DoubleML/doubleml-for-py/pull/76>`_
    - Run lint checks with flake8 `#78 <https://github.com/DoubleML/doubleml-for-py/pull/78>`_, align code with PEP8
      standards `#79 <https://github.com/DoubleML/doubleml-for-py/pull/79>`_, activate code quality checks at codacy
      `#80 <https://github.com/DoubleML/doubleml-for-py/pull/80>`_
    - Refactoring (reduce code redundancy) of the code for tuning of the ML learners used for approximation the
      nuisance functions `#81 <https://github.com/DoubleML/doubleml-for-py/pull/81>`_
    - Minor updates, bug fixes and improvements of the exception handling
      (contained in `#82 <https://github.com/DoubleML/doubleml-for-py/pull/82>`_ &
      `#89 <https://github.com/DoubleML/doubleml-for-py/pull/89>`_)

    **DoubleML 0.1.2**

    - Fixed a compatibility issue with ``scikit-learn`` 0.24, which only affected some unit tests
      (`#70 <https://github.com/DoubleML/doubleml-for-py/issues/70>`_, `#71 <https://github.com/DoubleML/doubleml-for-py/pull/71>`_)
    - Added scheduled unit tests on github-action (three times a week) `#69 <https://github.com/DoubleML/doubleml-for-py/pull/69>`_
    - Split up estimation of nuisance functions and computation of score function components. Further introduced a
      private method ``_est_causal_pars_and_se()``, see `#72 <https://github.com/DoubleML/doubleml-for-py/pull/72>`_.
      This is needed for the DoubleML-Serverless project: https://github.com/DoubleML/doubleml-serverless.

    **DoubleML 0.1.1**

    - Bug fix in the drawing of bootstrap weights for the multiple treatment case
      `#66 <https://github.com/DoubleML/doubleml-for-py/pull/66>`_ (see also https://github.com/DoubleML/doubleml-for-r/pull/28)
    - Update install instructions as DoubleML is now listed on pypi
    - Prepare submission to conda-forge: Include LICENSE file in source distribution
    - Documentation is now served with HTTPS `https://docs.doubleml.org/ <https://docs.doubleml.org/>`_

    **DoubleML 0.1.0**

    - Initial release
    - Development at `https://github.com/DoubleML/doubleml-for-py <https://github.com/DoubleML/doubleml-for-py>`_
    - The Python package **DoubleML** provides an implementation of the double / debiased machine learning framework of
      `Chernozhukov et al. (2018) <https://doi.org/10.1111/ectj.12097)>`_.
    - Implements double machine learning for four different models:

        - Partially linear regression models (PLR) in class ``DoubleMLPLR``
        - Partially linear IV regression models (PLIV) in class ``DoubleMLPLIV``
        - Interactive regression models (IRM) in class ``DoubleMLIRM``
        - Interactive IV regression models (IIVM) in class ``DoubleMLIIVM``

    - All model classes are inherited from an abstract base class ``DoubleML`` where the key elements of double machine
      learning are implemented.

.. tabbed:: R

    **DoubleML 0.4.1**

    - Prevent usage of `glmnet` learner for unit testing as recommended by CRAN (failing tests on Solaris)
      `#137 <https://github.com/DoubleML/doubleml-for-r/pull/137>`_
    - Prepare for the upcoming release of `checkmate` which is not backward compatible with our unit tests
      `#134 <https://github.com/DoubleML/doubleml-for-r/pull/134>`_

    **DoubleML 0.4.0**

    - **Release highlight:** Clustered standard errors for double machine learning models
      `#119 <https://github.com/DoubleML/doubleml-for-r/pull/119>`_
    - Apply styler as described in the wiki (https://github.com/DoubleML/doubleml-for-r/wiki/Style-Guidelines) and add a
      corresponding CI on github actions `#120 <https://github.com/DoubleML/doubleml-for-r/pull/120>`_
      `#122 <https://github.com/DoubleML/doubleml-for-r/pull/122>`_
    - Other refactoring, bug fixes and documentation updates
      `#127 <https://github.com/DoubleML/doubleml-for-r/pull/127>`_
      `#129 <https://github.com/DoubleML/doubleml-for-r/pull/129>`_
      `#130 <https://github.com/DoubleML/doubleml-for-r/pull/130>`_
      `#131 <https://github.com/DoubleML/doubleml-for-r/pull/131>`_
      `#132 <https://github.com/DoubleML/doubleml-for-r/pull/132>`_
      `#133 <https://github.com/DoubleML/doubleml-for-r/pull/133>`_

    **DoubleML 0.3.1**

    - Initialize all numeric matrices, vectors and arrays with the correct data type by using ``NA_real_`` instead of
      ``NA`` and replace a ``print()`` call with ``cat()`` `#115 <https://github.com/DoubleML/doubleml-for-r/pull/115>`_

    **DoubleML 0.3.0**

    - Use active bindings in the R6 OOP implementation
      `#106 <https://github.com/DoubleML/doubleml-for-r/pull/106>`_ &
      `#93 <https://github.com/DoubleML/doubleml-for-r/pull/93>`_
    - Fix the aggregation formula for standard errors from repeated cross-fitting
      `#94 <https://github.com/DoubleML/doubleml-for-r/pull/94>`_ &
      `#95 <https://github.com/DoubleML/doubleml-for-r/pull/95>`_
    - Always use the same bootstrap algorithm independent of ``dml1`` vs ``dml2`` and consistent with docu and paper
      `#98 <https://github.com/DoubleML/doubleml-for-r/pull/98>`_ &
      `#99 <https://github.com/DoubleML/doubleml-for-r/pull/99>`_
    - Initialize predictions with NA and make sure that there are no misleading entries in the evaluated score
      functions `#96 <https://github.com/DoubleML/doubleml-for-r/pull/96>`_ &
      `#105 <https://github.com/DoubleML/doubleml-for-r/pull/105>`_
    - Avoid overriding learner parameters during tuning
      `#83 <https://github.com/DoubleML/doubleml-for-r/pull/83>`_ &
      `#84 <https://github.com/DoubleML/doubleml-for-r/pull/84>`_
    - Fixes in the exception handling and extension of the unit tests for the score function choice
      `#82 <https://github.com/DoubleML/doubleml-for-r/pull/82>`_
    - Prevent overwriting parameters from initialization when calling set_ml_nuisance_params
      `#87 <https://github.com/DoubleML/doubleml-for-r/pull/87>`_ &
      `#89 <https://github.com/DoubleML/doubleml-for-r/pull/89>`_
    - Major refactoring and cleanup and extension of the unit test framework
      `#101 <https://github.com/DoubleML/doubleml-for-r/pull/101>`_
    - Extension and reorganization of exception handling for ``DoubleMLData`` objects
      `#63 <https://github.com/DoubleML/doubleml-for-r/pull/63>`_ &
      `#90 <https://github.com/DoubleML/doubleml-for-r/pull/90>`_
    - Introduce style guide and clean up code
      `#80 <https://github.com/DoubleML/doubleml-for-r/pull/80>`_ &
      `#81 <https://github.com/DoubleML/doubleml-for-r/pull/81>`_
    - Adaption to be compatible with an API change in the next ``mlr3`` release
      `#103 <https://github.com/DoubleML/doubleml-for-r/pull/103>`_
    - Run unit tests with mlr3 in dev version on github actions
      `#104 <https://github.com/DoubleML/doubleml-for-r/pull/104>`_
    - Updated the citation info
      `#78 <https://github.com/DoubleML/doubleml-for-r/pull/78>`_,
      `#79 <https://github.com/DoubleML/doubleml-for-r/pull/79>`_ &
      `#86 <https://github.com/DoubleML/doubleml-for-r/pull/86>`_
    - Added a short version of and a reference to the arXiv paper as vignette
      `#110 <https://github.com/DoubleML/doubleml-for-r/pull/110>`_ &
      `#113 <https://github.com/DoubleML/doubleml-for-r/pull/113>`_
    - Prevent using the subclassed methods check_score and check_data when constructing DoubleML objects
      `#107 <https://github.com/DoubleML/doubleml-for-r/pull/107>`_
    - Other refactoring and minor adaptions
      `#91 <https://github.com/DoubleML/doubleml-for-r/pull/91>`_,
      `#92 <https://github.com/DoubleML/doubleml-for-r/pull/92>`_,
      `#102 <https://github.com/DoubleML/doubleml-for-r/pull/102>`_ &
      `#108 <https://github.com/DoubleML/doubleml-for-r/pull/108>`_

    **DoubleML 0.2.1**

    - Provide an option to store & export the first-stage predictions
      `#74 <https://github.com/DoubleML/doubleml-for-r/pull/74>`_
    - Reduce and refine messaging to the console during estimation
      `#72 <https://github.com/DoubleML/doubleml-for-r/pull/72>`_
    - Fix bug in IIVM model if the IV variable is not named ``z``
      `#75 <https://github.com/DoubleML/doubleml-for-r/pull/75>`_
    - Fix failing unit test `#71 <https://github.com/DoubleML/doubleml-for-r/pull/71>`_
    - Added the package logo to the doc

    **DoubleML 0.2.0**

    - In the PLR one can now also specify classifiers for ``ml_m`` in case of a binary treatment variable with values 0 and 1
    - Major refactoring of core-parts of the estimation and tuning of the ML estimators for the nuisance functions: All models now use central helper functions ``dml_cv_predict()`` and ``dml_tune()``
    - Extensions to the unit test framework to improve upon test coverage
    - Added unit test coverage via codecov: `https://app.codecov.io/gh/DoubleML/doubleml-for-r <https://app.codecov.io/gh/DoubleML/doubleml-for-r>`_
    - Minor docu updates and adaptions: `#58 <https://github.com/DoubleML/doubleml-for-r/pull/58>`_, `#61 <https://github.com/DoubleML/doubleml-for-r/pull/61>`_ & `#70 <https://github.com/DoubleML/doubleml-for-r/pull/70>`_

    **DoubleML 0.1.2**

    - Adapt calls to ``mlr3tuning`` due to a change in their API (since version 0.6.0): fixes `#51 <https://github.com/DoubleML/doubleml-for-r/issues/51>`_
    - Add ``bbotk`` to suggests: fixes R CMD check note `#47 <https://github.com/DoubleML/doubleml-for-r/issues/47>`_
    - Use ``doi{}`` command: fixes R CMD check note `#54 <https://github.com/DoubleML/doubleml-for-r/issues/54>`_
    - Minor docu updates as ``DoubleML`` is now available on CRAN

    **DoubleML 0.1.1**

    - First release to CRAN `https://cran.r-project.org/package=DoubleML <https://cran.r-project.org/package=DoubleML>`_
    - Clean up of imports
    - Continuous integration was extended by unit tests on github actions
      `https://github.com/DoubleML/doubleml-for-r/actions <https://github.com/DoubleML/doubleml-for-r/actions>`_

    **DoubleML 0.1.0**

    - Initial release
    - Development at `https://github.com/DoubleML/doubleml-for-r <https://github.com/DoubleML/doubleml-for-r>`_
    - The R package **DoubleML** provides an implementation of the double / debiased machine learning framework of
      `Chernozhukov et al. (2018) <https://doi.org/10.1111/ectj.12097)>`_.
    - Implements double machine learning for four different models:

        - Partially linear regression models (PLR) in class ``DoubleMLPLR``
        - Partially linear IV regression models (PLIV) in class ``DoubleMLPLIV``
        - Interactive regression models (IRM) in class ``DoubleMLIRM``
        - Interactive IV regression models (IIVM) in class ``DoubleMLIIVM``

    - All model classes are inherited from ``DoubleML`` where the key elements of double machine learning are
      implemented.

