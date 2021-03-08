:parenttoc: True

Release notes
=============

.. tabbed:: Python

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
      (`#76 <https://github.com/DoubleML/doubleml-for-py/pull/76>`_)
    - Run lint checks with flake8 (`#78 <https://github.com/DoubleML/doubleml-for-py/pull/78>`_), align code with PEP8
      standards (`#79 <https://github.com/DoubleML/doubleml-for-py/pull/79>`_), activate code quality checks at codacy
      (`#80 <https://github.com/DoubleML/doubleml-for-py/pull/80>`_)
    - Refactoring (reduce code redundancy) of the code for tuning of the ML learners used for approximation the
      nuisance functions (`#81 <https://github.com/DoubleML/doubleml-for-py/pull/81>`_)
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

