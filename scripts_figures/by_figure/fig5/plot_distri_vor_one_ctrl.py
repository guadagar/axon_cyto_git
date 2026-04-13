#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import matplotlib as mpl
from matplotlib.lines import Line2D
import types

'''
This script generates fig 5 panel c
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.5,1.1)}
mpl.rcParams.update(params)

vor_vol = []
name = 'd03c33ax14'#'d01c06ax02'#'d03c24ax40'
filename = '../../../../latest_results/latest_blend_11_22/voronoi_vol/fh/fh_vor_con/'+name+'_ssvr.txt'
fh_ves_vol = 0.00003104361
p = open(filename,'r')
lines = p.readlines()[1:]
p.close()
n = 0
for line in lines:
    #print(line)
    vor_vol.append(float(line.split()[1]))
    n = n + 1

#con intersection
vor_vol3 = []
filename = '../../../../latest_results/latest_blend_11_22/mcell_sim/mcell_sim_all/random/FH/fh_vor_con/'+name+'_ssvr.txt'
p = open(filename,'r')
lines = p.readlines()[1:]
p.close()
n3 = 0
for line in lines:
    vor_vol3.append(float(line.split()[1]))
    n3 = n3 + 1
print('ltp-vor',np.median(vor_vol),np.median(vor_vol3), stats.mannwhitneyu(vor_vol3, vor_vol)[1])

w = 5e-5
bins = np.arange(0, 1.5e-3,w)

aov_l = np.array(vor_vol) - fh_ves_vol

aov_l3 = np.array(vor_vol3) - fh_ves_vol

fig, ax = plt.subplots(figsize=(1.5, 1.1))
fig.subplots_adjust(right=0.93, left = 0.25, bottom =0.3, top = 0.98)

sns.histplot(data = aov_l,stat='probability', kde=True,line_kws={'lw': 1}, bins= bins, color ='b', label = 'Control')

sns.histplot(data = aov_l3,stat='probability', kde=True,line_kws={'lw': 1},bins= bins, color ='skyblue', label ='Control RD')


formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)

formatter.set_powerlimits((0,0))
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks([0,0.5e-3,1e-3])
ax.set_ylabel(r'Frequency (#/N)',fontsize=6,labelpad=0.01)
ax.set_xlabel(r'AVol$\rm_{SV}$ ($\mu m{^3}$)',fontsize=6,labelpad=0.01)#, x=0, ha='left')

pad = plt.rcParams["xtick.major.size"] + plt.rcParams["xtick.major.pad"]
def bottom_offset(self, bboxes, bboxes2):
    bottom = self.axes.bbox.ymin
    self.offsetText.set(va="top", ha="left")
    oy = bottom - pad * self.figure.dpi / 72.0
    self.offsetText.set_position((0.8, oy))

ax.xaxis._update_offset_text_position = types.MethodType(bottom_offset, ax.xaxis)

circ1 = Line2D([0], [0], linestyle="none", marker="s",  markersize=2, markerfacecolor="b",mec='b')
circ2 = Line2D([0], [0], linestyle="none", marker="s",  markersize=2, markerfacecolor="skyblue",mec='skyblue')
plt.legend((circ1, circ2), ("Control","Control RD"), numpoints=1, loc="upper right", frameon = False,handletextpad=0.01,labelspacing=0.1)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/'+name+'_vor_distri_control.png',dpi = 600)
plt.show()
