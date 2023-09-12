
#!/usr/bin/env python
import matplotlib.ticker as mticker
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib.lines import Line2D
from matplotlib import cm
from random import random
import seaborn as sns
import pandas as pd

data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')

#data['mito_rel'] = 100*(data['b_vol']-data['mito_vol']-data['mean_ves_boot'])/data['b_vol']
data['den_ves'] = 100*(data['nr_ves'])/data['b_vol']

ltp = data.loc[(data['Condition'] == 'LTP')& (data['med_ass_final']>0) ]
c = data.loc[(data['Condition'] == 'Control') & (data['med_ass_final']>0)]

#fig 4 c -------
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(2.5, 2.1))
fig.subplots_adjust(right=0.93, left = 0.28, bottom =0.25, top = 0.88)

plt.plot(ltp['den_ves'],ltp['med_ass_final'],'r o',markersize = 2)
plt.plot(c['den_ves'],c['med_ass_final'],'o b',markersize = 2)

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(ltp['den_ves']),np.log(ltp['med_ass_final' ]))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c['den_ves']),np.log(c['med_ass_final']))
print(r_value,r_valuec)
a = np.exp(intercept)
b = slope
x = ltp['den_ves']

plt.plot(x, a*(x**b),color='r')

a1 = np.exp(interceptc)
b1 = slopec
x1 = c['den_ves']
plt.plot(x1, a1*(x1**b1),color='b')


plt.xlabel('Den ves in bouton ($\mu m^{-3}$)')
#plt.ylabel('Asso Ves Vol ($\mu m^3$) ')
plt.xlabel('Std Dis ($\mu m$) ')
plt.ylabel('Med Dis Ves ($\mu m$) ')


yText1 = r'$y = {%.3f}*x^{%.2f}$, R = %.2f ' %(np.round(a1,decimals= 3 ),np.round(slopec,decimals =2),np.round(r_valuec,decimals=2))
yText2 = r'$y = %.3f *x^{ %.2f} $, R = %.2f ' %(np.round(a,decimals=3),np.round(slope,decimals=2),np.round(r_value,decimals=2))

#plt.text(22000,0.15, yText1, fontsize=8,color='b')
#plt.text(22000,0.2, yText2, fontsize=8,color='r')
plt.text(0.007,0.1, yText1, fontsize=8,color='b')
plt.text(0.007,0.15, yText2, fontsize=8,color='r')

plt.xscale('log')
plt.yscale('log')

#plt.ylim(0.01,0.2)


#plt.ylim(0.005,0.2) #
#plt.xlim(2e4,1e6)
#plt.ylim(0.01,0.2) #med dis
#plt.xlim(0.006,0.15) # std dis

#plt.savefig('../../../figures/v2/figures/new/final/final_final/another_final/den_nndis.png',dpi =600)#,bbox_inches='tight')
#plt.savefig('../../../figures/v2/figures/new/final/final_final/another_final/den_nndis.png',dpi =600)#,bbox_inches='tight')

#plt.savefig('./Figures/dis_ves_ves_ch_reg.png',dpi =600)#,bbox_inches='tight')
#plt.savefig('./Figures/distri_dis_prob_b.png',dpi =600)

#------fig 4 D
#/nr_ves_chf_an2_m.png',dpi =600)#,bbox_inches='tight')

plt.show()
