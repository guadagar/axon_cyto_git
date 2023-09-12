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


params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)
#

#%------ Figure 1a -----------
#sns.set_theme()
sns.set_theme(style="whitegrid", palette="bright")
fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.15, top = 0.85)
data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')
#data = pd.read_csv('../../latest_results/data/all_data_together/fp_xr_together.csv')

#print(data.drop(data.loc[data['convex_hul_vol'] == 0].index))
#sns.lineplot(data['b_vol'], data['mito_vol'])
#plt.plot(data['mito_vol'], data['b_vol'],'o')
data['dis_final'] = data['final_med_mean_dis']#1000*data['dis_nn']

axs = sns.violinplot(data=data.drop(data.loc[data['Mito'] == 'Yes'].index), x="Animal", y="dis_final", hue="Condition",
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
#plt.grid(True,color='0.95')
axs.set_xticklabels(['- Mito', '- Mito'],fontsize=9)
#axs.set_yticklabels([])
#axs.set_xlabel('')
axs.set_ylabel(r'Median Dis Ves (nm)',fontsize=9,labelpad=0.3)
#axs.set_ylabel('')
plt.legend([],[], frameon=False)
plt.ylim(0,100)
#plt.title('JB023',fontsize=9, pad =0.6)
#formatter = ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
#formatter.set_powerlimits((-1,1))
#axs.yaxis.set_major_formatter(formatter)
axs.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.yaxis.offsetText.set_fontsize(9)

#axs.get_yaxis().set_tick_params(pad=0.2)
#plt.savefig('../../figures/v2/figures/new/final/violin_median_dis_nm.png',dpi =600)#,bbox_inches='tight')

#Figure 2------------
sns.set_theme(style="whitegrid", palette="bright")
fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.15, top = 0.85)


axs = sns.violinplot(data=data.drop(data.loc[data['Mito'] == 'No'].index), x="Animal", y="dis_final", hue="Condition",
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
#plt.grid(True,color='0.95')
axs.set_xticklabels(['+ Mito', '+ Mito'],fontsize=9)
#axs.set_yticklabels([])
#axs.set_xlabel('')
axs.set_ylabel(r'Median Dis Ves (nm)',fontsize=9,labelpad=0.3)
#axs.set_ylabel('')
plt.legend([],[], frameon=False)
plt.ylim(0,100)
#plt.title('JB023',fontsize=9, pad =0.6)
#formatter = ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
#formatter.set_powerlimits((-1,1))
#axs.yaxis.set_major_formatter(formatter)
axs.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.yaxis.offsetText.set_fontsize(9)

#plt.savefig('../../figures/v2/figures/new/final/violin_median_dis_m.png',dpi =600)#,bbox_inches='tight')
# c['dis_final']
jb24_ltp_nm = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No') & (data['Animal'] == 'JB024') &  (data['dis_final'] < 0.033)]
jb24_c_nm = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No') & (data['Animal'] == 'JB024') & (data['dis_final'] < 0.033)]
jb23_ltp_nm = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No') & (data['Animal'] == 'JB023') & (data['dis_final'] < 0.033)]
jb23_c_nm = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'No') & (data['Animal'] == 'JB023') & (data['dis_final'] < 0.033)]

jb24_ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') & (data['Animal'] == 'JB024')  & (data['dis_final'] < 0.033)]
jb24_c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') & (data['Animal'] == 'JB024') & (data['dis_final'] < 0.033)]

jb23_ltp_m = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'Yes') & (data['Animal'] == 'JB023') & (data['dis_final'] < 0.033) ]
jb23_c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') &  (data['Animal'] == 'JB023') & (data['dis_final'] < 0.033) ]#&  (data['b_vol'] < 1) ]

print(len(jb24_ltp_nm['dis_final']),len(jb23_ltp_nm['dis_final']))
print(len(jb24_ltp_m['dis_final']),len(jb23_ltp_m['dis_final']))

print(len(jb24_c_nm['dis_final']),len(jb23_c_nm['dis_final']))
print(len(jb24_c_m['dis_final']),len(jb23_c_m['dis_final']))

plt.show()
