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

data['cyto_vol'] = data['b_vol'] - data['convex_hull_inter_mito']

nm_ld = data.loc[(data['Mito'] == 'No')  & (data['final_med_mean_dis'] > 0.033)]
nm_hd = data.loc[(data['Mito'] == 'No')  & (data['final_med_mean_dis'] < 0.033)]

fig = plt.figure(figsize =(4,3))
fig.subplots_adjust(right=0.95, left = 0.15, bottom =0.2, top = 0.98)

plt.plot(nm_ld['b_vol'],nm_ld['cyto_vol']/nm_ld['convex_hull_inter_mito'],'r.', label = 'LVD')
plt.plot(nm_hd['b_vol'],nm_hd['cyto_vol']/nm_hd['convex_hull_inter_mito'],'b.', label = 'HVD')

slope, intercept, r_value, p_value, std_err = stats.linregress(np.log(nm_ld['b_vol']),np.log(nm_ld['cyto_vol']/nm_ld['convex_hull_inter_mito']))
slopec, interceptc, r_valuec, p_valuec, std_errc = stats.linregress(np.log(nm_hd['b_vol']),np.log(nm_hd['cyto_vol']/nm_hd['convex_hull_inter_mito']))

a = np.exp(intercept)
b = slope
x = nm_ld['b_vol']
plt.plot(x, a*(x**b),color='r')

a1 = np.exp(interceptc)
b1 = slopec
x1 = nm_hd['b_vol']
plt.plot(x1, a1*(x1**b1),color='b')

plt.xscale('log')
plt.yscale('log')

plt.ylabel('Cytoplasm vol/Convex hull vol')
plt.xlabel('Total bouton volume ($\mu m^3$)')

yText1 = r'$y = {%.2f}*x^{%.2f}$, R = %.2f ' %(np.round(a1,decimals=2),np.round(slopec,decimals =2),np.round(r_valuec,decimals=2))
yText2 = r'$y = %.2f *x^{ %.2f} $, R = %.2f ' %(np.round(a,decimals=2),np.round(slope,decimals=2),np.round(r_value,decimals=2))

plt.text(0.03,0.03, yText1, fontsize=8,color='b')
plt.text(0.03,0.06, yText2, fontsize=8,color='r')
#plt.savefig('../../figures/v2/figures/new/final/final_final/rel_mito_vs_rel_ves.png',dpi =600)
plt.ylim(0.0001, 15)

plt.legend(loc='lower right')
plt.savefig('./Figures/fig_4_3.png', dpi =600)
plt.show()
