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
            'figure.figsize': (2.5,2)}
mpl.rcParams.update(params)

#%------ Figure 1a -----------
#sns.set_theme()
sns.set_theme(style="whitegrid", palette="bright")
fig, axs = plt.subplots(figsize=(2.5, 2))
fig.subplots_adjust(right=0.95, left = 0.22, bottom =0.25, top = 0.95)
data1 = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')
#data = pd.read_csv('../../latest_results/data/all_data_together/fp_xr_all_together.csv')

#print(data['median_median_dis_ves_final'])
#data['dis_final'] = data['final_dis_az']

ltp = data.loc[(data['Mito'] == 'Yes') & (data['Condition'] == 'LTP') & (data['final_dis_AZ']>0) & (data['Animal'] == 'JB023')]
c = data.loc[(data['Mito'] == 'No')& (data['Condition'] == 'LTP') & (data['final_dis_AZ']>0)  & (data['Animal'] == 'JB023')]

bins = np.arange(0, 1,5e-3)
hist, bin_edges = np.histogram((ltp['final_dis_AZ']),bins)
plt.bar(bin_edges[:-1], hist/len(ltp['final_dis_AZ']), width = 5e-3, color='red', label ='')

hist, bin_edges = np.histogram((c['final_dis_AZ']),bins)
plt.bar(bin_edges[:-1], hist/len(c['final_dis_AZ']), width = 5e-3, color='blue', label ='',alpha =0.5)
print(np.median(ltp['final_dis_AZ']),np.median(c['final_dis_AZ']))
plt.ylabel('Frequency')
plt.xlabel(r'Median Dis AZ ($\mu$m)')
#plt.savefig('./Figures/distri_dis.png',dpi =600)
plt.show()
