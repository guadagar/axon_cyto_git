#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation,normaltest,shapiro
import csv


'''Loop over the distances to get the media
12.1.22
GCG
'''

#folder_path = './latest_blend_02_22/dist_ves_latest/fp/'
#folder_path = './latest_blend_02_22/APV_05_22/dis_ves/CVZ'
folder_path = './dist_ves_latest/xr/'

#f = open('./del_dist_latest/APV/cvz_del_ves_distri_stats.txt','w')
f = open('./del_ves_distri_xr_med_mean.txt','w')

na = []
mito =[]
vol = []
ves_nr = []
sa = []
n_ves_files = 0
not_normal = 0

for filename in glob.glob(os.path.join(folder_path,'*ssvr')):
    n_ves_files += 1
    x = filename.split('/')
    di = pickle.load(open(filename,'rb'))
    shapiro_test = shapiro(np.log(di))
    if shapiro_test.pvalue > 0.05:
        print('probably normal')
    else:
        print('not normal')
        not_normal += 1

    #print(x, x[5].split('s'))

   # if x[4].split('_')[0] in na:
    #    j = na.index(x[4].split('_')[0])
        #print(filename, mito[j])
        #if mito[j]=='y' or mito[j]=='yes':
        #    n_ves_files_m +=1
#--------final usage ----------
    #f.write(x[5].split('s')[0])
    f.write(x[3].split('_')[0])
    f.write('\t')
    f.write(str(np.median(di)))
    f.write('\t')
    f.write(str(np.std(di)))
#    f.write('\t')
    #f.write(str(np.median(di)))
    f.write('\n')
f.close()
#print(n_ves_files,not_normal)
