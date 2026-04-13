#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import matplotlib as mpl

'''
This script generates fig 4 panel j
GCG
'''


params = {'axes.labelsize': 9,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)


data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

c_m = data.loc[(data['Condition'] == 'Control') & (data['mito_vol'] > 0)]
l_m = data.loc[(data['Condition'] == 'LTP') & (data['mito_vol'] > 0)]

c_nm = data.loc[(data['Condition'] == 'Control') & (data['mito_vol'] == 0)]
l_nm = data.loc[(data['Condition'] == 'LTP') & (data['mito_vol'] == 0)]

fig, axs = plt.subplots(figsize=(1.7,1.5))
fig.subplots_adjust(right=0.98, left = 0.28, bottom =0.23, top = 0.94)

a = 'b_vol'
b ='final_chull_ax'
plt.scatter(c_nm[a],c_nm[b],color='#224FDF',marker='.', label='Control -M',s=10,zorder=10)
plt.scatter(l_nm[a],l_nm[b],color='salmon',marker='.', label='LTP -M',s=10,zorder=10)

plt.scatter(c_m[a],c_m[b],color='navy',marker='.',label='Control +M',s=10,zorder=10)
plt.scatter(l_m[a],l_m[b],color='#CB1D25',marker='.',label='LTP +M',s=10,zorder=10)

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(l_nm[a]),np.log(l_nm[b]))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c_nm[a]),np.log(c_nm[b]))

a2 = np.exp(intercept)
b2 = slope
x2 = l_nm[a]
plt.plot(x2, a2*(x2**b2),color='salmon',lw=1,zorder=5)

a1 = np.exp(interceptc)
b1 = slopec
x1 = c_nm[a]
plt.plot(x1, a1*(x1**b1),color='#224FDF',lw=1,zorder=5)

plt.xscale('log')
plt.yscale('log')

yText1 = r'R$^2$ = %.2f ' %(np.round(r_valuec**2,decimals=2))
yText2 = r'R$^2$ = %.2f ' %(np.round(r_value**2,decimals=2))

slopem, interceptm, r_valuem, p_valuem, std_errm = stats.linregress(np.log(c_m[a]),np.log(c_m[b]))
slopelm, interceptlm, r_valuelm, p_valuelm, std_errlm = stats.linregress(np.log(l_m[a]),np.log(l_m[b]))
print(slopem,  np.exp(interceptm))

a3 = np.exp(interceptm)
b3 = slopem
x3 = c_m[a]
plt.plot(x3, a3*(x3**b3),color='navy',lw=1,zorder=5)

a4 = np.exp(interceptlm)
b4 = slopelm
x4 = l_m[a]
plt.plot(x4, a4*(x4**b4),color='#CB1D25',lw=1,zorder=5)

plt.ylabel(r'SV Vol$\rm_{C}$ ($\mu m^3$)',fontsize=8,labelpad=0.001)
plt.xlabel('Bouton Vol ($\mu m^3$)',fontsize=8,labelpad=0.001)

yText3 = r'R$^2$ = %.2f ' %(np.round(r_valuem**2,decimals=2))
yText4 = r'R$^2$ = %.2f ' %(np.round(r_valuelm**2,decimals=2))

plt.text(0.03,0.55, yText1, fontsize=6,color='#224FDF') #control no mito
plt.text(0.03,0.35, yText3, fontsize=6,color='navy') #control mito
plt.text(0.03,0.21, yText2, fontsize=6,color='salmon')  #ltp no mito
plt.text(0.03,0.13, yText4, fontsize=6,color='#CB1D25')#mito ltp

plt.ylim(0.005,1)
#plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/chull_vs_b_vol.png',dpi =600)

plt.show()
