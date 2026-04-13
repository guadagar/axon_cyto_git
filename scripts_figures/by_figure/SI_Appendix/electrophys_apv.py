#!/usr/bin/env python
import  matplotlib.pyplot as plt
from scipy import stats
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np
'''
This script generates the electrophysiology image, fig S1
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6,
            'figure.figsize': (1.8,1.3)}
mpl.rcParams.update(params)

fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.95, left = 0.25, bottom =0.25, top = 0.87)

io = '../../../../latest_results/data/all_data_together/electrophysiology.xlsx'
data = pd.read_excel(io, sheet_name='2c_APVphys',nrows=80)
print(data['Time (min)'][0:80])

data['avg%control'] = data[['JB056 Control %', 'JB064 Control %']].mean(axis=1)
data['avg%LTP'] = data[['JB056 TBS %', 'JB064 TBS %']].mean(axis=1)
data['err%control'] = data[['JB056 Control %', 'JB064 Control %']].std(axis=1)/np.sqrt(2)
data['err%LTP'] = data[['JB056 TBS %', 'JB064 TBS %']].std(axis=1)/np.sqrt(2)

plt.errorbar(data['Time (min)'], data['avg%control'],yerr = data['err%control'], fmt='.', color='b',markersize=1,markeredgewidth=0.1,elinewidth=0.3,label = 'APV-Control')
plt.errorbar(data['Time (min)'], y = data['avg%LTP'], yerr = data['err%LTP'] , fmt='.', color='r',markersize=1,markeredgewidth=0.1,elinewidth=0.3,label = 'APV-LTP')

for spine in axs.spines.values():
    spine.set_linewidth(0.5)  # Set the thickness to 0.5

plt.ylim(0,350)
plt.xlim(-40,125)
plt.legend(frameon = False, loc='upper right')
plt.ylabel(r'% fEPSP Baseline')
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)
axs.set_xlabel(r'Time (min)',fontsize=6,labelpad=0.3)
axs.set_xticks([0,40,80,120])

#plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/apv_baseline.png', dpi = 600)

io = '../../../../latest_results/data/all_data_together/electrophysiology.xlsx'
#
data1 = pd.read_excel(io, sheet_name='2c_APVwaveforms',skiprows = 1)


fig, axs = plt.subplots(figsize=(0.2, 0.2))
fig.subplots_adjust(right=0.99, left = 0.05, bottom =0.15, top = 0.87)
#
plt.plot(data1['time (msec)'],data1['JB056-stim2-Ctrl Baseline'],'k',linewidth=0.1)
plt.plot(data1['time (msec)'],data1['JB056-stim2-Ctrl post-TBS'],'b',linewidth=0.1)

plt.xlim(0,25)
plt.ylim(-0.04,0.02)
plt.axis('off')
#
plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/apv_waveform_ctrl.png', dpi = 1500)
#
fig, axs = plt.subplots(figsize=(0.2, 0.2))
fig.subplots_adjust(right=0.99, left = 0.05, bottom =0.15, top = 0.87)
fig.subplots_adjust(right=0.99, left = 0.1, bottom =0.15, top = 0.87)
#
plt.plot(data1['time (msec)'],data1['JB056-Stim1-TBS Baseline'],'k',linewidth=0.1)
plt.plot(data1['time (msec)'],data1['JB056-Stim1-TBS post-TBS'],'r',linewidth=0.1)
plt.axis('off')
plt.xlim(0,25)
plt.ylim(-0.04,0.02)

plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/apv_waveform_ltp.png', dpi = 1500)
plt.show()
#
