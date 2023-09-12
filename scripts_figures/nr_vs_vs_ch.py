
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

data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')

#data['mito_rel'] = 100*(data['b_vol']-data['mito_vol']-data['mean_ves_boot'])/data['b_vol']
data['den_ves'] = 100*(data['nr_ves'])/data['b_vol']

ltp = data.loc[(data['Condition'] == 'LTP') ]
c = data.loc[(data['Condition'] == 'Control')  ]#& (data['nr_ves']<1500)]

#jb23_ltp_nm = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'No') & (data['Animal'] == 'JB023') ]#& (data['mean_ass_ves_final']>0)]
#jb23_c_nm = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'No') & (data['Animal'] == 'JB023')]# & (data['nr_ves']< 1500)] #& (data['mean_ass_ves_final']>0) ]

#jb24_ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') & (data['Animal'] == 'JB024') ]#& (data['mean_ass_ves_final']>0)]
#jb24_c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') & (data['Animal'] == 'JB024') ]#& (data['mean_ass_ves_final']>0)]

#jb23_ltp_m = data.loc[(data['Condition'] == 'LTP')  & (data['Mito'] == 'Yes') & (data['Animal'] == 'JB023') ]#& (data['nr_ves'] > 200)]
#jb23_c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes') &  (data['Animal'] == 'JB023')]

#print(select1['mito_len']
#Median dis ves
#print('med_dis_jb24',jb24_ltp['median_dis_final'].median(),jb24_c['median_dis_final'].median(),stats.ks_2samp(jb24_ltp['median_dis_final'],jb24_c['median_dis_final']))
#print('med_dis_jb23',jb23_ltp['median_dis_final'].median(),jb23_c['median_dis_final'].median(),stats.ks_2samp(jb23_ltp['median_dis_final'],jb23_c['median_dis_final']))


#fig 4 c -------
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(2.5, 2.1))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.2, top = 0.88)

plt.plot(ltp['nr_ves'],ltp['final_chull'],'r o',markersize = 3)
plt.plot(c['nr_ves'],c['final_chull'],'o b',markersize = 3)

plt.xlabel('# Vesicles')
plt.ylabel('Vol Cloud ($\mu m^3$)')

slope4, intercept4, r_value4, p_value, std_err = stats.linregress(np.log(ltp['nr_ves']),np.log(ltp['final_chull']))
print('slope xr nm',slope4,intercept4,'r2',r_value4**2)
#plt.plot(jb23_ltp_nm['nr_ves'],jb23_ltp_nm['nr_ves']*slope4+intercept4,'r')
a4 = np.exp(intercept4)
b4 = slope4
x4 = ltp['nr_ves']
#v = np.log(var1a)
plt.plot(x4, a4*(x4**b4),color='r')

plt.text(12,0.25, r'$R^{2} = {%.2f}$' %(np.round(r_value4**2,decimals =2)), fontsize=7,color='r')
plt.text(12,0.16, r'$y = {%.5f}*x^{%.3f}$' %(np.round(a4,decimals=5),np.round(slope4,decimals =3)), fontsize=7,color='r')

slope4, intercept4, r_value4, p_value, std_err = stats.linregress(np.log(c['nr_ves']),np.log(c['final_chull']))
a4 = np.exp(intercept4)
b4 = slope4
x4 = c['nr_ves']
#v = np.log(var1a)
plt.plot(x4, a4*(x4**b4),color='b')

plt.text(12,0.55, r'$R^{2} = {%.2f}$' %(np.round(r_value4**2,decimals =2)), fontsize=7,color='b')
plt.text(12,0.38, r'$y = {%.5f}*x^{%.3f}$' %(np.round(a4,decimals=5),np.round(slope4,decimals =3)), fontsize=7,color='b')

plt.xscale('log')
plt.yscale('log')

plt.ylim(0.002,1)
plt.xlim(10,3000)

#plt.savefig('./Figures/den_disp_cm.png',dpi =600)#,bbox_inches='tight')

#plt.savefig('./Figures/nr_ves_chf_m.png',dpi =600)#,bbox_inches='tight')
#plt.savefig('./Figures/distri_dis_prob_b.png',dpi =600)

#------fig 4 D
#/nr_ves_chf_an2_m.png',dpi =600)#,bbox_inches='tight')

plt.show()
