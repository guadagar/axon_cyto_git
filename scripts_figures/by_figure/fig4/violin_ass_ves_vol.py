#!/usr/bin/env python
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import seaborn as sns
import pandas as pd

'''
This script generates fig 4 panel h
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

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last.csv')

data1 = data.loc[(data['med_ass_ves_vol_final_im'] > 0)]
data1 ['den'] = 1/data1['med_ass_ves_vol_final_im']

fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.2, bottom =0.18, top = 0.8)
plt.rc('ytick', labelsize=9)
axs = sns.violinplot(data=data1, x="Mito", y="med_ass_ves_vol_final_im", hue="Condition",order=['No','Yes'],
               split=True, inner="quartile", linewidth=1,cut = 0,
			            		palette={"Control": "b", "LTP": "r"},saturation=0.75, ax =axs)
sns.despine(left=True, bottom=True)
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=9)
axs.set_ylabel(r'AVol$\rm_{SV}$ ($\mu m^3$)',fontsize=8,labelpad=0.3)

plt.legend([],[], frameon=False)
plt.ylim(0,0.0006)
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axs.yaxis.set_major_formatter(formatter)
plt.tick_params(axis='both', which='major', labelsize=9,pad=0.3)
axs.yaxis.offsetText.set_fontsize(9)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/violin_med_ass_ves_im.png',dpi =600)

plt.show()
