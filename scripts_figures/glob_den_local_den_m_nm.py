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


data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')

#data['den'] = data['nr_ves']/data['final_chull']
#data['den_loc'] = 1.0 /data['med_ass_final']
data['den'] = data['nr_ves']/data['final_chull_mvv']
data['den_loc'] = 1.0 /data['med_ass_final']


ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') & (data['med_ass_final'] > 0)]
c_m = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'Yes') &  (data['med_ass_final'] > 0)]

ltp_nm = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No') & (data['med_ass_final'] > 0)]
c_nm = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No') & (data['med_ass_final'] > 0)]



fig = plt.figure(figsize =(4,3))
fig.subplots_adjust(right=0.95, left = 0.2, bottom =0.2, top = 0.98)

plt.plot(ltp_nm['den'],ltp_nm['den_loc'],'r.', label = 'NM')
plt.plot(c_nm['den'],c_nm['den_loc'],'b.', label = 'NM')

plt.plot(ltp_m['den'],ltp_m['den_loc'],'m.', label = 'M')
plt.plot(c_m['den'],c_m['den_loc'],'c.', label = 'M')

#plt.plot(l_ltp_m['b_vol'],l_ltp_m['b_sa'],'y.', label = 'M')
#plt.plot(l_c_m['b_vol'],l_c_m['b_sa'],'g.', label = 'M')

#slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(ltp['den']),np.log(ltp['den_loc']))
#slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(c['den']),np.log(c['den_loc']))
slope, intercept, r_value, p_value, std_err = stats.linregress((ltp_nm['den']),(ltp_nm['den_loc']))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress((c_nm['den']),(c_nm['den_loc']))

#a = np.exp(intercept)
#b = slope
x = ltp_nm['den']

#plt.plot(x, a*(x**b),color='r')
plt.plot(x, slope*(x)+intercept,color='r')

#a1 = np.exp(interceptc)
#b1 = slopec
x1 = c_nm['den']
#plt.plot(x1, a1*(x1**b1),color='b')
plt.plot(x1, slopec*(x1)+interceptc,color='b')

#yText1 = r'$y = {%.2f}*x^{%.2f}$, R = %.2f ' %(np.round(a1,decimals=2),np.round(slopec,decimals =2),np.round(r_valuec,decimals=2))
#yText2 = r'$y = %.2f *x^{ %.2f} $, R = %.2f ' %(np.round(a,decimals=2),np.round(slope,decimals=2),np.round(r_value,decimals=2))
yText1 = r'$y = {%.2f}+x*{%.2f}$, R = %.2f , NM' %(np.round(intercept,decimals=2),np.round(slope,decimals =2),np.round(r_value,decimals=2))
yText2 = r'$y = %.2f +x*{ %.2f} $, R = %.2f ,NM ' %(np.round(interceptc,decimals=2),np.round(slopec,decimals=2),np.round(r_valuec,decimals=2))

plt.text(650,19000, yText1, fontsize=8,color='r')
plt.text(650,20000, yText2, fontsize=8,color='b')

slope, intercept, r_value, p_value, std_err = stats.linregress(ltp_m['den'],ltp_m['den_loc'])
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(c_m['den'],c_m['den_loc'])

#a = np.exp(intercept)
#b = slope
x = ltp_m['den']

#plt.plot(x, a*(x**b),color='y')
plt.plot(x, slope*(x)+intercept,color='m')

#a1 = np.exp(interceptc)
#b1 = slopec
x1 = c_m['den']
#plt.plot(x1, a1*(x1**b1),color='g')
plt.plot(x1, slopec*(x1)+interceptc,color='c')

#plt.xscale('log')
#plt.yscale('log')

plt.ylabel('Local Den Ves ($\mu m^{-3}$)')
plt.xlabel('Global Den Ves ($\mu m^{-3}$)')

yText1 = r'$y = {%.2f}+x*{%.2f}$, R = %.2f , M' %(np.round(intercept,decimals=2),np.round(slope,decimals =2),np.round(r_value,decimals=2))
yText2 = r'$y = %.2f +x*{ %.2f} $, R = %.2f , M ' %(np.round(interceptc,decimals=2),np.round(slopec,decimals=2),np.round(r_valuec,decimals=2))

plt.text(650,21000, yText1, fontsize=8,color='m')
plt.text(650,22000, yText2, fontsize=8,color='c')

#yText1 = r'$y = {%.2f}*x^{%.2f}$, R = %.2f ' %(np.round(a1,decimals=2),np.round(slopec,decimals =2),np.round(r_valuec,decimals=2))
#yText2 = r'$y = %.2f *x^{ %.2f} $, R = %.2f ' %(np.round(a,decimals=2),np.round(slope,decimals=2),np.round(r_value,decimals=2))

#plt.text(0.04,6, yText1, fontsize=8,color='g')
#plt.text(0.04,6.5, yText2, fontsize=8,color='y')
plt.savefig('../../../figures/v2/figures/new/final/final_final/another_final/glob_vs_loc_den_M_NM_wovv.png',dpi =600)
#plt.ylim(0,0.17)
#plt.ylim(0,0.6)

#plt.legend(loc='lower right')
plt.show()