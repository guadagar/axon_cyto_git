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

ltp = data.loc[(data['Condition'] == 'LTP') & (data['med_ass_ves_vol'] > 0)]
c = data.loc[(data['Condition'] == 'Control') & (data['med_ass_ves_vol'] > 0)]

bins = np.arange(0, 8e-4,1e-5)

sns.histplot(data = ltp['med_ass_ves_vol'],stat='probability', kde=True,bins= bins, color ='red')
sns.histplot(data = c['med_ass_ves_vol'],stat='probability', kde=True,bins=bins, color
='blue')
#plt.plot(0.033*np.ones(len(np.arange(0,0.2,1e-3))), np.arange(0,0.2,1e-3), color = 'k', ls ='-.')
#ax.set_yticks(np.arange(-20,121,20))
#axs.set_xticks(np.arange(0.015, 0.1, 0.005))
#plt.xlim(0.015,0.1)
#plt.ylim(0,0.25)
plt.ylabel('Frequency')
plt.xlabel(r'Vesicle Associated Volume ($\mu m^3$)')
plt.savefig('./Figures/distri_dis_ass_vol.png',dpi =600)
plt.show()
