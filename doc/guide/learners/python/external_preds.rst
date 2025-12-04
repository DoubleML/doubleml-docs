Since there might be cases where the user wants to use a learner that is not supported by :ref:`DoubleML <doubleml_package>`
or do some extensive hyperparameter tuning, it is possible to use external predictions for the nuisance functions.
Remark that this requires the user to take care of the cross-fitting procedure and learner evaluation.

To illustrate the use of external predictions, we work with the following example.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

      import numpy as np
      import doubleml as dml
      from doubleml.irm.datasets import make_irm_data
      from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

      np.random.seed(3333)
      data = make_irm_data(theta=0.5, n_obs=500, dim_x=10, return_type='DataFrame')
      obj_dml_data = dml.DoubleMLData(data, 'y', 'd')

      # DoubleML with interal predictions
      ml_g = RandomForestRegressor(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
      ml_m = RandomForestClassifier(n_estimators=100, max_features=10, max_depth=5, min_samples_leaf=2)
      dml_irm_obj = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
      dml_irm_obj.fit()
      print(dml_irm_obj.summary)

The :py:class:`doubleml.DoubleMLIRM` model class saves nuisance predictions in the ``predictions`` attribute as a nested dictionary.
To rely on external predictions, the user has to provide a nested dictionary, where the outer level keys correspond to the treatment
variable names and the inner level keys correspond to the nuisance learner names. Further the values have to be ``numpy`` arrays of shape
``(n_obs, n_rep)``. Here we generate an external predictions dictionary from the internal ``predictions`` attribute.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

      pred_dict = {"d": {
          "ml_g0": dml_irm_obj.predictions["ml_g0"][:, :, 0],
          "ml_g1": dml_irm_obj.predictions["ml_g1"][:, :, 0],
          "ml_m": dml_irm_obj.predictions["ml_m"][:, :, 0]
          }               
      }

The external predictions can be passed to the ``fit()`` method of the :py:class:`doubleml.DoubleML` class via the ``external_predictions`` argument.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python
      
      ml_g = dml.utils.DMLDummyRegressor()
      ml_m = dml.utils.DMLDummyClassifier()
      dml_irm_obj_ext = dml.DoubleMLIRM(obj_dml_data, ml_g, ml_m)
      dml_irm_obj_ext.fit(external_predictions=pred_dict)
      print(dml_irm_obj_ext.summary)

Both model have identical estimates. Remark that :py:class:`doubleml.DoubleML` class usually require learners for initialization.
With external predictions these learners are not used. The ``DMLDummyRegressor`` and ``DMLDummyClassifier`` are dummy learners which
are used to initialize the :py:class:`doubleml.DoubleML` class. Both dummy learners raise errors if specific methods are called to safeguard against
undesired behavior. Further, the :py:class:`doubleml.DoubleMLData` class requires features (e.g. via the ``x_cols`` argument) which are not used. 
This can be handled by adding a dummy column to the data.