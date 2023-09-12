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

ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes')  ]
c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') ]


fig = plt.figure(figsize =(4,3))
fig.subplots_adjust(right=0.95, left = 0.15, bottom =0.2, top = 0.98)

plt.scatter(ltp_m['final_med_mean_dis'],ltp_m['mito_vol']/ltp_m['convex_hull_inter_mito'],color='r',marker='.', label = 'LDV-LTP')
plt.scatter(c_m['final_med_mean_dis'],c_m['mito_vol']/c_m['convex_hull_inter_mito'],color = 'b',marker='.', label = 'LDV-C')

#slope, intercept, r_value, p_value, std_err = stats.linregress(ltp_nm_ld['b_vol'],ltp_nm_ld['convex_hull_inter_mito'])
#slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(c_nm_ld['b_vol'],c_nm_ld['convex_hull_inter_mito'])

#print('ltp,ves',r_value,'cves',r_valuec)
plt.legend(loc = 'lower right')
x = ltp_m['b_vol']
x1 = c_m['b_vol']

#plt.plot(x1, slopec*x1+interceptc,'b')
#plt.plot(x, slope*x+intercept,'r')

plt.ylabel(r'Mito rat')
plt.xlabel(r'Dis Ves')

#yText1 = r'$y = %.2f *x  %.2f $, R = %.2f ' %(np.round(slopec,decimals=2),np.round(interceptc,decimals=2),np.round(r_valuec,decimals=2))
#yText2 = r'$y = %.2f *x  %.2f $, R = %.2f ' %(np.round(slope,decimals=2),np.round(intercept,decimals=2),np.round(r_value,decimals=2))

#plt.text(0.05,0.45, yText1, fontsize=8,color='b')
#plt.text(0.05,0.5, yText2, fontsize=8,color='r')
plt.savefig('fig_4_1.png', dpi =600)
plt.show()