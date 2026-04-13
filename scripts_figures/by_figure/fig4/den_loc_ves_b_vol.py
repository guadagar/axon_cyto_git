#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import matplotlib as mpl

'''
This script generates fig 4 panel k
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.613,1.319)}
mpl.rcParams.update(params)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

data['den'] =data['nr_ves'] / data['final_chull_mvv_ax'] #packing density
data['pack'] =data['mean_ves_vol'] / data['final_chull_mvv_ax'] #packing density
data['den_loc'] =  1 / data['med_ass_ves_vol_final_ax'] #data['nr_ves_b'] / data['final_chull_ax']

d = data.loc[ (data['final_med_mean_dis'] > 0) &  (data['med_ass_ves_vol_final_ax'] > 0)]

l_nm = d.loc[(d['mito_vol'] == 0) & (d['Condition']=='LTP')]
c_nm = d.loc[ (d['mito_vol'] == 0) & (d['Condition']=='Control')]

l_m = d.loc[(d['mito_vol']>0) & (d['Condition']=='LTP')]
c_m = d.loc[(d['mito_vol']>0) & (d['Condition']=='Control')]

fig, axs = plt.subplots(figsize=(1.7,1.5))
fig.subplots_adjust(right=0.95, left = 0.25, bottom =0.23, top = 0.94)

a = 'final_chull_ax'
b = 'den_loc'

plt.scatter(c_nm[a],c_nm[b],color='#224FDF',marker='.', label='Control -M',s=10,zorder=10)
plt.scatter(l_nm[a],l_nm[b],color='salmon',marker='.', label='LTP -M',s=10,zorder=10)

plt.scatter(c_m[a],c_m[b],color='navy',marker='.',label='Control +M',s=10,zorder=10)
plt.scatter(l_m[a],l_m[b],color='#CB1D25',marker='.',label='LTP +M',s=10,zorder=10)
#
slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(c_nm[a]),np.log(c_nm[b]))
slopel, interceptl, r_valuel, p_valuel, std_errl = stats.linregress(np.log(l_nm[a]),np.log(l_nm[b]))

print(r_value**2,p_value,r_valuel**2,p_valuel)

slopem, interceptm, r_valuem, p_valuem, std_errm = stats.linregress(np.log(c_m[a]),np.log(c_m[b]))
slopelm, interceptlm, r_valuelm, p_valuelm, std_errlm = stats.linregress(np.log(l_m[a]),np.log(l_m[b]))

print(r_valuem**2,p_valuem,r_valuelm**2,p_valuelm)

ae = np.exp(intercept)
b = slope
x = c_nm[a]
plt.plot(x, ae*(x**b),color='#224FDF',lw=1)

a1 = np.exp(interceptl)
b1 = slopel
x1 = l_nm[a]
plt.plot(x1, a1*(x1**b1),color='salmon',lw=1)

yText1 = r'$R^2$ = %.3f,' %(np.round(r_valuel**2,decimals=3))
yText2 = r'$R^2$ = %.3f,' %(np.round(r_value**2,decimals=3))
print(r_valuel**2,r_value**2)

ae = np.exp(interceptm)
b = slopem
x = c_m[a]
plt.plot(x, ae*(x**b),color='navy',lw=1)

a1 = np.exp(interceptlm)
b1 = slopelm
x1 = l_m[a]

plt.plot(x1, a1*(x1**b1),color='#CB1D25',lw=1)

plt.xscale('log')
plt.yscale('log')

axs.set_ylabel(r'SV Den$\rm_{i}$ ($\mu m^{-3}$)',fontsize=8,labelpad=0.01)
axs.set_xlabel(r'SV Vol$\rm_{C}$ ($\mu m^3$)',fontsize=8,labelpad=0.01)

yText3 = r'R$^2$ = %.3f' %(np.round(r_valuelm**2,decimals=3))
yText4 = r'R$^2$ = %.3f' %(np.round(r_valuem**2,decimals=3))

plt.text(0.005,3.4e4, yText2, fontsize=6,color='#224FDF')
plt.text(0.08,3.4e4, yText4, fontsize=6,color='navy')
plt.text(0.005,2.4e4, yText1, fontsize=6,color='salmon')
plt.text(0.08,2.4e4, yText3, fontsize=6,color='#CB1D25')

plt.ylim(500, 5.3e4)
plt.xlim(4e-3,1)

plt.legend(loc = 'lower left',mode ='expand', ncol=2, frameon = False,prop={'size': 5}, labelspacing=0.1,borderaxespad=0.1,handletextpad=0.1, handlelength=1)

#plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/locden_vs_b_vol.png',dpi =600)

plt.show()