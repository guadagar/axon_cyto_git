#!/usr/bin/env python
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
import seaborn as sns
import pandas as pd

'''
This script generates fig 4 panel c
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

sns.set_theme(style="whitegrid", palette="bright")
fig, axs = plt.subplots(figsize=(1.62, 1.21))
fig.subplots_adjust(right=0.99, left = 0.4, bottom =0.15, top = 0.9)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

axs = sns.violinplot(data=data, x="Mito", y="final_chull_mvv_ax", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=9)
axs.set_xlabel('')

axs.set_ylabel(r'AVol$\rm_{C}$ ($\mu m^3$)',fontsize=8,labelpad=0.3)

plt.legend([],[], frameon=False)
plt.ylim(-0.03,0.7)

plt.tick_params(axis='both', which='major', labelsize=8,pad=0.3)
plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/ves_cloud_vol_mvv_ax.png',dpi =600)

plt.show()
