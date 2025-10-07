The ``DoubleMLDIDData`` class tailors :ref:`DoubleMLData <dml_data>` to difference-in-differences
applications. It handles both panel settings and repeated cross-sections by tracking an optional time indicator.

Key arguments
"""""""""""""

* ``t_col``: column containing the time variable for repeated cross-sections. It
  must be unique from ``y_col``, ``d_cols``, ``x_cols``, ``z_cols`` and
  ``cluster_cols``.
* ``cluster_cols``: optional cluster identifiers inherited from
  :class:`doubleml.DoubleMLData`.
* ``force_all_d_finite``: controls how missing or infinite treatment values are
  handled. For standard DiD applications it defaults to ``True``.

``DoubleMLDIDData`` exposes additional helpers such as the ``t`` property and
an extended ``from_arrays`` constructor that accepts the ``t`` array (and
``cluster_vars``) alongside the standard covariates.

Example usage
"""""""""""""

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import doubleml as dml
            from doubleml.did.datasets import make_did_SZ2020

            df = make_did_SZ2020(n_obs=500, return_type="DataFrame")
            print(df.head())
            dml_data = dml.DoubleMLDIDData(
                df,
                y_col="y",
                d_cols="d",
            )

            # from arrays
            x, y, d, t = make_did_SZ2020(n_obs=200, return_type="array")
            dml_data_arrays = dml.DoubleMLDIDData.from_arrays(x, y, d)
            print(dml_data)

