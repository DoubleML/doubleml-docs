.. _doubleml_package:

DoubleML
========

.. |build| image:: https://github.com/DoubleML/doubleml-for-py/workflows/build/badge.svg
.. _build: https://github.com/DoubleML/doubleml-for-py/actions?query=workflow%3Abuild

.. |PyPi| image:: https://badge.fury.io/py/DoubleML.svg
.. _PyPi: https://badge.fury.io/py/DoubleML

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue
.. _PythonVersion: https://www.python.org/

The Python and R package **DoubleML** provide an implementation of the double / debiased machine learning framework of
`Chernozhukov et al. (2018) <https://doi.org/10.1111/ectj.12097>`_.
The Python package is built on top of `scikit-learn <https://scikit-learn.org/>`_ (Pedregosa et al., 2011)
and the R package on top of `mlr3 <https://mlr3.mlr-org.com/>`_ and the `mlr3
ecosystem <https://github.com/mlr-org/mlr3/wiki/Extension-Packages>`_ (Lang et al., 2019).


.. panels::
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
    :card: text-center
    :img-top-cls: pl-5 pr-5 pt-5 pb-5
    :header: font-weight-bold border-0 h4
    :footer: border-0

    ---
    :img-top: _static/gettingstarted.png

    Getting started
    ^^^^^^^^^^^^^^^

    New to **DoubleML**? Then check out how to get started!

    +++

    .. link-button:: intro/intro
        :type: ref
        :text: To the getting started guide
        :classes: btn-block btn-dark stretched-link btn-sm

    ---
    :img-top: _static/userguide.png

    User guide
    ^^^^^^^^^^

    Want to learn everything about **DoubleML**? Then you should visit our extensive user guide with detailed explanations and further references.

    +++

    .. link-button:: guide/guide
        :type: ref
        :text: To the user guide
        :classes: btn-block btn-dark stretched-link btn-sm

    ---
    :img-top: _static/workflow.png

    Workflow
    ^^^^^^^^^^^^^^^^^

    The **DoubleML** workflow demonstrates the typical steps to consider when using **DoubleML** in applied analysis.

    +++

    .. link-button:: workflow/workflow
        :type: ref
        :text: To the DoubleML workflow
        :classes: btn-block btn-dark stretched-link btn-sm

    ---
    :img-top: _static/pythonapi.png

    Python API
    ^^^^^^^^^^

    The Python API documentation.

    +++

    .. link-button:: api/api
        :type: ref
        :text: To the Python API
        :classes: btn-block btn-dark stretched-link btn-sm

    ---
    :img-top: _static/rapi.png

    R API
    ^^^^^

    The R API documentation.

    +++

    .. link-button:: https://docs.doubleml.org/r/stable/
        :type: url
        :text: To the R API
        :classes: btn-block btn-dark stretched-link btn-sm

    ---
    :img-top: _static/examplegallery.png

    Example gallery
    ^^^^^^^^^^^^^^^

    A gallery with examples demonstrating the functionalities of **DoubleML**.

    +++

    .. link-button:: examples/index
        :type: ref
        :text: To the example gallery
        :classes: btn-block btn-dark stretched-link btn-sm


.. toctree::
   :hidden:

   self

.. toctree::
   :hidden:

    Install <intro/install>
    Getting started <intro/intro>
    User guide <guide/guide>
    Workflow <workflow/workflow>
    Python API <api/api>
    R API <https://docs.doubleml.org/r/stable/>
    Examples <examples/index>
    Release notes <release/release>

Main Features
-------------

Double / debiased machine learning `Chernozhukov et al. (2018) <https://doi.org/10.1111/ectj.12097>`_ for

- Partially linear regression models (PLR)
- Partially linear IV regression models (PLIV)
- Interactive regression models (IRM)
- Interactive IV regression models (IIVM)

The object-oriented implementation of DoubleML is very flexible.
The model classes `DoubleMLPLR`, `DoubleMLPLIV`, `DoubleMLIRM` and `DoubleIIVM` implement the estimation of the nuisance
functions via machine learning methods and the computation of the Neyman orthogonal score function.
All other functionalities are implemented in the abstract base class `DoubleML`.
In particular functionalities to estimate double machine learning models and to perform statistical inference via the
methods `fit`, `bootstrap`, `confint`, `p_adjust` and `tune`.
This object-oriented implementation allows a high flexibility for the model specification in terms of ...

- ... the machine learning methods for estimation of the nuisance functions,
- ... the resampling schemes,
- ... the double machine learning algorithm,
- ... the Neyman orthogonal score functions,
- ...

It further can be readily extended with regards to

- ... new model classes that come with Neyman orthogonal score functions being linear in the target parameter,
- ... alternative score functions via callables,
- ... alternative resampling schemes,
- ...

.. image:: oop.svg
    :width: 100%
    :alt: OOP structure of the DoubleML package

Source code and maintenance
---------------------------

Documentation and website: `https://docs.doubleml.org/ <https://docs.doubleml.org/>`_

DoubleML is currently maintained by
`@MalteKurz <https://github.com/MalteKurz>`_ and
`@PhilippBach <https://github.com/PhilippBach>`_.

The source code is available on GitHub: `Python source <https://github.com/DoubleML/doubleml-for-py>`_ and
`R source <https://github.com/DoubleML/doubleml-for-r>`_.

Bugs can be reported to the issue trackers:
`https://github.com/DoubleML/doubleml-for-py/issues <https://github.com/DoubleML/doubleml-for-py/issues>`_
and `https://github.com/DoubleML/doubleml-for-r/issues <https://github.com/DoubleML/doubleml-for-r/issues>`_.


Citation
--------

If you use the DoubleML package a citation is highly appreciated:

Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M. (2021),
DoubleML - An Object-Oriented Implementation of Double Machine Learning in Python,
arXiv:`2104.03220 <https://arxiv.org/abs/2104.03220>`_.


Bach, P., Chernozhukov, V., Kurz, M. S., and Spindler, M. (2021),
DoubleML - An Object-Oriented Implementation of Double Machine Learning in R,
arXiv:`2103.09603 <https://arxiv.org/abs/2103.09603>`_.

Bibtex-entries:

.. code-block:: TeX

    @misc{DoubleML2021Python,
      title={{DoubleML} -- {A}n Object-Oriented Implementation of Double Machine Learning in {P}ython},
      author={Philipp Bach and Victor Chernozhukov and Malte S. Kurz and Martin Spindler},
      year={2021},
      eprint={2104.03220},
      archivePrefix={arXiv},
      primaryClass={stat.ML},
      note={arXiv:\href{https://arxiv.org/abs/2104.03220}{2104.03220} [stat.ML]}
    }

.. code-block:: TeX

    @misc{DoubleML2021R,
      title={{DoubleML} -- {A}n Object-Oriented Implementation of Double Machine Learning in {R}},
      author={P. Bach and V. Chernozhukov and M. S. Kurz and M. Spindler},
      year={2021},
      eprint={2103.09603},
      archivePrefix={arXiv},
      primaryClass={stat.ML},
      note={arXiv:\href{https://arxiv.org/abs/2103.09603}{2103.09603} [stat.ML]}
    }

References
----------

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W. and Robins, J. (2018),
Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal, 21: C1-C68, doi:`10.1111/ectj.12097 <https://doi.org/10.1111/ectj.12097>`_.

Lang, M., Binder, M., Richter, J., Schratz, P., Pfisterer, F., Coors, S., Au, Q., Casalicchio, G., Kotthoff, L. and Bischl, B. (2019),
mlr3: A modern object-oriented machine learing framework in R. Journal of Open Source Software, doi:`10.21105/joss.01903 <https://10.21105/joss.01903>`_.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M. and Duchesnay, E. (2011),
Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12: 2825--2830, `https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html <https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html>`_.

.. panels::
    :column: col-lg

    .. dropdown:: Main References
        :open:
        :container: + reference-dropdown
        :title: bg-primary text-white text-center font-weight-bold

        Main References https://doi.org/10.1111/ectj.12097

    .. dropdown:: Software for Double Machine Learning
        :title: bg-primary text-white text-center font-weight-bold
        :body: bg-light text-left font-italic list-group

        - DoubleML in Python: https://arxiv.org/abs/2104.03220
        - DoubleML in R: https://arxiv.org/abs/2103.09603
        - DoubleMLServerless: https://dl.acm.org/doi/10.1145/3447545.3451181
        - EconML https://github.com/microsoft/EconML
        - Szitas J (2019). “postDoubleR: Post Double Selection with Double Machine Learning.” https://CRAN.R-project.org/package=postDoubleR
        - Knaus MC (2020). “Double Machine Learning based Program Evaluation under Unconfoundedness.” arXiv preprint arXiv:2003.03191. URL https://github.com/MCKnaus/causalDML
        - Knaus MC (2021). “A Double Machine Learning Approach to Estimate the Effects of Musical Practice on Student’s Skills.” Journal of the Royal Statistical Society A, 184(1), 282–300. URL https://github.com/MCKnaus/dmlmt.

    .. dropdown:: Double Machine Learning Models and Methodological Extensions
        :title: bg-primary text-white text-center font-weight-bold

        - Neng-Chieh Chang |br|
          **Double/debiased machine learning for difference-in-differences models** |br|
          The Econometrics Journal, Volume 23, Issue 2, May 2020, Pages 177–191 |br|
          `[link] <https://academic.oup.com/ectj/article/23/2/177/5722119>`_
        - Harold D. Chiang, Kengo Kato, Yukun Ma, Yuya Sasaki |br|
          **Multiway Cluster Robust Double/Debiased Machine Learning** |br|
          Journal of Business & Economic Statistics, 2021/03/03 |br|
          `[link] <https://www.tandfonline.com/doi/abs/10.1080/07350015.2021.1895815>`_
        - reinforcement learning 1: `[link] <https://jmlr.org/papers/volume21/19-827/19-827.pdf>`_
        - reinforcement learning 2: `[link] <https://arxiv.org/abs/2002.08536>`_
        - Orthogonal Machine Learning: Power and Limitations `[link] <https://arxiv.org/abs/1711.00342>`_
        - Heterogenous Treatment Effects: `[link] <https://arxiv.org/abs/1712.09988>`_

    .. dropdown:: Debiased Sparsity-Based Inference / Theoretical Foundations
        :title: bg-primary text-white text-center font-weight-bold

        - Belloni et al. 2011, 2014b; Javanmard and Montanari 2014; van de Geer et al. 2014; Zhang and Zhang 2014; Chernozhukov et al. 2015b --> See Remark 4 in https://arxiv.org/pdf/2103.09603.pdf
        - Neyman (1959) --> also from https://arxiv.org/pdf/2103.09603.pdf


.. panels::
    :column: col-lg-12
    :header: text-center text-white
    :card: text-center text-white
    :body: text-center text-white

    **Want to add or update a reference in the literature overview?**
    ^^^

    .. link-button:: intro/intro
        :type: ref
        :text: Edit this file and propose the change via a pull request
        :classes: btn-block btn-dark stretched-link btn-sm pr-button fw-bold

.. raw:: html

    <script>
    // add the GitHub Mark icon to the pull request button
        var pr_button = document.getElementsByClassName('pr-button')[0]
        var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" style="padding-left: 7px" width="20" height="16"><path fill="white" fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>';
        pr_button.innerHTML += svg
    </script>

.. |br| raw:: html

    <br/>