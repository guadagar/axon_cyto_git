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
data['dis_final'] = data['final_med_mean_dis']

ltp = data.loc[(data['Condition'] == 'LTP') & (data['Animal'] == 'JB024')]
c = data.loc[(data['Condition'] == 'Control') & (data['Animal'] == 'JB024') ]

bins = np.arange(0.015, 0.1,2.5e-3)
hist, bin_edges = np.histogram((ltp['dis_final']),bins=bins)

#print(bins, bin_edges)

#plt.bar(bin_edges[:-1], hist/len(ltp['dis_final']), width = 2.5e-3, color='y', label ='')
##plt.hist(ltp['dis_final'], bins=bins,density=True, color='m')
#print(bin_edges[:-1])
#plt.plot(bin_edges[:-1],hist/len(ltp['dis_final']),'k')

#hist, bin_edges = np.histogram((c['dis_final']),bins)
#plt.bar(bin_edges[:-1], hist/len(c['dis_final']), width = 2.5e-3, color='g', label ='',alpha =0.5)
#plt.plot(bin_edges[:-1],hist/len(c['dis_final']),'b')

#sns.distplot(ltp['dis_final'], hist=True, kde=True, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth':2}, bins=bins, color='red')
#sns.distplot(c['dis_final'], hist=True, kde=True, hist_kws={'edgecolor':'black'}, kde_kws={'linewidth':2}, bins=15, color='blue')


sns.histplot(data = ltp['dis_final'],stat='probability', kde=True,bins= bins, color ='red')
sns.histplot(data = c['dis_final'],stat='probability', kde=True,bins=bins, color='blue')
plt.plot(0.033*np.ones(len(np.arange(0,0.2,1e-3))), np.arange(0,0.2,1e-3), color = 'k', ls ='-.')
#ax.set_yticks(np.arange(-20,121,20))
axs.set_xticks(np.arange(0.015, 0.1, 0.005))
plt.xlim(0.015,0.1)
plt.ylim(0,0.25)
plt.ylabel('Frequency')
plt.xlabel(r'Median Dis Ves ($\mu$m)')
#plt.savefig('./Figures/distri_dis_prob_a2.png',dpi =600)
plt.show()
