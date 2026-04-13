#!/usr/bin/env python
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import seaborn as sns
import pandas as pd

'''
This script generates fig 4 panel d
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
fig, axs = plt.subplots(figsize=(1.62, 1.19))
#fig.subplots_adjust(right=0.99, left = 0.25, bottom =0.15, top = 0.85)
fig.subplots_adjust(right=0.99, left = 0.35, bottom =0.17, top = 0.84)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

data['den'] = data['nr_ves_b']/data['final_chull_mvv_ax']

axs = sns.violinplot(data=data, x="Mito", y="den", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75,ax =axs)
sns.despine(left=True, bottom=True)
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=8)
axs.set_xlabel('')
axs.set_ylabel(r'SV Den$\rm_{C}$ (#/$\mu m^3$)',fontsize=8,labelpad=0.3)
axs.set_ylim([0,2.5e4])
plt.legend([],[], frameon=False)

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs.yaxis.set_major_formatter(formatter)
plt.tick_params(axis='both', which='major', labelsize=8,pad=0.3)

axs.yaxis.offsetText.set_fontsize(9)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/ves_glob_den.png',dpi =600)

plt.show()
