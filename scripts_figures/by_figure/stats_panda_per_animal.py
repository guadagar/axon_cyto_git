
#!/usr/bin/env python
import matplotlib.ticker as mticker
import numpy as np
from scipy import stats
import pandas as pd

'''
This script is used to calculate statistics between different animalst 
GCG
'''

data = pd.read_csv('../../../latest_results/data/all_data_together/all_data_last.csv')

data['den'] = data['nr_ves_b']/data['final_chull_mvv_ax']
data ['den_loc'] = 1/data['med_ass_ves_vol_final_im']

#A = 'JB024'
A = 'JB023'
a = 'mito_vol'

ltp_nm = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'No')  & (data['Animal'] == A ) & (data[a] > 0 )]#& (data['final_dis_AZ']>0)] ['med_ass_ves_vol_final_ax'] > 0 ) ]
c_nm = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No')  & (data['Animal'] == A) & (data[a] > 0 ) ]#& (data['final_dis_AZ']>0)] & (data['med_ass_ves_vol_final_ax'] > 0)] 0 ) ]

ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') &  (data['Animal'] == A) & (data[a] > 0 ) ]#& (data['final_dis_AZ']>0)]# & (data['med_ass_ves_vol_final_ax'] > 0 )]
c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes')  & (data['Animal'] == A) & (data[a] > 0 )]#& (data['final_dis_AZ']>0)]#  &  (data['med_ass_ves_vol_final_ax'] > 0 )]

x = 6

#LTP vs Control
#print('C-LTP-NM',np.round(c_nm[a].median(),decimals=x),np.round(ltp_nm[a].median(),decimals=x),stats.mannwhitneyu(ltp_nm[a],c_nm[a])[1])
#print('C-LTP-NM-std',np.round(c_nm[a].std(),decimals=x),np.round(ltp_nm[a].std(),decimals=x))
#print(len(c_nm[a]),len(ltp_nm[a]))
#print(len(c_m[a]),len(ltp_m[a]))
print('C-LTP-M',np.round(c_m[a].median(),decimals=x),np.round(ltp_m[a].median(),decimals=x),stats.mannwhitneyu(ltp_m[a],c_m[a])[1])
#print('C-LTP-M -std',np.round(c_m[a].std(),decimals=x),np.round(ltp_m[a].std(),decimals=x))

#print('C-NM-M',stats.mannwhitneyu(c_nm[a],c_m[a])[1])
#print('L-NM-M',stats.mannwhitneyu(ltp_nm[a],ltp_m[a])[1])

A = 'JB024'

ltp_nm = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'No')  & (data['Animal'] == A ) & (data[a] > 0 )]#& (data['final_dis_AZ']>0)] ['med_ass_ves_vol_final_ax'] > 0 ) ]
c_nm = data.loc[(data['Condition'] == 'Control') & (data['Mito'] == 'No')   & (data['Animal'] == A) & (data[a] > 0 ) ]#& (data['final_dis_AZ']>0)] & (data['med_ass_ves_vol_final_ax'] > 0)] 0 ) ]

ltp_m = data.loc[(data['Condition'] == 'LTP') & (data['Mito'] == 'Yes') & (data['Animal'] == A) & (data[a] > 0 ) ]#& (data['final_dis_AZ']>0)]# & (data['med_ass_ves_vol_final_ax'] > 0 )]
c_m = data.loc[(data['Condition'] == 'Control')  & (data['Mito'] == 'Yes')  & (data['Animal'] == A) & (data[a] > 0 )]#& (data['final_dis_AZ']>0)]#  &  (data['med_ass_ves_vol_final_ax'] > 0 )]


x = 6

#LTP vs Control
#print('JB024, C-LTP-NM',np.round(c_nm[a].median(),decimals=x),np.round(ltp_nm[a].median(),decimals=x),stats.mannwhitneyu(ltp_nm[a],c_nm[a])[1])
#print('C-LTP-NM-std',np.round(c_nm[a].std(),decimals=x),np.round(ltp_nm[a].std(),decimals=x))
#print(len(c_nm[a]),len(ltp_nm[a]))
#print(len(c_m[a]),len(ltp_m[a]))
print('JB024, C-LTP-M',np.round(c_m[a].median(),decimals=x),np.round(ltp_m[a].median(),decimals=x),stats.mannwhitneyu(ltp_m[a],c_m[a])[1])
#print('C-LTP-M -std',np.round(c_m[a].std(),decimals=x),np.round(ltp_m[a].std(),decimals=x))

#print('C-NM-M',stats.mannwhitneyu(c_nm[a],c_m[a])[1])
#print('L-NM-M',stats.mannwhitneyu(ltp_nm[a],ltp_m[a])[1])
