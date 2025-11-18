The :ref:`plr-model` will be used as an example

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python

            import numpy as np
            import doubleml as dml
            from doubleml.plm.datasets import make_plr_CCDDHNR2018
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.base import clone

            learner = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            ml_l = clone(learner)
            ml_m = clone(learner)
            np.random.seed(1111)
            data = make_plr_CCDDHNR2018(alpha=0.5, n_obs=500, dim_x=20, return_type='DataFrame')
            obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
            dml_plr_obj = dml.DoubleMLPLR(obj_dml_data, ml_l, ml_m)

If the sensitivity analysis is implemented (see :ref:`sensitivity_models`), the corresponding sensitivity elements are estimated
automatically by calling the ``fit()`` method. In most cases these elements are based on the following plug-in estimators

.. math::

    \hat{\sigma}^2 &:= \mathbb{E}_n[(Y-\hat{g}(W))^2]

    \hat{\nu}^2 &:= \mathbb{E}_n[2m(W,\hat{\alpha}) -  \hat{\alpha}(W)^2]

where :math:`\hat{g}(W)` and :math:`\hat{\alpha}(W)` denote the cross-fitted predictions of the outcome regression and the Riesz
representer (both are model specific, see :ref:`sensitivity_models`). Further, the corresponding scores are defined as

.. math::

    \psi_{\sigma^2}(W, \hat{\sigma}^2, g) &:= (Y-\hat{g}(W))^2 - \hat{\sigma}^2\\
    \psi_{\nu^2}(W, \hat{\nu}^2, \alpha) &:= 2m(W,\hat{\alpha}) - \hat{\alpha}(W)^2 - \hat{\nu}^2.

After the ``fit()`` call, the sensitivity elements are stored in a dictionary and can be accessed via the ``sensitivity_elements`` property.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            
            dml_plr_obj.fit()
            dml_plr_obj.sensitivity_elements.keys()

Each value is a :math:`3`-dimensional array, with the variances being of form ``(1, n_rep, n_coefs)`` and the scores of form ``(n_obs, n_rep, n_coefs)``.
The ``sensitivity_analysis()`` method then computes the upper and lower bounds for the estimate, based on the sensitivity parameters
``cf_y``, ``cf_d`` and ``rho`` (default is ``rho=1.0`` to account for adversarial confounding). Additionally, one-sided confidence bounds are computed 
based on a supplied significance level (default ``level=0.95``). 
The results are summarized as a formatted string in the ``sensitivity_summary``

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            
            dml_plr_obj.sensitivity_analysis(cf_y=0.03, cf_d=0.03, rho=1.0, level=0.95)
            print(dml_plr_obj.sensitivity_summary)

or can be directly accessed via the ``sensitivity_params`` property.

.. tab-set::

    .. tab-item:: Python
        :sync: py

        .. ipython:: python
            
            dml_plr_obj.sensitivity_params

The bounds are saved as a nested dictionary, where the keys ``'theta'``
denote the bounds on the parameter :math:`\hat{\theta}_{\pm}`, ``'se'`` denotes the corresponding standard error and ``'ci'`` denotes the lower and upper
confidence bounds for :math:`\hat{\theta}_{\pm}`. Each of the keys refers to a dictionary with keys ``'lower'`` and ``'upper'``
which refer to the lower or upper bound, e.g. ``sensitivity_params['theta']['lower']`` refers to the lower bound :math:`\hat{\theta}_{-}` of the estimated cofficient .

Further, the sensitivity analysis has an input parameter ``theta`` (with default ``theta=0.0``), which refers to the null hypothesis used for each coefficient.
This null hypothesis is used to calculate the robustness values as displayed in the ``sensitivity_params``.

The robustness value $RV$ is defined as the required confounding strength (``cf_y=rv`` and ``cf_d=rv``), such that the lower or upper bound of the causal parameter includes the null hypothesis.
If the estimated parameter :math:`\hat{\theta}` is larger than the null hypothesis the lower bound is used and vice versa.
The robustness value $RVa$ defined analogous, but additionally incorporates statistical uncertainty (as it is based on the confidence intervals of the bounds). 

To obtain a more complete overview over the sensitivity one can call the ``sensitivity_plot()`` method. The methods creates a contour plot, which calculates estimate of the upper or lower bound for :math:`\theta`
(based on the null hypothesis) for each combination of ``cf_y`` and ``cf_d`` in a grid of values.

.. figure:: /_static/sensitivity_example_nb.png
   :alt: Contour plot
   :figclass: captioned-image

   Contour plot example (see :ref:`examplegallery`)

By adjusting the parameter ``value='ci'`` in the ``sensitivity_plot()`` method the bounds are displayed for the corresponding confidence level.

.. note::

 -  The ``sensitivity_plot()`` requires to call ``sensitivity_analysis`` first, since the choice of the bound (upper or lower) is based on
    the corresponding null hypothesis. Further, the parameters ``rho`` and ``level`` are used. Both are contained in the ``sensitivity_params`` property.   
 -  The ``sensitivity_plot()`` is created for the first treatment variable. This can be changed via the ``idx_treatment`` parameter.
 -  The robustness values are given via the intersection countour of the null hypothesis and the identity.