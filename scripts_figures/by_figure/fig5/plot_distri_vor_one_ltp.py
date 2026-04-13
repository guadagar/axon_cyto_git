#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import matplotlib as mpl
import types
from matplotlib.lines import Line2D

'''
This script generates fig 5 panel e
GCG
'''


params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}

mpl.rcParams.update(params)


vor_vol = []
name = 'd01c14ax04'
filename = '../../../../latest_results/latest_blend_11_22/voronoi_vol/fw/fw_vor_con/'+name+'_ssvr.txt'
ves_vol_fw = 0.00004768875 #um3

p = open(filename,'r')
lines = p.readlines()[1:]
p.close()
n = 0
for line in lines:
    vor_vol.append(float(line.split()[1]))
    n = n + 1

#con intersection
vor_vol3 = []
filename = '../../../../latest_results/latest_blend_11_22/mcell_sim/mcell_sim_all/random/FW/fw_vor_con/'+name+'_ssvr.txt'
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

aov_l = np.array(vor_vol) - ves_vol_fw
aov_l3 = np.array(vor_vol3) - ves_vol_fw

fig, ax = plt.subplots(figsize=(1.5, 1.1))
fig.subplots_adjust(right=0.92, left = 0.25, bottom =0.3, top = 0.98)

sns.histplot(data = aov_l,stat='probability', kde=True,line_kws={'lw': 1}, bins= bins, color ='r', label = 'LTP')

sns.histplot(data = aov_l3,stat='probability', kde=True,line_kws={'lw': 1},bins= bins, color ='#F08080', label ='LTP RD')

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
ax.xaxis.set_major_formatter(formatter)
formatter.set_powerlimits((-1,1))
ax.xaxis.set_major_formatter(formatter)
ax.set_xticks([0,0.5e-3,1e-3])

ax.set_ylabel(r'Frequency (#/N)',fontsize=6,labelpad=0.01)
ax.set_xlabel(r'AVol$\rm_{SV}$ ($\mu m{^3}$)',fontsize=6,labelpad=0.01)

pad = plt.rcParams["xtick.major.size"] + plt.rcParams["xtick.major.pad"]
def bottom_offset(self, bboxes, bboxes2):
    bottom = self.axes.bbox.ymin
    self.offsetText.set(va="top", ha="left")
    oy = bottom - pad * self.figure.dpi / 72.0
    self.offsetText.set_position((0.8, oy))

ax.xaxis._update_offset_text_position = types.MethodType(bottom_offset, ax.xaxis)

circ1 = Line2D([0], [0], linestyle="none", marker="s",  markersize=2, markerfacecolor="r",mec='r')
circ2 = Line2D([0], [0], linestyle="none", marker="s",  markersize=2, markerfacecolor="#F08080",mec='#F08080')
plt.legend((circ1, circ2), ("LTP","LTP RD"), numpoints=1, loc="upper right", frameon = False,handletextpad=0.01,labelspacing=0.1)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/'+name+'_vor_distri_LTP.png',dpi = 600)

plt.show()
