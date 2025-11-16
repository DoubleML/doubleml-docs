The minimum requirement for a learner to be used for nuisance models in the :ref:`DoubleML <doubleml_package>`
package is

* The implementation of a ``fit()`` and ``predict()`` method.
  Some models, like :py:class:`doubleml.DoubleMLIRM` and :py:class:`doubleml.DoubleMLIIVM` require classifiers.
* In case of classifiers, the learner needs to come with a ``predict_proba()`` instead of, or in addition to, a
  ``predict()`` method, see for example :py:meth:`sklearn.ensemble.RandomForestClassifier.predict_proba`.
* In order to be able to use the ``set_ml_nuisance_params()`` method of :ref:`DoubleML <doubleml_package>` classes the
  learner additionally needs to come with a ``set_params()`` method,
  see for example :py:meth:`sklearn.ensemble.RandomForestRegressor.set_params`.
* We further rely on the function :py:func:`sklearn.base.clone` which adds the requirement of a ``get_params()``
  method for a learner in order to be used for nuisance models of :ref:`DoubleML <doubleml_package>` model classes.

Most learners from `scikit-learn <https://scikit-learn.org/>`_ satisfy all these minimum requirements.
