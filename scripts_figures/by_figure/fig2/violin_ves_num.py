#!/usr/bin/env python
import  matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import seaborn as sns
import pandas as pd

'''
This script generates fig 2 panel f
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
fig, axs = plt.subplots(figsize=(1.6, 1.3))
fig.subplots_adjust(right=0.97, left = 0.33, bottom =0.15, top = 0.8)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

axs = sns.violinplot(data=data, x="Mito", y="nr_ves_b", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
axs.set_xticks([-0.05,1.05])
axs.set_xticklabels(['-Mito', '+Mito'],fontsize=6)
axs.set_xlabel('')
axs.set_ylabel(r'# SVs',fontsize=9,labelpad=0.3)

plt.legend([],[], frameon=False)

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs.yaxis.set_major_formatter(formatter)
plt.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.yaxis.offsetText.set_fontsize(9)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/num_ves_volb.png',dpi =600)


plt.show()
