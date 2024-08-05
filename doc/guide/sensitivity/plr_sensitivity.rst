In the :ref:`plr-model` the confounding strength ``cf_d`` can be further be simplified to match the explanation of ``cf_y``. 
Given the that the Riesz representer takes the following form

.. math::

    \alpha(W) = \frac{D-\mathbb{E}[D|X]}{\mathbb{E}[(D-\mathbb{E}[D|X]^2)]}

    \tilde{\alpha}(\tilde{W}) = \frac{D-\mathbb{E}[D|X,A]}{\mathbb{E}[(D-\mathbb{E}[D|X,A]^2)]}

one can show that

.. math::

    C_D^2 :=\frac{\frac{\mathbb{E}\big[\big(\mathbb{E}[D|X,A] - \mathbb{E}[D|X]\big)^2\big]}{\mathbb{E}\big[\big(D - \mathbb{E}[D|X]\big)^2\big]}}{1-\frac{\mathbb{E}\big[\big(\mathbb{E}[D|X,A] - \mathbb{E}[D|X]\big)^2\big]}{\mathbb{E}\big[\big(D - \mathbb{E}[D|X]\big)^2\big]}}.

Therefore,

- ``cf_y``:math:`:=\frac{\mathbb{E}[(\tilde{g}(\tilde{W}) - g(W))^2]}{\mathbb{E}[(Y - g(W))^2]}`  measures the proportion of residual variance in the outcome :math:`Y` explained by the latent confounders :math:`A`

- ``cf_d``:math:`:=\frac{\mathbb{E}\big[\big(\mathbb{E}[D|X,A] - \mathbb{E}[D|X]\big)^2\big]}{\mathbb{E}\big[\big(D - \mathbb{E}[D|X]\big)^2\big]}` measures the proportion of residual variance in the treatment :math:`D` explained by the latent confounders :math:`A`

.. note::
    In the :ref:`plr-model`, both ``cf_y`` and ``cf_d`` can be interpreted as *nonparametric partial* :math:`R^2`

    - ``cf_y`` has the interpretation as the *nonparametric partial* :math:`R^2` *of* :math:`A` *with* :math:`Y` *given* :math:`(D,X)`
    
    .. math:: 
        
        \frac{\textrm{Var}(\mathbb{E}[Y|D,X,A]) - \textrm{Var}(\mathbb{E}[Y|D,X])}{\textrm{Var}(Y)-\textrm{Var}(\mathbb{E}[Y|D,X])}

    - ``cf_d`` has the interpretation as the *nonparametric partial* :math:`R^2` *of* :math:`A` *with* :math:`D` *given* :math:`X`
    
    .. math:: 
        
        \frac{\textrm{Var}(\mathbb{E}[D|X,A]) - \textrm{Var}(\mathbb{E}[D|X])}{\textrm{Var}(D)-\textrm{Var}(\mathbb{E}[D|X])}

Using the partially linear regression model with ``score='partialling out'`` the ``nuisance_elements`` are implemented in the following form

.. math::

    \hat{\sigma}^2 &:= \mathbb{E}_n\Big[\big(Y-\hat{l}(X) - \hat{\theta}(D-\hat{m}(X))\big)^2\Big]

    \hat{\nu}^2 &:= \mathbb{E}_n[\hat{\alpha}(W)^2] = \frac{1}{\mathbb{E}_n\big[(D - \hat{m}(X))^2\big]}

with scores

.. math::

    \psi_{\sigma^2}(W, \hat{\sigma}^2, g) &:=  \big(Y-\hat{l}(X) - \hat{\theta}(D-\hat{m}(X))\big)^2 - \hat{\sigma}^2

    \psi_{\nu^2}(W, \hat{\nu}^2, \alpha) &:= \hat{\nu}^2 - \big(D-\hat{m}(X)\big)^2\big(\hat{\nu}^2)^2.

If ``score='IV-type'`` the senstivity elements are instead set to

.. math::

    \hat{\sigma}^2 &:= \mathbb{E}_n\Big[\big(Y - \hat{\theta}D - \hat{g}(X)\big)^2\Big]

    \psi_{\sigma^2}(W, \hat{\sigma}^2, g) &:=  \big(Y - \hat{\theta}D - \hat{g}(X)\big)^2 - \hat{\sigma}^2.