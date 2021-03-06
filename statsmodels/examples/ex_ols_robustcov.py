
from __future__ import print_function
import numpy as np
from statsmodels.regression.linear_model import OLS, GLSAR
from statsmodels.tools.tools import add_constant
from statsmodels.datasets import macrodata
import statsmodels.regression.tests.results.results_macro_ols_robust as res


d2 = macrodata.load().data
g_gdp = 400*np.diff(np.log(d2['realgdp']))
g_inv = 400*np.diff(np.log(d2['realinv']))
exogg = add_constant(np.c_[g_gdp, d2['realint'][:-1]], prepend=False)
res_olsg = OLS(g_inv, exogg).fit()



print(res_olsg.summary())
res_hc0 = res_olsg.get_robustcov_results('HC1')
print('\n\n')
print(res_hc0.summary())
print('\n\n')
res_hac4 = res_olsg.get_robustcov_results('HAC', maxlags=4, use_correction=True)
print(res_hac4.summary())


print('\n\n')
tt = res_hac4.t_test(np.eye(len(res_hac4.params)))
print(tt.summary())
print('\n\n')
print(tt.summary_frame())

res_hac4.use_t = False

print('\n\n')
tt = res_hac4.t_test(np.eye(len(res_hac4.params)))
print(tt.summary())
print('\n\n')
print(tt.summary_frame())

print(vars(res_hac4.f_test(np.eye(len(res_hac4.params))[:-1], use_f=True)))
print(vars(res_hac4.f_test(np.eye(len(res_hac4.params))[:-1], use_f=False)))
