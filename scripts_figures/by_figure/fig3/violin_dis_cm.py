#!/usr/bin/env python
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
import seaborn as sns
import pandas as pd

'''
This script generates fig 3 panel f
GCG
'''


params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)

sns.set_theme(style="whitegrid", palette="bright")
fig, axs = plt.subplots(figsize=(1.61, 1.17))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.16, top = 0.85)
data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

axs = sns.violinplot(data=data, x="Mito", y="dis_ves_cm_f", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=9)
axs.set_ylabel(r'D$\rm_{CC}$ ($\mu$m)',fontsize=9,labelpad=0.3)
plt.legend([],[], frameon=False)

axs.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.yaxis.offsetText.set_fontsize(9)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/violin_median_disp_cloud.png',dpi =600)

plt.show()
