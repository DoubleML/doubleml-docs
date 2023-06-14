
"""
CVAR
===================================

This is an example of how to use the double machine learning approach for conditional value-at-risk estimation.
The code demonstrates the usage of the `DoubleMLCateEstimator` class and provides a step-by-step guide.
"""

# %% [markdown]
# # Python: Conditional Value at Risk of potential outcomes
# In this example, we illustrate how the [DoubleML](https://docs.doubleml.org/stable/index.html) package can be used to estimate the conditional Value at Risk of potential outcomes. The estimation is based on [Kallus  et al. (2019)](https://arxiv.org/abs/1912.12945).

# %% [markdown]
# ## Data
# We define a data generating process to create synthetic data to compare the estimates to the true effect.

# %%
import numpy as np
import pandas as pd
import doubleml as dml
import multiprocessing

from lightgbm import LGBMClassifier, LGBMRegressor

# %% [markdown]
# The data is generated as a location-scale model with
# 
# $$Y_i = \text{loc}(D_i,X_i) + \text{scale}(D_i,X_i)\cdot\varepsilon_i,$$
# 
# where $X_i\sim\mathcal{U}[-1,1]^{p}$ and $\varepsilon_i \sim \mathcal{N}(0,1)$.
# Further, the location and scale are determined according to the following functions
# 
# $$\begin{aligned}
# \text{loc}(d,x) &:= 0.5d + 2dx_5 + 2\cdot 1\{x_2 > 0.1\} - 1.7\cdot 1\{x_1x_3 > 0\} - 3x_4 \\
# \text{scale}(d,x) &:= \sqrt{0.5d + 0.3dx_1 + 2},
# \end{aligned}$$
# 
# and the treatment takes the following form
# 
# $$D_i = 1_{\{(X_2 - X_4 + 1.5\cdot 1\{x_1 > 0\} + \epsilon_i > 0)\}}$$
# 
# with $\epsilon_i \sim \mathcal{N}(0,1)$.

# %%
def f_loc(D, X):
  loc = 0.5*D + 2*D*X[:,4] + 2.0*(X[:,1] > 0.1) - 1.7*(X[:,0] * X[:,2] > 0) - 3*X[:,3]
  return loc

def f_scale(D, X):
  scale = np.sqrt(0.5*D + 0.3*D*X[:,1] + 2)
  return scale

def dgp(n=200, p=5):
    X = np.random.uniform(-1,1,size=[n,p])
    D = ((X[:,1 ] - X[:,3] + 1.5*(X[:,0] > 0) + np.random.normal(size=n)) > 0)*1.0
    epsilon = np.random.normal(size=n)

    Y = f_loc(D, X) + f_scale(D, X)*epsilon

    return Y, X, D, epsilon

# %% [markdown]
# We can calculate the true conditional value at risk through simulations. Here, we will just approximate the true conditional value at risk for the potential outcomes for a range of quantiles.

# %%
tau_vec = np.arange(0.1,0.95,0.05)
p = 5
n_true = int(10e+6)

_, X_true, _, epsilon_true = dgp(n=n_true, p = p)
D1 = np.ones(n_true)
D0 = np.zeros(n_true)

Y1 = f_loc(D1, X_true) + f_scale(D1, X_true)*epsilon_true
Y0 = f_loc(D0, X_true) + f_scale(D0, X_true)*epsilon_true

Y1_quant = np.quantile(Y1, q=tau_vec)
Y0_quant = np.quantile(Y0, q=tau_vec)

Y1_cvar = [Y1[Y1 >= quant].mean() for quant in Y1_quant]
Y0_cvar = [Y0[Y0 >= quant].mean() for quant in Y0_quant]

print(f'Conditional Value at Risk Y(0): {Y0_cvar}')
print(f'Conditional Value at Risk Y(1): {Y1_cvar}')

# %% [markdown]
# Let us generate $n=5000$ observations and convert them to a [DoubleMLData](https://docs.doubleml.org/stable/api/generated/doubleml.DoubleMLData.html) object.

# %%
n = 5000
np.random.seed(42)
Y, X, D, _ = dgp(n=n,p=p)
obj_dml_data = dml.DoubleMLData.from_arrays(X, Y, D)

# %% [markdown]
# ## Conditional Value at Risk (CVaR)
# Next, we can initialize our two machine learning algorithms to train the different nuisance elements (remark that in contrast to potential quantile estimation `ml_g` is a regressor). Then we can initialize the `DoubleMLCVAR` objects and call `fit()` to estimate the relevant parameters. To obtain confidence intervals, we can use the `confint()` method.

# %%
ml_g = LGBMRegressor(n_estimators=300, learning_rate=0.05, num_leaves=10)
ml_m = LGBMClassifier(n_estimators=300, learning_rate=0.05, num_leaves=10)

CVAR_0 = np.full((len(tau_vec)), np.nan)
CVAR_1 = np.full((len(tau_vec)), np.nan)

ci_CVAR_0 = np.full((len(tau_vec),2), np.nan)
ci_CVAR_1 = np.full((len(tau_vec),2), np.nan)

for idx_tau, tau in enumerate(tau_vec):
    print(f'Quantile: {tau}')
    dml_CVAR_0 = dml.DoubleMLCVAR(obj_dml_data,
                                ml_g, ml_m,
                                quantile=tau,
                                treatment=0,
                                n_folds=5)
    dml_CVAR_1 = dml.DoubleMLCVAR(obj_dml_data,
                                ml_g, ml_m,
                                quantile=tau,
                                treatment=1,
                                n_folds=5)

    dml_CVAR_0.fit()
    dml_CVAR_1.fit()

    ci_CVAR_0[idx_tau, :] = dml_CVAR_0.confint(level=0.95).to_numpy()
    ci_CVAR_1[idx_tau, :] = dml_CVAR_1.confint(level=0.95).to_numpy()

    CVAR_0[idx_tau] = dml_CVAR_0.coef
    CVAR_1[idx_tau] = dml_CVAR_1.coef

# %% [markdown]
# Finally, let us take a look at the estimated values.

# %%
data = {"Quantile": tau_vec, "CVaR Y(0)": Y0_cvar, "CVaR Y(1)": Y1_cvar,
        "DML CVaR Y(0)": CVAR_0, "DML CVaR Y(1)": CVAR_1,
        "DML CVaR Y(0) lower": ci_CVAR_0[:, 0], "DML CVaR Y(0) upper": ci_CVAR_0[:, 1],
        "DML CVaR Y(1) lower": ci_CVAR_1[:, 0], "DML CVaR Y(1) upper": ci_CVAR_1[:, 1]}
df = pd.DataFrame(data)
print(df)

# %%
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = 10., 7.5
fig, (ax1, ax2) = plt.subplots(1 ,2)
ax1.grid(); ax2.grid()

ax1.plot(df['Quantile'],df['DML CVaR Y(0)'], color='violet', label='Estimated CVaR Y(0)')
ax1.plot(df['Quantile'],df['CVaR Y(0)'], color='green', label='True CVaR Y(0)')
ax1.fill_between(df['Quantile'], df['DML CVaR Y(0) lower'], df['DML CVaR Y(0) upper'], color='violet', alpha=.3, label='Confidence Interval')
ax1.legend()
ax1.set_ylim(-2, 6)

ax2.plot(df['Quantile'],df['DML CVaR Y(1)'], color='violet', label='Estimated CVaR Y(1)')
ax2.plot(df['Quantile'],df['CVaR Y(1)'], color='green', label='True CVaR Y(1)')
ax2.fill_between(df['Quantile'], df['DML CVaR Y(1) lower'], df['DML CVaR Y(1) upper'], color='violet', alpha=.3, label='Confidence Interval')
ax2.legend()
ax2.set_ylim(-2, 6)

fig.suptitle('Conditional Value at Risk', fontsize=16)
fig.supxlabel('Quantile')
_ = fig.supylabel('CVaR and 95%-CI')

# %% [markdown]
# ## CVaR Treatment Effects
# In most cases, we want to evaluate the treatment effect on the CVaR as the difference between potential CVaRs.
# To estimate the treatment effect, we can use the `DoubleMLQTE` object and specify `CVaR` as the score. 
# 
# As for quantile treatment effects, different quantiles can be estimated in parallel with `n_jobs_models`.

# %%
n_cores = multiprocessing.cpu_count()
cores_used = np.min([5, n_cores - 1])
print(f"Number of Cores used: {cores_used}")

dml_CVAR = dml.DoubleMLQTE(obj_dml_data,
                           ml_g,
                           ml_m,
                           score='CVaR',
                           quantiles=tau_vec,
                           n_folds=5)
dml_CVAR.fit(n_jobs_models=cores_used)
print(dml_CVAR)

# %% [markdown]
# As for standard `DoubleMLCVAR` objects, we can construct valid confidencebands with the `confint()` method. Additionally, it might be helpful to construct uniformly valid confidence regions via boostrap.

# %%
ci_CVAR = dml_CVAR.confint(level=0.95, joint=False)

dml_CVAR.bootstrap(n_rep_boot=2000)
ci_joint_CVAR = dml_CVAR.confint(level=0.95, joint=True)
ci_joint_CVAR

# %% [markdown]
# Finally, we can compare the predicted treatment effect with the true treatment effect on the CVaR.

# %%
CVAR = np.array(Y1_cvar) - np.array(Y0_cvar)
data = {"Quantile": tau_vec, "CVaR": CVAR, "DML CVaR": dml_CVAR.coef,
        "DML CVaR pointwise lower": ci_CVAR['2.5 %'], "DML CVaR pointwise upper": ci_CVAR['97.5 %'],
        "DML CVaR joint lower": ci_joint_CVAR['2.5 %'], "DML CVaR joint upper": ci_joint_CVAR['97.5 %']}
df = pd.DataFrame(data)
print(df)

# %%
plt.rcParams['figure.figsize'] = 10., 7.5
fig, ax = plt.subplots()
ax.grid()

ax.plot(df['Quantile'],df['DML CVaR'], color='violet', label='Estimated CVaR')
ax.plot(df['Quantile'],df['CVaR'], color='green', label='True CVaR')
ax.fill_between(df['Quantile'], df['DML CVaR pointwise lower'], df['DML CVaR pointwise upper'], color='violet', alpha=.3, label='Pointwise Confidence Interval')
ax.fill_between(df['Quantile'], df['DML CVaR joint lower'], df['DML CVaR joint upper'], color='violet', alpha=.2, label='Joint Confidence Interval')

plt.legend()
plt.title('Conditional Value at Risk', fontsize=16)
plt.xlabel('Quantile')
_ = plt.ylabel('QTE and 95%-CI')


