#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import matplotlib as mpl

'''
This script generates fig 2 panel h
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

c_nm = data.loc[ (data['Condition'] == 'Control') & (data['Mito']=='No')]
ltp_nm = data.loc[(data['Condition'] =='LTP') & (data['Mito']=='No')]

fig, axs = plt.subplots(figsize=(2, 1.6))
fig.subplots_adjust(right=0.98, left = 0.26, bottom =0.22, top = 0.94)

plt.scatter(ltp_nm['b_vol'],ltp_nm['mean_ves_vol'],color='#CB1D25',marker='.',s = 10)#, label = 'LTP')
plt.scatter(c_nm['b_vol'],c_nm['mean_ves_vol'],color = '#224FDF',marker='.',s = 10)#, label = 'CTRL')

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(ltp_nm['b_vol']),np.log(ltp_nm['mean_ves_vol']))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c_nm['b_vol']),np.log(c_nm['mean_ves_vol']))
print('ltp',p_value,'c',p_valuec)

a = np.exp(intercept)
b = slope
x = ltp_nm['b_vol']
plt.plot(x, a*(x**b),color='#CB1D25')

a1 = np.exp(interceptc)
b1 = slopec
x1 = c_nm['b_vol']
plt.plot(x1, a1*(x1**b1),color='#224FDF')

axs.set_ylabel(r'Total SV Vol ($\mu m^3$)',fontsize=9,labelpad=0.3)
axs.set_xlabel(r'Bouton Vol ($\mu m^3$)',fontsize=9,labelpad=0.3)
axs.yaxis.set_label_coords(-.2, .5)
yText1 = r'R$^2$= %.2f ' %(np.round(r_valuec**2,decimals=2))
yText2 = r'R$^2$ = %.2f ' %(np.round(r_value**2,decimals=2))

plt.ylim(0.0005,0.3)
plt.text(0.029,0.15, yText1, fontsize=7,color='#224FDF')
plt.text(0.029,0.09, yText2, fontsize=7,color='#CB1D25')
plt.xscale('log')
plt.yscale('log')

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/bvol_ves_vol_nm.png',dpi =600)

plt.show()