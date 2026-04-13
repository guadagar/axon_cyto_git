#!/usr/bin/env python
import  matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib.lines import Line2D

'''
This scripts generates Fig S4a
GCG
'''

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data_last_msb_con.csv')

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)

sns.set_theme(style="whitegrid",palette=None)
fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.92, left = 0.23, bottom =0.15, top = 0.87)

c = data.loc[(data['Condition'] == 'Control') & (data['final_dis_AZ']>0)]

axs = sns.violinplot(data=c, x="Mito", y="final_dis_AZ", hue="msb",order=['No','Yes'],
                     split=True, inner="quartile", linewidth=1,cut = 0,
                      palette={"n": "#224FDF", "y": "b"},saturation=0.75,ax =axs)


sns.despine(left=True, bottom=True)
axs.set_xticklabels(['- Mito', '+ Mito'],fontsize=9)
axs.set_ylabel(r'D$_{AZ}$ ($\mu$m)',fontsize=9,labelpad=0.3)
plt.legend([],[], frameon=False)

plt.tick_params(axis='both', which='major', labelsize=9,pad=0.3)


circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="b",mec='b')
circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="#224FDF",mec='#224FDF')

plt.legend((circ1, circ2),("MSB","SSB"), numpoints=1,loc='upper left',frameon = False,bbox_to_anchor=(0.7, 1.2,0.05,0.05),handletextpad=0.01,labelspacing=0.1,prop={'size': 7})
plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/dis_az_msb_con.png',dpi =600)

plt.show()