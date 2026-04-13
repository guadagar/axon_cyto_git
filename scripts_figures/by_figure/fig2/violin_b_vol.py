#!/usr/bin/env python
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np

'''
This script generates fig 2 panel e
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
fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.15, top = 0.87)

data = pd.read_csv('../../../../../latest_results/data/all_data_together/all_data_last.csv')

axs = sns.violinplot(data=data, x="Mito", y="b_vol", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=9)
axs.set_xlabel('')
axs.set_ylabel(r'Bouton Vol ($\mu m^3$)',fontsize=9,labelpad=0.3)

plt.legend([],[], frameon=False)
plt.ylim(-0.03,1.1)

plt.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
#plt.savefig('../../../../../figures/v2/figures/new/final/final_final/another_final/violin_b_vol.png',dpi =600)

plt.show()
