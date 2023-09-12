#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
from scipy import stats
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter,ScalarFormatter
import seaborn as sns
from scipy import stats

'''Plot distribution of mean distances and mean distances vs things
'''

params = {'axes.labelsize': 10,
           'axes.titlesize': 10,
          'legend.fontsize': 8,
           'xtick.labelsize': 8,
           'ytick.labelsize': 8,
            'figure.figsize': (4.5,4)}
            #'figure.figsize': (6.4, 6)}
mpl.rcParams.update(params)

med_dis_ltp =[]
med_dis_c =[]

g = open('./dis_az_chull/fw_az_dis_median.txt','r')
f = open('./dis_az_chull/fh_az_dis_median.txt','r')

s = open('./dis_az_chull/xr_az_dis_median.txt','r')
p = open('./dis_az_chull/fp_az_dis_median.txt','r')

for line in g:
    line_split = line.split()
    med_dis_ltp.append(float(line_split[1]))

for line in s:
    line_split = line.split()
    med_dis_ltp.append(float(line_split[1]))

for line in f:
    line_split = line.split()
    med_dis_c.append(float(line_split[1]))

for line in p:
    line_split = line.split()
    med_dis_c.append(float(line_split[1]))

#print(med_dis_c)
plt.figure(1)

bins = np.arange(0, 1,5e-2)

sns.histplot(data = med_dis_ltp,stat='probability', kde=True,bins= bins, color ='red')
sns.histplot(data = med_dis_c,stat='probability', kde=True,bins=bins, color = 'blue')

#bins = np.arange(0, 1,5e-2)
#hist, bin_edges = np.histogram((med_dis_c),bins)
#plt.bar(bin_edges[:-1], hist/len(med_dis_c), width = 5e-2, color = 'b', label ='C')

#yText1 = r'Mean : %.6f ($\mu m$)' %(np.round(np.mean(mec),decimals=5))
#yText2 = r'Mean : %.6f ($\mu m$)' %(np.round(np.mean(me_mc),decimals=5))
#yText3 = r'p value : %.6e' %(np.round(stats.ks_2samp(mec,me_mc)[1],decimals=6))
#plt.text(0.08,12, yText1, fontsize=9,color='b')
#plt.text(0.08,11, yText2, fontsize=9,color='r')
#plt.text(0.08,10, yText3, fontsize=9,color='r')

#print(np.median(me),np.median(me_m))
print('ltp_nm:',np.mean(med_dis_ltp),np.mean(med_dis_c),stats.mannwhitneyu(med_dis_ltp,med_dis_c)[1])
plt.xlabel(r'Med Dis AZ chull ($\mu m$)')
plt.ylabel('Frequency (#)')
#plt.xlim(0,0.1)
plt.legend(loc = 'upper right')
#plt.savefig('hist_var_dist_ctrl_ltp_NM')

#plt.figure(2)
##plt.plot(vol_mc,me_mc,'r o', label = 'LTP NMito')
#plt.plot(volc,mec,'b o', label = 'CTRL NMito')

#plt.ylabel(r'Median distance between vesicles ($\mu m$)')
#plt.xlabel(r'Bouton volume ($\mu m{^3}$)')
#plt.legend(loc ='upper left')
#plt.savefig('median_ves_dis_vs_b_vol_ctrl_ltp_NM')

plt.show()
