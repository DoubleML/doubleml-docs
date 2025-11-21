The ``DoubleMLRDDData`` class specialises :ref:`DoubleMLData <dml_data>` for
regression discontinuity designs. In addition to the standard causal roles it
tracks a mandatory running variable.

Key arguments
"""""""""""""

* ``score_col``: column with the running/score variable.
* ``cluster_cols``: optional cluster identifiers inherited from the base data
  class.
* ``from_arrays``: expects an additional ``score`` array alongside ``x``, ``y``
  and ``d``.

``DoubleMLRDDData`` ensures that the running variable is kept separate from the
other feature sets and exposes the ``score`` property for convenient access.

Example usage
"""""""""""""

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

          import doubleml as dml
          from doubleml.rdd.datasets import make_simple_rdd_data

          dict_rdd = make_simple_rdd_data(n_obs=500, return_type="DataFrame")
          dml_data = dml.DoubleMLRDDData.from_arrays(
            x=dict_rdd["X"], 
            y=dict_rdd["Y"], 
            d=dict_rdd["D"], 
            score=dict_rdd["score"]
            )

          print(dml_data)

