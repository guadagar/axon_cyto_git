#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import matplotlib as mpl

'''
This script generates Fig S2a  
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)
#
sheet_2_df = pd.read_excel('./VesicleCalibration2.xlsx', sheet_name = None)
df_x = sheet_2_df['XRZCT']
df_fh = sheet_2_df['FHLTD']
df_fw = sheet_2_df['FWNGV']
df_fp = sheet_2_df['FPNCT']

df_merged = pd.concat([df_fh,df_fw],ignore_index = True, sort = False)

ltp_m = df_merged.loc[(df_merged['Condition'] == 'LTP')  & (df_merged['mito?'] == 'y')]
c_m = df_merged.loc[(df_merged['Condition'] == 'Control')  & (df_merged['mito?'] == 'y')]
ltp_nm = df_merged.loc[(df_merged['Condition'] == 'LTP')  & (df_merged['mito?'] == 'n')]
c_nm = df_merged.loc[(df_merged['Condition'] == 'Control')  & (df_merged['mito?'] == 'n')]

#print(df_merged)

sns.set_theme(style="whitegrid", palette="bright")

fig, axs = plt.subplots(figsize=(1.6, 1.3))
fig.subplots_adjust(right=0.97, left = 0.35, bottom =0.15, top = 0.85)

axs = sns.violinplot(data=df_merged, x="mito?", y="radius", hue="Condition",order=['n','y'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
#plt.grid(True,color='0.95')
axs.set_xticks([-0.05,1.05])
axs.set_xticklabels(['-Mito', '+Mito'],fontsize=6)
axs.set_yticklabels([])
axs.set_xlabel('')
axs.set_ylabel(r'',fontsize=9,labelpad=0.3)

plt.legend([],[], frameon=False)
plt.ylim(1.2e-2,4e-2)

# =============================================================================
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs.yaxis.set_major_formatter(formatter)

# =============================================================================
plt.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.set_yticklabels([])
axs.yaxis.offsetText.set_fontsize(9)

# =============================================================================
plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/violin_ves_rad_JB024.png',dpi =600)#,bbox_inches='tight')
plt.show()
a = 'radius'
print('L-C_M',ltp_m[a].median(),c_m[a].median(),stats.mannwhitneyu(ltp_m[a], c_m[a])[1])
print('L-C_M',ltp_m[a].std(),c_m[a].std())
print('L-C_NM',ltp_nm[a].median(),c_nm[a].median(),stats.mannwhitneyu(ltp_nm[a], c_nm[a])[1])
print('L-C_NM',ltp_nm[a].std(),c_nm[a].std())
