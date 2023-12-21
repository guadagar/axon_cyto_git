#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
from scipy.stats import skew
from scipy.stats import norm
from scipy import stats
import os,glob

folder_path = './latest_blend_11_22/dis_ves_ol/fw/'

f2s = open('fw_pval_distri_dol_ax.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_ssvr')):

    x = filename.split('/')
    xname = x[4].split('_')[0]
    #print(xname)
    di_ol_name = './latest_blend_11_22/dis_ves_ol/fw/'+xname+'_ssvr' #dist_ol - sigue asi

    try:
        di = pickle.load(open(di_ol_name,'rb'))
        a_di = np.array(di[di!= 0])
    except:
        print('no di')

    #distance OL
    file_path_name2 = './latest_blend_11_22/mcell_sim/chull_axon/mcell_sim_all/random/dis_ves_ol/fw/'+xname+'_ssvr_ra'

    try:
        di = pickle.load(open(file_path_name2,'rb'))
        a_di1 = np.array(di[di!= 0])
        print('dis',xname,stats.mannwhitneyu(a_di, a_di1)[1])
        f2s.write(str(xname))
        f2s.write('\t')
        f2s.write(str(stats.mannwhitneyu(a_di, a_di1)[1]))
        f2s.write('\n')
    except:
        print('No,random',xname)
