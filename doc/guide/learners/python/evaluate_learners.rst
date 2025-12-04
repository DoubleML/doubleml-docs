To compare different learners it is possible to evaluate the out-of-sample performance of each learner. The ``summary``
already displays either the root-mean-squared error (for regressions) or log-loss (for classifications) for each learner
and each corresponding repetition of cross-fitting (``n_rep`` argument).

To illustrate the parameter tuning, we work with the following example.

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
        dml_plr_obj.fit()
        print(dml_plr_obj)

The loss of each learner are also stored in the ``nuisance_loss`` attribute.
Further, the ``evaluate_learners()`` method allows to evalute customized evaluation metrics as e.g. the mean absolute error. 
The default option is still the root-mean-squared error for evaluation.

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

        print(dml_plr_obj.nuisance_loss)
        print(dml_plr_obj.evaluate_learners())

To evaluate a customized metric one has to define a ``callable``. For some models (e.g. the IRM model) it is important that
the metric can handle ``nan`` values as not all target values are known.   

.. tab-set::

  .. tab-item:: Python
    :sync: py

    .. ipython:: python

        from sklearn.metrics import mean_absolute_error

        def mae(y_true, y_pred):
            subset = np.logical_not(np.isnan(y_true))
            return mean_absolute_error(y_true[subset], y_pred[subset])

        dml_plr_obj.evaluate_learners(learners=['ml_l'], metric=mae)

A more detailed notebook on the choice of learners is available in the :ref:`example gallery <examplegallery>`.