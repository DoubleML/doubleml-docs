Parameter tuning of learners for the nuisance functions of :ref:`DoubleML <doubleml_package>` models can be done via
the ``tune_ml_models()`` method.
To illustrate the parameter tuning, we generate data from a sparse partially linear regression model.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

      import doubleml as dml
      import numpy as np

      np.random.seed(3141)
      n_obs = 200
      n_vars = 200
      theta = 3
      X = np.random.normal(size=(n_obs, n_vars))
      d = np.dot(X[:, :3], np.array([5, 5, 5])) + np.random.standard_normal(size=(n_obs,))
      y = theta * d + np.dot(X[:, :3], np.array([5, 5, 5])) + np.random.standard_normal(size=(n_obs,))
      dml_data = dml.DoubleMLData.from_arrays(X, y, d)

The hyperparameter-tuning is performed using `Optuna <https://optuna.org/#key_features>`_ as backend. Here, we illustrate
the tuning via defining a search space for the nuisance function learners over ``100`` trials. The most important input
argument is the hyperparameter space via a dictionary of functions. This search space will internally transformed into a
suitable ``objective(trial)`` function for `Optuna <https://optuna.org/#key_features>`_.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python
      :okwarning:

      import doubleml as dml
      from sklearn.linear_model import Lasso
      import optuna

      ml_l = Lasso()
      ml_m = Lasso()
      dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_l, ml_m)

      def ml_l_params(trial):
          return {'alpha': trial.suggest_float('alpha', 0.05, 1.0)}

      def ml_m_params(trial):
          return {'alpha': trial.suggest_float('alpha', 0.05, 1.0)}

      param_space = {'ml_l': ml_l_params, 'ml_m': ml_m_params}
      optuna_settings = {'n_trials': 100, 'verbosity': optuna.logging.WARNING}

      dml_plr_obj.tune_ml_models(ml_param_space=param_space, optuna_settings=optuna_settings)
      
      print(dml_plr_obj.params)
      print(dml_plr_obj.fit().summary)

A more detailed description of hyperparameter-tuning possibilities can be found in the :ref:`Example Gallery <examplegallery>`.