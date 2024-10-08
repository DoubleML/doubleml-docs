Assume that we can write the model in the following representation

.. math::

    \theta_0 = \mathbb{E}[m(W,g_0)],

where usually :math:`g_0(W) = \mathbb{E}[Y|X, D]` (currently, the sensitivity analysis is only available for linear models).
As long as :math:`\mathbb{E}[m(W,f)]` is a continuous linear functional of :math:`f`, there exists a unique square 
integrable random variable :math:`\alpha_0(W)`, called Riesz representer
(see `Riesz-Fréchet representation theorem <https://en.wikipedia.org/wiki/Riesz_representation_theorem>`_), such that

.. math::

    \theta_0 = \mathbb{E}[g_0(W)\alpha_0(W)].

The target parameter :math:`\theta_0` has the following representation

.. math::

    \theta_0 = \mathbb{E}[m(W,g_0) + (Y-g_0(W))\alpha_0(W)],

which corresponds to a Neyman orthogonal score function (orthogonal with respect to nuisance elements :math:`(g, \alpha)`).
To bound the omitted variable bias, the following further elements are needed. 
The variance of the outcome regression 

.. math::

    \sigma_0^2 := \mathbb{E}[(Y-g_0(W))^2]

and the second moment of the Riesz representer 

.. math::

    \nu_0^2 := \mathbb{E}[\alpha_0(W)^2] =2\mathbb{E}[m(W,\alpha_0)] -  \mathbb{E}[\alpha_0(W)^2].

Both representations are Neyman orthogonal with respect to :math:`g` and :math:`\alpha`, respectively.
Further, define the corresponding score functions

.. math::

    \psi_{\sigma^2}(W, \sigma^2, g) &:= (Y-g_0(W))^2 - \sigma^2\\
    \psi_{\nu^2}(W, \nu^2, \alpha) &:= 2m(W,\alpha) - \alpha(W)^2 - \nu^2.

Recall that the parameter :math:`\theta_0` is identified via the moment condition

.. math::

    \theta_0 = \mathbb{E}[m(W,g_0)].

If :math:`W=(Y, D, X)` does not include all confounding variables, the "true" target parameter :math:`\tilde{\theta}_0`
would only be identified via the extendend (or "long") form

.. math::

    \tilde{\theta}_0 = \mathbb{E}[m(\tilde{W},\tilde{g}_0)],

where :math:`\tilde{W}=(Y, D, X, A)` includes the unobserved counfounders :math:`A`.
In Theorem 2 of their paper `Chernozhukov et al. (2022) <https://www.nber.org/papers/w30302>`_ are able to bound the omitted variable bias

.. math::

    |\tilde{\theta}_0 -\theta_0|^2 = \rho^2 B^2,

where 

.. math::

    B^2 := \mathbb{E}\Big[\big(g(W) - \tilde{g}(\tilde{W})\big)^2\Big]\mathbb{E}\Big[\big(\alpha(W) - \tilde{\alpha}(\tilde{W})\big)^2\Big],

denotes the product of additional variations in the outcome regression and Riesz representer generated by omitted confounders and

.. math::

    \rho^2 := \textrm{Cor}^2\Big(g(W) - \tilde{g}(\tilde{W}),\alpha(W) - \tilde{\alpha}(\tilde{W})\Big),

denotes the correlations between the deviations generated by omitted confounders. The choice :math:`\rho=1` is conservative and
accounts for adversarial confounding. Further, the bound can be expressed as

.. math::

    B^2 := \sigma_0^2 \nu_0^2 C_Y^2 C_D^2,

where

.. math::

    C_Y^2 &:= \frac{\mathbb{E}[(\tilde{g}(\tilde{W}) - g(W))^2]}{\mathbb{E}[(Y - g(W))^2]}

    C_D^2 &:=\frac{1 - \frac{\mathbb{E}\big[\alpha(W)^2\big]}{\mathbb{E}\big[\tilde{\alpha}(\tilde{W})^2\big]}}{\frac{\mathbb{E}\big[\alpha(W)^2\big]}{\mathbb{E}\big[\tilde{\alpha}(\tilde{W})^2\big]}}.

As :math:`\sigma_0^2` and :math:`\nu_0^2` do not depend on the unobserved confounders :math:`A` they are identified. Further, the other parts have the following interpretations

- ``cf_y``:math:`:=\frac{\mathbb{E}[(\tilde{g}(\tilde{W}) - g(W))^2]}{\mathbb{E}[(Y - g(W))^2]}`  measures the proportion of residual variance in the outcome :math:`Y` explained by the latent confounders :math:`A`

- ``cf_d``:math:`:=1 - \frac{\mathbb{E}\big[\alpha(W)^2\big]}{\mathbb{E}\big[\tilde{\alpha}(\tilde{W})^2\big]}` measures the proportion of residual variance in the Riesz representer :math:`\tilde{\alpha}(\tilde{W})` generated by the latent confounders :math:`A`

.. note::
    - ``cf_y`` has the interpretation as the *nonparametric partial* :math:`R^2` *of* :math:`A` *with* :math:`Y` *given* :math:`(D,X)`
    
    .. math:: 
        
        \frac{\textrm{Var}(\mathbb{E}[Y|D,X,A]) - \textrm{Var}(\mathbb{E}[Y|D,X])}{\textrm{Var}(Y)-\textrm{Var}(\mathbb{E}[Y|D,X])}

    - For model-specific interpretations of ``cf_d`` or :math:`C_D^2`, see the corresponding chapters (e.g. :ref:`sensitivity_plr`).

Consequently, for given values ``cf_y`` and ``cf_d``, we can create lower and upper bounds for target parameter :math:`\tilde{\theta}_0` of the form

.. math::

    \theta_{\pm}:=\theta_0 \pm |\rho| \sigma_0 \nu_0 C_Y C_D

Let :math:`\psi(W,\theta,\eta)` the (correctly scaled) score function for the target parameter :math:`\theta_0`. Then

.. math::

    \psi_{\pm}(W,\theta,\eta_\pm):= \psi(W,\theta,\eta) \pm \frac{|\rho| C_Y C_D}{2 \sigma \nu} \Big(\sigma^2 \psi_{\nu^2}(W, \nu^2, \alpha) + \nu^2 \psi_{\sigma^2}(W, \sigma^2, g)\Big)

determines a orthongonal score function for :math:`\theta_{\pm}`, with nuisance elements :math:`\eta_\pm:=(g, \alpha, \sigma, \nu)`.
The score can be used to calculate the standard deviations of :math:`\theta_{\pm}` via

.. math::

    \sigma^2_{\pm}= \mathbb{E}[\psi_{\pm}(W,\theta,\eta_\pm)^2]
    
For more detail and interpretations see `Chernozhukov et al. (2022) <https://www.nber.org/papers/w30302>`_.