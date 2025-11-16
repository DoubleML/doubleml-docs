The minimum requirement for a learner to be used for nuisance models in the :ref:`DoubleML <doubleml_package>` package is

* The implementation as a learner for regression or classification in the `mlr3 <https://mlr3.mlr-org.com/>`_ package
  or its extension packages `mlr3learners <https://mlr3learners.mlr-org.com/>`_ and
  `mlr3extralearners <https://mlr3extralearners.mlr-org.com/>`_ . A guide on how to add a learner is provided in the
  `chapter on extending learners in the mlr3 book <https://mlr3book.mlr-org.com/chapters/chapter10/advanced_technical_aspects_of_mlr3.html#sec-extending>`_ .
* The `mlr3 <https://mlr3.mlr-org.com/>`_ package makes sure that the learners satisfy some core functionalities.
  To specify a specific learner in :ref:`DoubleML <doubleml_package>` users can pass objects of the class
  `Learner <https://mlr3.mlr-org.com/reference/Learner.html>`_. A fast way to construct these objects is to use the
  `mlr3 <https://mlr3.mlr-org.com/>`_  function `lrn() <https://mlr3.mlr-org.com/reference/mlr_sugar.html>`_.
  An introduction to learners in `mlr3 <https://mlr3.mlr-org.com/>`_  is provided in the `chapter on learners of the mlr3 book <https://mlr3book.mlr-org.com/chapters/chapter2/data_and_basic_modeling.html#sec-learners>`_.
* It is also possible to pass learners that have been constructed from a pipeline with the `mlr3pipelines <https://mlr3pipelines.mlr-org.com/>`_
  package.
* The models `DoubleML::DoubleMLIRM <https://docs.doubleml.org/r/stable/reference/DoubleMLIRM.html>`_ and
  `DoubleML::DoubleMLIIVM <https://docs.doubleml.org/r/stable/reference/DoubleMLIIVM.html>`_ require classifiers.
  Users can also specify classifiers in the `DoubleML::DoubleMLPLR <https://docs.doubleml.org/r/stable/reference/DoubleMLPLR.html>`_
  in cases with binary treatment variables.
* Hyperparameters of learners can either be set at instantiation in `mlr3 <https://mlr3.mlr-org.com/>`_ or after
  instantiation using the ``set_ml_nuisance_params()`` method.


An interactive list of provided learners in the `mlr3 <https://mlr3.mlr-org.com/>`_ and extension packages can be found on the
`website of the mlr3extralearners package <https://mlr3extralearners.mlr-org.com/articles/learners/list_learners.html>`_.
