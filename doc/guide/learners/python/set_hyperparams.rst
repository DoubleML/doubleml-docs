The learners are set during initialization of the :ref:`DoubleML <doubleml_package>` model classes
:py:class:`doubleml.DoubleMLPLR`, :py:class:`doubleml.DoubleMLPLIV`,
:py:class:`doubleml.DoubleMLIRM` and :py:class:`doubleml.DoubleMLIIVM`.
Lets simulate some data and consider the partially linear regression model.
We need to specify learners for the nuisance functions :math:`g_0(X) = E[Y|X]` and :math:`m_0(X) = E[D|X]`,
for example :py:class:`sklearn.ensemble.RandomForestRegressor`.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

      import doubleml as dml
      from doubleml.plm.datasets import make_plr_CCDDHNR2018
      from sklearn.ensemble import RandomForestRegressor

      np.random.seed(1234)
      ml_l = RandomForestRegressor()
      ml_m = RandomForestRegressor()
      data = make_plr_CCDDHNR2018(alpha=0.5, return_type='DataFrame')
      obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
      dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m)
      dml_plr_obj.fit().summary

Without further specification of the hyperparameters, default values are used. To set hyperparameters:

* We can also use pre-parametrized learners, like ``RandomForestRegressor(n_estimators=10)``.
* Alternatively, hyperparameters can also be set after initialization via the method
  ``set_ml_nuisance_params(learner, treat_var, params)``


.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

        np.random.seed(1234)
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data,
                                      RandomForestRegressor(n_estimators=10),
                                      RandomForestRegressor())
        print(dml_plr_obj.fit().summary)

        np.random.seed(1234)
        dml_plr_obj = dml.DoubleMLPLR(obj_dml_data,
                                      RandomForestRegressor(),
                                      RandomForestRegressor())
        dml_plr_obj.set_ml_nuisance_params('ml_l', 'd', {'n_estimators': 10});
        print(dml_plr_obj.fit().summary)

Setting treatment-variable-specific or fold-specific hyperparameters:

* In the multiple-treatment case, the method ``set_ml_nuisance_params(learner, treat_var, params)`` can be used to set
  different hyperparameters for different treatment variables.
* The method ``set_ml_nuisance_params(learner, treat_var, params)`` accepts dicts and lists for ``params``.
  A dict should be provided if for each fold the same hyperparameters should be used.
  Fold-specific parameters are supported. To do so,  provide a nested list as ``params``, where the outer list is of
  length ``n_rep`` and the inner list of length ``n_folds``.