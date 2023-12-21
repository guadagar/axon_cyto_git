#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
from scipy.stats import skew
from scipy.stats import norm
from scipy import stats
import os,glob

folder_path = './xr/xr_vor_con/'

f2s = open('xr_pval_distri_vor_ax.txt','w')


for filename in glob.glob(os.path.join(folder_path,'*_ssvr.txt')):
    x = filename.split('/')
    #print(filename.split('/')[3])
    xname = x[3].split('_')[0]
    #print(xname)
    vor_vol = []
    file2open = os.path.join(folder_path,xname+'_ssvr.txt')
    p = open(file2open,'r')
    lines = p.readlines()[1:]
    p.close()
    n = 0
    for line in lines:
        vor_vol.append(float(line.split()[1]))
        n = n + 1
    vor_vol_ra = []
    file_path_name1 = './random/xr/xr_vor_con/'+xname+'_ssvr.txt'
    #print(filename)
    try:
        p = open(file_path_name1,'r')
        lines = p.readlines()[1:]
        p.close()
        print('esta',xname)
        n_ra = 0
        for line in lines:
            vor_vol_ra.append(float(line.split()[1]))
            n_ra = n_ra + 1
        #print(vor_vol_ra)
        # #print('Ra-LTP',xname,'stats',stats.mannwhitneyu(vor_vol_ra, vor_vol)[1])
        print(xname,stats.mannwhitneyu(vor_vol_ra, vor_vol)[1])
        f2s.write(str(xname))
        f2s.write('\t')
        f2s.write(str(stats.mannwhitneyu(vor_vol_ra, vor_vol)[1]))
        f2s.write('\t')
        f2s.write(str(np.std(vor_vol)/np.mean(vor_vol)))
        f2s.write('\t')
        f2s.write(str(np.std(vor_vol_ra)/np.mean(vor_vol_ra)))
        f2s.write('\n')
    #print('LTP-Ra', 'med vor:',np.median(vor_vol),np.median(vor_vol_ra), 'stats:',stats.mannwhitneyu(vovor_vol_ra, vor_vol)[1])
    except:
        #continue
        print('No,random',xname)

f2s.close()
