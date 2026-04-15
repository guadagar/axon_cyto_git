#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''This script loops over the distances and generates a text file with the median distance to the cluster's center
for all the boutons.
02.01.22
GCG
'''

folder_path = './dis_cm/xr/'
f = open('./dis_cm/xr_dis_ves_cm_median.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_ssvr')):
    x = filename.split('/')
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))
    a_di = np.array(di[di!= 0])

    f.write(xname)
    f.write('\t')
    f.write(str(np.median(a_di)))
    f.write('\t')
    f.write(str(np.std(a_di)))
    f.write('\n')
f.close()
