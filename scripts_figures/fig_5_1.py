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

m_ld = data.loc[(data['Mito'] == 'Yes') & (data['final_med_mean_dis'] > 0.033)]
m_hd = data.loc[(data['Mito'] == 'Yes') & (data['final_med_mean_dis'] < 0.033)]

fig = plt.figure(figsize =(4,3))
fig.subplots_adjust(right=0.95, left = 0.2, bottom =0.2, top = 0.98)

plt.plot(m_ld['b_vol'],m_ld['mito_vol'],'r.', label = 'LVD')
plt.plot(m_hd['b_vol'],m_hd['mito_vol'],'b.', label = 'HVD')

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(m_ld['b_vol']),np.log(m_ld['mito_vol']))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(m_hd['b_vol']),np.log(m_hd['mito_vol']))

a = np.exp(intercept)
b = slope
x = m_ld['b_vol']

plt.plot(x, a*(x**b),color='r')

a1 = np.exp(interceptc)
b1 = slopec
x1 = m_hd['b_vol']
plt.plot(x1, a1*(x1**b1),color='b')

plt.xscale('log')
plt.yscale('log')

plt.ylabel('Mitochondria volume ($\mu m^3$)')
plt.xlabel('Total bouton volume ($\mu m^3$)')


yText1 = r'$y = {%.2f}*x^{%.2f}$, R = %.2f ' %(np.round(a1,decimals=2),np.round(slopec,decimals =2),np.round(r_valuec,decimals=2))
yText2 = r'$y = %.2f *x^{ %.2f} $, R = %.2f ' %(np.round(a,decimals=2),np.round(slope,decimals=2),np.round(r_value,decimals=2))

plt.text(0.08,0.12, yText1, fontsize=8,color='b')
plt.text(0.08,0.16, yText2, fontsize=8,color='r')
#plt.savefig('../../figures/v2/figures/new/final/final_final/rel_mito_vs_rel_ves.png',dpi =600)
#plt.ylim(0,0.17)
plt.ylim(0,0.6)

plt.legend(loc='lower right')
plt.savefig('./Figures/fig_5_1.png', dpi =600)
plt.show()