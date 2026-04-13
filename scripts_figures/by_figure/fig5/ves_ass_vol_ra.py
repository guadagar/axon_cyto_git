#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats
import pandas as pd
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import seaborn as sns
from matplotlib.lines import Line2D

'''
This script generates fig 5 panel g
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.7,1.3)}

mpl.rcParams.update(params)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

ltp = data.loc[ (data['Condition'] == 'LTP') & (data['med_ass_ves_vol_final_ax'] > 0)   & (data['ra_ass_ves_vol_final_ax'] > 0)  ]

c = data.loc[(data['Condition'] == 'Control') & (data['med_ass_ves_vol_final_ax'] > 0)   & (data['ra_ass_ves_vol_final_ax'] > 0) ]

fig, ax = plt.subplots(figsize=(1.7,1.3))

fig.subplots_adjust(right=0.97, left = 0.25, bottom =0.3, top = 0.98)
sns.scatterplot(data=c, x= 'ra_ass_ves_vol_final_ax',y= 'med_ass_ves_vol_final_ax',s = 3,color='#224FDF',legend=False,ax=ax, label ='Control')# marker='s',s = 2,c=l_ltp_m['per_mito'],cmap=plt.cm.viridis,vmin=0, vmax=20)
sns.scatterplot(data=ltp, x= 'ra_ass_ves_vol_final_ax',y= 'med_ass_ves_vol_final_ax',s = 3,color='#CB1D25',legend=False,ax=ax, label = 'LTP' )# marker='s',s = 2,c=l_ltp_m['per_mito'],cmap=plt.cm.viridis,vmin=0, vmax=20)

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(ltp['ra_ass_ves_vol_final_ax']),np.log(ltp['med_ass_ves_vol_final_ax']))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c['ra_ass_ves_vol_final_ax']),np.log(c['med_ass_ves_vol_final_ax']))

a = np.exp(intercept)
b = slope
x = ltp['ra_ass_ves_vol_final_ax']

plt.plot(x, a*(x**b),color='#CB1D25',lw=1)

a1 = np.exp(interceptc)
b1 = slopec
x1 = c['ra_ass_ves_vol_final_ax']
plt.plot(x1, a1*(x1**b1),color='#224FDF',lw=1)

yText2 = r'R$^2$ = %.2f ' %(np.round(r_valuec**2,decimals=2))
yText1 = r'R$^2$ = %.2f ' %(np.round(r_value**2,decimals=2))

plt.text(0.0003,0.0007, yText1, fontsize=6,color='#CB1D25')
plt.text(0.0003,0.001, yText2, fontsize=6, color='#224FDF') #control

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#224FDF",mec='#224FDF')
circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#CB1D25",mec='#CB1D25')
plt.legend((circ1, circ2), ("Control","LTP"), numpoints=1,  frameon = False, bbox_to_anchor=(0.5, 0.68),handletextpad=0.01,labelspacing=0.1)

ax.set_ylabel(r' AVol$\rm_{SV}$ ($\mu m^{3}$)',fontsize=6,labelpad=0.01)
ax.set_xlabel(r' AVol$\rm_{SV}$ RD ($\mu m^{3}$)',fontsize=6,labelpad=0.01)

ax.yaxis.set_label_coords(-0.23,0.35)

x = np.arange(6e-5,0.7e-3,1e-4)
plt.plot(x, 1*(x),color='k',lw=1)
plt.ylim(4e-5,0.0015)
plt.xlim(4e-5,0.0015)

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

plt.xscale('log')
plt.yscale('log')

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/med_vor_ra_vs_c_ltp_log.png',dpi =600)

plt.show()
