#!/usr/bin/env python
#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
from sklearn.cluster import KMeans
from matplotlib.lines import Line2D
'''
This script reads and analyses the some sheets of the original AXON_ca1_Master.xlsx file. To each axon the volume of
the contained mitochondria was added. The actual files read are: fpnct.csv, xrzct.csv, fwngv.cvs, and fhltd.cvs.
The analysis of the multilinear regression is also performed here.
GCG
12.20
'''

params = {'axes.labelsize': 9,
           'axes.titlesize': 9,
          'legend.fontsize': 9,
           'xtick.labelsize': 9,
           'ytick.labelsize': 9,
            'figure.figsize': (2,2)}
            #'figure.figsize': (6.4, 6)}
mpl.rcParams.update(params)


#data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')
data = pd.read_csv('../../../latest_results/data/all_data_together/fw_all_data.csv')
#data1 = pd.read_csv('../../../latest_results/data/all_data_together/fh_all_data.csv')

#data['den'] = data['nr_ves']/data['final_chull_mvv']
#data['den_loc'] = 1.0 /data['med_ass_ves_vol_final_im']
#data['den_loc_ra'] = 1.0 /data['ra_ass_ves_vol_final']

#ctrl['den'] = ctrl['nr_ves']/ctrl['Final_C_hull']
#ctrl['den_loc'] = 1.0 /ctrl['med_ass_im']


ltp = data.loc[ (data['med_ass_ves_vol_final_im'] > 0)  & (data['final_chull_mvv']>0) & (data['ra_ass_ves_vol_final'] > 0)]
#ltp_ra = data.loc[(data['ra_ass_ves_vol_final'] > 0)]

#c = ctrl.loc[ (ctrl['med_ass_im'] > 0)]
#ltp = data.loc[(data['Condition'] == 'LTP') & (data['med_ass_final'] > 0)]

fig = plt.figure(figsize =(4,3))
fig.subplots_adjust(right=0.95, left = 0.2, bottom =0.2, top = 0.98)

plt.plot(ltp['ra_ass_ves_vol_final'],ltp['med_ass_ves_vol_final_im'],'r.', label = 'NM')
#plt.plot(c['den'],c['den_loc'],'b.', label = 'NM')

#slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(ltp['den']),np.log(ltp['den_loc']))
#slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c['den']),np.log(c['den_loc']))
slope, intercept, r_value, p_value, std_err = stats.linregress(ltp['ra_ass_ves_vol_final'],ltp['med_ass_ves_vol_final_im'])
#slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress((c['den']),(c['den_loc']))

#a = np.exp(intercept)
#b = slope
x = ltp['ra_ass_ves_vol_final']

#plt.plot(x, a*(x**b),color='r')
plt.plot(x, slope*(x)+intercept,color='r')

#a1 = np.exp(interceptc)
#b1 = slopec
#x1 = c['den']
#plt.plot(x1, a1*(x1**b1),color='b')
#plt.plot(x1, slopec*(x1)+interceptc,color='b')

#yText1 = r'$y = {%.2f}*x^{%.2f}$, R = %.2f ' %(np.round(a1,decimals=2),np.round(slopec,decimals =2),np.round(r_valuec,decimals=2))
#yText2 = r'$y = %.2f *x^{ %.2f} $, R = %.2f ' %(np.round(a,decimals=2),np.round(slope,decimals=2),np.round(r_value,decimals=2))
yText1 = r'$y = {%.2f}*x + {%.2f}$, R = %.2f' %(np.round(slope,decimals=2),np.round(intercept,decimals =2),np.round(r_value,decimals=2))
#yText2 = r'$y = {%.2f}*x + { %.2f} $, R = %.2f ' %(np.round(slopec,decimals=2),np.round(interceptc,decimals=2),np.round(r_valuec,decimals=2))

plt.text(0.0001,0.0001, yText1, fontsize=8,color='r')
#plt.text(650,21000, yText2, fontsize=8,color='b')

plt.ylabel('Ves-Asso Vol ($\mu m^{3}$)')
plt.xlabel('Ves-Asso Vol Ra ($\mu m^{3}$)')
#x = np.arange(300,10000,2000)
plt.plot(x, 1*(x),color='k')
#plt.ylim(0,23000)
#plt.savefig('../../../figures/v2/figures/new/final/final_final/another_final/glob_vs_loc_den_wovv.png',dpi =600)
#plt.ylim(0,0.17)


#plt.legend(loc='lower right')
plt.show()
