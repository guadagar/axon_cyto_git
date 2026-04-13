#!/usr/bin/env python
import matplotlib.ticker as mticker
import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
import pandas as pd
from matplotlib.lines import Line2D

'''
This script generates fig S7 
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

data_apv = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_w_apv.csv')

data['mito_rel'] =data['mito_vol']/data['b_vol']
data['den_ves'] = (data['nr_ves_b'])/data['final_chull_mvv_ax']
data['ves_rel'] = (data['b_vol']-data['mito_vol']-data['final_chull_ax'])/data['b_vol']


ltp = data.loc[(data['Condition'] == 'LTP') & (data['final_med_mean_dis']>0)  ]# &  (data['med_ass_ves_vol_final_ax'] > 0)]
c = data.loc[(data['Condition'] == 'Control') & (data['final_med_mean_dis']>0)  ]#&  (data['med_ass_ves_vol_final_ax'] > 0) ]

data_apv['den_ves'] = (data_apv['nr_ves_b'])/data_apv['final_chull_mvv_ax']

ltp_apv = data_apv.loc[(data_apv['Condition'] == 'LTP') & (data_apv['final_med_mean_dis']>0) & (data_apv['APV']=='Yes')  ]# &  (data['med_ass_ves_vol_final_ax'] > 0)]
c_apv = data_apv.loc[(data_apv['Condition'] == 'Control') & (data_apv['final_med_mean_dis']>0)  & (data_apv['APV']=='Yes') ]#&  (data['med_ass_ves_vol_final_ax'] > 0) ]

fig, axs = plt.subplots(figsize=(1.7, 1.3))
fig.subplots_adjust(right=0.97, left = 0.25, bottom =0.23, top = 0.98)

var = 'den_ves'
var1 = 'final_med_mean_dis'

print(ltp_apv[var])
plt.scatter(ltp[var],ltp[var1],color='#CB1D25',marker='o',s=3, label= 'LTP +M',zorder=10)
plt.scatter(c[var],c[var1],color='navy',marker='o',s=3,label= 'Control +M', zorder=10)

plt.scatter(ltp_apv[var],ltp_apv[var1],color='orange',marker='o',s=3, label= 'LTP-APV',zorder=10)
plt.scatter(c_apv[var],c_apv[var1],color='darkcyan',marker='o',s=3, label= 'Control-APV',zorder=10)

slope, intercept, r_valuem, p_value, std_err = stats.linregress(np.log(ltp[var]),np.log(ltp[var1]))
slopec, interceptc, r_valuecm, p_valuec, std_errc = stats.linregress(np.log(c[var]),np.log(c[var1]))


a = np.exp(intercept)
b = slope
x = ltp[var]

a1 = np.exp(interceptc)
b1 = slopec
x1 = c[var]

slopenm, interceptnm, r_valuenm, p_value, std_err = stats.linregress(np.log(ltp_apv[var]),np.log(ltp_apv[var1]))
slopecnm, interceptcnm, r_valuecnm, p_valuec, std_errc = stats.linregress(np.log(c_apv[var]),np.log(c_apv[var1]))

axs.set_ylabel(r'D$\rm_{Neigh}$ ($\mu m$)',fontsize=6,labelpad=0.03)
axs.set_xlabel(r'SV Den$\rm_{C}$ ($\mu m^{-3}$)',fontsize=6,labelpad=0.01)

yText1 = r'R$^2$ = %.2f ' %(np.round(r_valuecnm**2,decimals=2))
yText2 = r'R$^2$ = %.2f ' %(np.round(r_valuenm**2,decimals=2))
yText3 = r'R$^2$ = %.2f ' %(np.round(r_valuecm**2,decimals=2))
yText4 = r'R$^2$ = %.2f ' %(np.round(r_valuem**2,decimals=2))
#dis
plt.text(880,0.019, yText1, fontsize=6,color='orange')#Control -M
plt.text(880,0.025, yText2, fontsize=6,color='darkcyan')
plt.text(880,0.012, yText3, fontsize=6,color='navy') #Contol +M
plt.text(880,0.015, yText4, fontsize=6,color='#CB1D25')

circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="darkcyan",mec='darkcyan',markeredgewidth=0.2)
circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="orange",mec='orange',markeredgewidth=0.2)
circ4 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="navy",mec='navy',markeredgewidth=0.2)
circ3 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#CB1D25",mec='#CB1D25',markeredgewidth=0.2)

plt.legend((circ1,circ2,circ3,circ4), ("LTP-APV","Control-APV","LTP","Control"),fontsize = 6, numpoints=1,loc = 'upper left',mode ='expand', ncol=2, frameon = False,prop={'size': 5}, labelspacing=0.1,borderaxespad=0.1,handletextpad=0.1, handlelength=1)
#plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.ylim(0.01,0.25) #med dis
plt.xlim(8e2,1.4e4) # std dis

#plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/den_vs_dis_all_apv.pdf',dpi =600)
ltp_apv = data_apv.loc[(data_apv['Condition'] == 'LTP') & (data_apv['final_med_mean_dis']>0) & (data_apv['APV']=='Yes')  & (data_apv['Mito']=='Yes') ]# &  (data['med_ass_ves_vol_final_ax'] > 0)]
c_apv = data_apv.loc[(data_apv['Condition'] == 'Control') & (data_apv['final_med_mean_dis']>0)  & (data_apv['APV'])  & (data_apv['Mito']=='Yes')]

ltp_apv_nm = data_apv.loc[
    (data_apv['Condition'] == 'LTP') & (data_apv['final_med_mean_dis'] > 0) & (data_apv['APV'] == 'Yes') & (
                data_apv['Mito'] == 'No')]  # &  (data['med_ass_ves_vol_final_ax'] > 0)]
c_apv_nm = data_apv.loc[(data_apv['Condition'] == 'Control') & (data_apv['final_med_mean_dis'] > 0) & (data_apv['APV']) & (
            data_apv['Mito'] == 'No')]

print(len(ltp_apv['b_vol']),len(ltp_apv_nm['b_vol']),len(c_apv['b_vol']),len(c_apv_nm['b_vol']) )
print(len(ltp_apv['b_vol'])+len(ltp_apv_nm['b_vol'])+len(c_apv['b_vol'])+len(c_apv_nm['b_vol']) )

plt.show()
