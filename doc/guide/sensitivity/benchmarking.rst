The input parameters for the sensitivity analysis are quite hard to interpret (depending on the model). Consequently it is challenging to come up with reasonable bounds 
for the confounding strength ``cf_y`` and ``cf_d`` (and ``rho``). To get a grasp on the magnitude of the bounds a popular approach is to rely on observed confounders
to obtain an informed guess on the strength of possibly unobserved confounders.

The underlying principle is relatively simple. If we have an observed confounder :math:`X_1`, we are able to emulate omitted confounding by purposely omitting
:math:`X_1` and refitting the whole model. This enables us to compare the "long" and "short" form with and without omitted confounding.
Considering the ``sensitivity_params`` of both models one can estimate the corresponding strength of confounding ``cf_y`` and ``cf_d`` (and ``rho``).

.. note::

 - The benchmarking can also be done with a set of benchmarking variables (e.g. :math:`X_1, X_2, X_3`), which tries to emulate the effect of multiple unobserved confounders.
 - The approach is quite computationally demanding, as the short model that omits the benchmark variables has to be fitted.

The ``sensitivity_benchmark()`` method implements this approach. 
The method just requires a set of valid covariates, the ``benchmarking_set``, to compute the benchmark. The benchmark variables have to be a subset of the covariates used in the main analysis.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            
            dml_plr_obj.sensitivity_benchmark(benchmarking_set=["X1"])

The method returns a :py:class:`pandas.DataFrame`, containing the benchmarked values for ``cf_y``, ``cf_d``,  ``rho`` and the change in the estimates
``delta_theta``.

.. note::

 -  The benchmarking results should be used to get an idea of the magnitude/validity of proposed confounding strength of the omitted confounders. Whether these values are close to the real confounding, depends entirely on the 
    setting and choice of the benchmarking variables. A good benchmarking set has a strong justification which refers to the omitted confounders.
 -  If the benchmarking variables are only weak confounders, the estimates of ``rho`` can be slightly unstable (due to small denominators).

The implementation is based on `Chernozhukov et al. (2022) <https://www.nber.org/papers/w30302>`_ Appendix D and corresponds to a generalization of 
the benchmarking process in the `Sensemakr package <https://github.com/carloscinelli/sensemakr>`_ for regression models to the use with double machine learning.
For an introduction to Sensemakr see `Cinelli and Hazlett (2020) <https://doi.org/10.1111/rssb.12348>`_ and the `Sensemakr introduction <https://cran.r-project.org/web/packages/sensemakr/vignettes/sensemakr.html>`_.

The benchmarked estimates are the following:

Let the subscript :math:`short`, denote the "short" form of the model, where the benchmarking variables are omitted.

- :math:`\hat{\sigma}^2_{short}` denotes the variance of the outcome regression in the "short" form.
- :math:`\hat{\nu}^2_{short}` denotes the second moment of the Riesz representer in the "short" form.

Both parameters are contained in the ``sensitivity_params`` of the "short" form.
This enables the following estimation of the nonparametric :math:`R^2`'s of the outcome regression

- :math:`\hat{R}^2:= 1 - \frac{\hat{\sigma}^2}{\textrm{Var}(Y)}`
- :math:`\hat{R}^2_{short}:= 1 - \frac{\hat{\sigma}^2_{short}}{\textrm{Var}(Y)}`

and the correlation ratio of the estimated Riesz representations

.. math::

    \hat{R}^2_{\alpha}:= \frac{\hat{\nu}^2_{short}}{\hat{\nu}^2}.

The benchmarked estimates are then defined as

- ``cf_y``:math:`:=\frac{\hat{R}^2 - \hat{R}^2_{short}}{1 - \hat{R}^2}`  measures the proportion of residual variance in the outcome :math:`Y` explained by adding the purposely omitted ``benchmarking_set``

- ``cf_d``:math:`:=\frac{1 - \hat{R}^2_{\alpha}}{\hat{R}^2_{\alpha}}` measures the proportional gain in variation that the ``benchmarking_set`` creates in the Riesz representer

Further, the degree of adversity :math:`\rho` can be estimated via

.. math::

    \hat{\rho} := \frac{\hat{\theta}_{short} - \hat{\theta}}{ \sqrt{(\hat{\sigma}^2_{short} - \hat{\sigma}^2)(\hat{\nu}^2 - \hat{\nu}^2_{short})}}.


For a more detailed description, see `Chernozhukov et al. (2022) <https://www.nber.org/papers/w30302>`_ Appendix D.

.. note::
    - As benchmarking requires the estimation of a seperate model, the use with external predictions is generally not possible, without supplying further predictions.