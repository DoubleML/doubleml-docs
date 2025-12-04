Parameter tuning of learners for the nuisance functions of :ref:`DoubleML <doubleml_package>` models can be done via
the ``tune()`` method.
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

The hyperparameter-tuning is performed using either an exhaustive search over specified parameter values
implemented in :class:`sklearn.model_selection.GridSearchCV` or via a randomized search implemented in
:class:`sklearn.model_selection.RandomizedSearchCV`.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python
      :okwarning:

      import doubleml as dml
      from sklearn.linear_model import Lasso

      ml_l = Lasso()
      ml_m = Lasso()
      dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_l, ml_m)
      par_grids = {'ml_l': {'alpha': np.arange(0.05, 1., 0.1)},
                    'ml_m': {'alpha': np.arange(0.05, 1., 0.1)}}
      dml_plr_obj.tune(par_grids, search_mode='grid_search');
      print(dml_plr_obj.params)
      print(dml_plr_obj.fit().summary)

      np.random.seed(1234)
      par_grids = {'ml_l': {'alpha': np.arange(0.05, 1., 0.01)},
                    'ml_m': {'alpha': np.arange(0.05, 1., 0.01)}}
      dml_plr_obj.tune(par_grids, search_mode='randomized_search', n_iter_randomized_search=20);
      print(dml_plr_obj.params)
      print(dml_plr_obj.fit().summary)

Hyperparameter tuning can also be done with more sophisticated methods, like for example an iterative fitting along
a regularization path implemented in :py:class:`sklearn.linear_model.LassoCV`.
In this case the tuning should be done externally and the parameters can then be set via the
``set_ml_nuisance_params()`` method.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

      import doubleml as dml
      from sklearn.linear_model import LassoCV

      np.random.seed(1234)
      ml_l_tune = LassoCV().fit(dml_data.x, dml_data.y)
      ml_m_tune = LassoCV().fit(dml_data.x, dml_data.d)

      ml_l = Lasso()
      ml_m = Lasso()
      dml_plr_obj = dml.DoubleMLPLR(dml_data, ml_l, ml_m)
      dml_plr_obj.set_ml_nuisance_params('ml_l', 'd', {'alpha': ml_l_tune.alpha_});
      dml_plr_obj.set_ml_nuisance_params('ml_m', 'd', {'alpha': ml_m_tune.alpha_});
      print(dml_plr_obj.params)
      print(dml_plr_obj.fit().summary)
