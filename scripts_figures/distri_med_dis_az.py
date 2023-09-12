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


params = {'axes.labelsize': 7,
           'axes.titlesize': 7,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (3.5,3)}
mpl.rcParams.update(params)

#%------ Figure 1a -----------
#sns.set_theme()
#sns.set_theme(style="whitegrid", palette="bright")
sns.set_style("ticks")
fig, axs = plt.subplots(figsize=(8, 3))
fig.subplots_adjust(right=0.95, left = 0.08, bottom =0.15, top = 0.95)
data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')
#data = pd.read_csv('../../latest_results/data/all_data_together/fp_xr_all_together.csv')

#print(data['median_median_dis_ves_final'])
data['mito_frac'] = 100*data['mito_vol']/data['b_vol']

ltp = data.loc[(data['Condition'] == 'LTP') &  (data['Mito'] =='Yes') ]# (data['final_dis_AZ'] > 0) ]
c = data.loc[(data['Condition'] == 'Control') & (data['Mito'] =='Yes')  ]# (data['final_dis_AZ'] > 0)]

bins = np.arange(0, 50,1)

#bins = np.arange(0.005, 0.5,5e-3)
#hist, bin_edges = np.histogram((ltp['dis_final']),bins=bins)

sns.histplot(data = ltp['mito_frac'],stat='probability', kde=True,bins= bins, color ='red')
sns.histplot(data = c['mito_frac'],stat='probability', kde=True,bins=bins, color='blue')
print(stats.mannwhitneyu(ltp['mito_frac'],c['mito_frac'])[1])
#plt.plot(0.033*np.ones(len(np.arange(0,0.2,1e-3))), np.arange(0,0.2,1e-3), color = 'k', ls ='-.')
#ax.set_yticks(np.arange(-20,121,20))
#axs.set_xticks(np.arange(0.015, 0.1, 0.005))
#plt.xlim(0.005,0.5)
#plt.ylim(0,0.25)
plt.ylabel('Frequency')
#plt.xlabel(r'Median Dis Ves AZ ($\mu$m)')
#plt.savefig('./Figures/distri_dis_AZ.png',dpi =600)
plt.show()
