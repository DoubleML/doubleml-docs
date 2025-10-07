The ``DoubleMLSSMData`` class covers the sample selection model backend. 
It extends :ref:`DoubleMLData <dml_data>` with a dedicated selection indicator and inherits support for clustered data.

Key arguments
"""""""""""""

* ``s_col``: column containing the selection indicator.
* ``cluster_cols``: optional cluster identifiers.
* ``from_arrays``: expects an additional ``s`` array together with ``x``, ``y`` and ``d``.

The object exposes the ``s`` property and keeps the selection indicator
separate from covariates and treatment variables.

Example usage
"""""""""""""

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            from doubleml.irm.datasets import make_ssm_data

            df = make_ssm_data(n_obs=500, return_type="DataFrame")
            dml_data = dml.DoubleMLSSMData(
                df,
                y_col="y",
                d_cols="d",
                s_col="s"
            )

            x, y, d, _, s = make_ssm_data(n_obs=200, return_type="array")
            dml_data_arrays = dml.DoubleMLSSMData.from_arrays(x, y, d, s=s)
            print(dml_data)

