
#!/usr/bin/env python
import matplotlib.ticker as mticker
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats
from scipy.stats import variation,zscore,median_abs_deviation
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
#data['dis_final'] = 1000*data['median_median_dis_ves_final']
#data = data.loc[(data['med_ass_ves_vol'] > 0)]

#data['ves_per'] = 100*(data['mean_ves_vol'])/data['b_vol']
#data['rat'] = data['dis_ves_ol']/data['dis_ves_cm']
data['den'] = data['nr_ves']/data['final_chull_mvv']
#data['dis_ves'] = 1000*data['median_median_dis_ves_final']
#data['rat_dis'] = data['dis_cm_az']/data['disp_cm']


ltp_nm = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No') ]#& (data['Animal'] == 'JB024') ]
c_nm = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No') ]#& (data['Animal'] == 'JB024') ]

ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') ]#& (data['Animal'] == 'JB024') ]
c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes')]# & (data['Animal'] == 'JB024') ]

#ltp = data.loc[(data['Condition'] == 'LTP') &  (data['final_dis_AZ']>0)]#& (data['med_dis_AZ']>0) ]
#c = data.loc[(data['Condition'] == 'Control') & (data['final_dis_AZ']>0) ]# & (data['med_dis_AZ']>0) ]

a = 'dis_ves_ol_f'
b = 'dis_ves_ol_ra_f'

x = 6

print(a,'NM',np.round(ltp_nm[a].median(),decimals=x),np.round(c_nm[a].median(),decimals=x),stats.ks_2samp(ltp_nm[a],c_nm[a]),stats.mannwhitneyu(ltp_nm[a], c_nm[a])[1])
print('NM',np.round(ltp_nm[a].std(),decimals=x),np.round(c_nm[a].std(),decimals=x))
print('M',np.round(ltp_m[a].median(),decimals=x),np.round(c_m[a].median(),decimals=x),stats.ks_2samp(ltp_m[a],c_m[a]),stats.mannwhitneyu(ltp_m[a],c_m[a])[1])
print('M',np.round(ltp_m[a].std(),decimals=x),np.round(c_m[a].std(),decimals=x))

print(a,'NM',np.round(ltp_nm[a].median(),decimals=x),np.round(ltp_nm[b].median(),decimals=x),stats.ks_2samp(ltp_nm[a],ltp_nm[b]),stats.mannwhitneyu(ltp_nm[a], ltp_nm[b])[1])
print('M',np.round(ltp_m[a].median(),decimals=x),np.round(ltp_m[b].median(),decimals=x),stats.ks_2samp(ltp_m[a],ltp_m[b]),stats.mannwhitneyu(ltp_m[a],ltp_m[b])[1])
