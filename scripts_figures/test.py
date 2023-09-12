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

#%------ Figure 1a -----------
#sns.set_theme()
sns.set_theme(style="whitegrid", palette="bright")
fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.15, top = 0.85)
data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')
#data = pd.read_csv('../../latest_results/data/all_data_together/fp_xr_all_together.csv')

#print(data['median_median_dis_ves_final'])
#data['dis_final'] = 1000*data['final_med_mean_dis']
data1 = data.loc[(data['med_ass_final'] > 0)]
data1['den'] = data1['nr_ves']/data1['final_chull']

axs = sns.violinplot(data=data1, x="Mito", y="dis_ves_cm", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
#plt.grid(True,color='0.95')
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=9)
#axs.set_yticklabels([])
#axs.set_xlabel('')
axs.set_ylabel(r'Median Dis Ves (nm)',fontsize=9,labelpad=0.3)
#axs.set_ylabel('')
plt.legend([],[], frameon=False)
#plt.ylim(0,100)
#plt.title('JB023',fontsize=9, pad =0.6)
#formatter = ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
#formatter.set_powerlimits((-1,1))
#axs.yaxis.set_major_formatter(formatter)
axs.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.yaxis.offsetText.set_fontsize(9)

#axs.get_yaxis().set_tick_params(pad=0.2)
#plt.savefig('../../../figures/v2/figures/new/final/final_final/another_final/violin_median_dis_all.png',dpi =600)#,bbox_inches='tight')
#plt.savefig('./Figures/violin_median_dis_all.png',dpi =600)#,bbox_inches='tight')

l_ltp_nm = data1.loc[(data['Condition'] == 'LTP') & (data1['Mito'] == 'No')]
l_c_nm = data1.loc[(data['Condition'] == 'Control')  & (data1['Mito'] == 'No')]

l_ltp_m = data1.loc[(data['Condition'] == 'LTP')  & (data1['Mito'] == 'Yes')]
l_c_m = data1.loc[(data['Condition'] == 'Control') & (data1['Mito'] == 'Yes')]

print('L-C-NM',l_ltp_nm['dis_ves_cm'].median(),l_c_nm['dis_ves_cm'].median(),stats.ks_2samp(l_ltp_nm['dis_ves_cm'],l_c_nm['dis_ves_cm']))
print('L-C_M',l_ltp_m['dis_ves_cm'].median(),l_c_m['dis_ves_cm'].median(),stats.ks_2samp(l_ltp_m['dis_ves_cm'],l_c_m['dis_ves_cm']))

plt.show()
