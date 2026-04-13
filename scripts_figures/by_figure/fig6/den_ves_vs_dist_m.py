#!/usr/bin/env python
import matplotlib.ticker as mticker
import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
import pandas as pd
from matplotlib.lines import Line2D

'''
This script generates fig 6 panel a - in env ves_det
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)
#

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

data['mito_rel'] =data['mito_vol']/data['b_vol']
data['den_ves'] = (data['nr_ves_b'])/data['final_chull_mvv_ax']
#data['ves_rel'] =data['final_chull_mvv_ax']/data['b_vol']
data['ves_rel'] = (data['b_vol']-data['mito_vol']-data['final_chull_ax'])/data['b_vol']

ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['final_med_mean_dis']>0)  & (data['Mito'] == 'Yes')]# &  (data['med_ass_ves_vol_final_ax'] > 0)]
c_m = data.loc[(data['Condition'] == 'Control') & (data['final_med_mean_dis']>0) & (data['Mito'] == 'Yes') ]#&  (data['med_ass_ves_vol_final_ax'] > 0) ]

ltp_nm = data.loc[(data['Condition'] == 'LTP') & (data['final_med_mean_dis']>0)  & (data['Mito'] == 'No') ]#&  (data['med_ass_ves_vol_final_ax'] > 0)]
c_nm = data.loc[(data['Condition'] == 'Control') & (data['final_med_mean_dis']>0) & (data['Mito'] == 'No') ]#& (data['med_ass_ves_vol_final_ax'] > 0) ]

print(len(ltp_m['den_ves']),len(c_m['den_ves']), len(ltp_nm['den_ves']), len(c_nm['den_ves']))

fig, axs = plt.subplots(figsize=(1.7, 1.3))
fig.subplots_adjust(right=0.97, left = 0.25, bottom =0.23, top = 0.98)

var = 'den_ves'
var1 = 'final_med_mean_dis'

plt.scatter(ltp_m[var],ltp_m[var1],color='#CB1D25',marker='o',s=3, label= 'LTP +M',zorder=10)
plt.scatter(c_m[var],c_m[var1],color='navy',marker='o',s=3,label= 'Control +M', zorder=10)

plt.scatter(ltp_nm[var],ltp_nm[var1],color='salmon',marker='o',s=3, label= 'LTP -M',zorder=10)
plt.scatter(c_nm[var],c_nm[var1],color='#224FDF',marker='o',s=3, label= 'Control -M',zorder=10)

slope, intercept, r_valuem, p_value, std_err = stats.linregress(np.log(ltp_m[var]),np.log(ltp_m[var1]))
slopec, interceptc, r_valuecm, p_valuec, std_errc = stats.linregress(np.log(c_m[var]),np.log(c_m[var1]))

a = np.exp(intercept)
b = slope
x = ltp_m[var]

plt.plot(x, a*(x**b),color='r',zorder=5)

a1 = np.exp(interceptc)
b1 = slopec
x1 = c_m[var]
plt.plot(x1, a1*(x1**b1),color='b',zorder=5)

slopenm, interceptnm, r_valuenm, p_value, std_err = stats.linregress(np.log(ltp_nm[var]),np.log(ltp_nm[var1]))
slopecnm, interceptcnm, r_valuecnm, p_valuec, std_errc = stats.linregress(np.log(c_nm[var]),np.log(c_nm[var1]))

a = np.exp(interceptnm)
b = slopenm
x = ltp_nm[var]

plt.plot(x, a*(x**b),color='salmon',zorder=5)

a1 = np.exp(interceptcnm)
b1 = slopecnm
x1 = c_nm[var]
plt.plot(x1, a1*(x1**b1),color='#224FDF',zorder=5)


axs.set_ylabel(r'D$\rm_{Neigh}$ ($\mu m$)',fontsize=6,labelpad=0.03)
axs.set_xlabel(r'SV Den$\rm_{C}$ ($\mu m^{-3}$)',fontsize=6,labelpad=0.01)

yText1 = r'R$^2$ = %.2f ' %(np.round(r_valuecnm**2,decimals=2))
yText2 = r'R$^2$ = %.2f ' %(np.round(r_valuenm**2,decimals=2))
yText3 = r'R$^2$ = %.2f ' %(np.round(r_valuecm**2,decimals=2))
yText4 = r'R$^2$ = %.2f ' %(np.round(r_valuem**2,decimals=2))
#dis
plt.text(880,0.019, yText1, fontsize=6,color='#224FDF')#Control -M
plt.text(880,0.025, yText2, fontsize=6,color='Salmon')
plt.text(880,0.012, yText3, fontsize=6,color='navy') #Contol +M
plt.text(880,0.015, yText4, fontsize=6,color='#CB1D25')

circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#224FDF",mec='#224FDF',markeredgewidth=0.2)
circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="Salmon",mec='Salmon',markeredgewidth=0.2)
circ4 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="navy",mec='navy',markeredgewidth=0.2)
circ3 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#CB1D25",mec='#CB1D25',markeredgewidth=0.2)

plt.legend((circ1, circ2,circ3,circ4), ("LTP -M ","Control -M ","LTP +M ","Control +M "),fontsize = 6, numpoints=1,loc = 'upper left',mode ='expand', ncol=2, frameon = False,prop={'size': 5}, labelspacing=0.1,borderaxespad=0.1,handletextpad=0.1, handlelength=1)

plt.xscale('log')
plt.yscale('log')

plt.ylim(0.01,0.25) #med dis
plt.xlim(8e2,1.4e4) # std dis

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/den_vs_dis_all_w_reg.png',dpi =600)

plt.show()
