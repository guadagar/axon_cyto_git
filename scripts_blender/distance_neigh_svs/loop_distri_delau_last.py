#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation,normaltest,shapiro
import csv


'''This script goes over all the distances to get the median & sd of the distributions
12.1.22
GCG
'''
#input path
folder_path = './dis_ves/FHLTD/'

#name output file
f = open('./del_ves_distri_fh_med_mean.txt','w')

n_ves_files = 0
not_normal = 0

for filename in glob.glob(os.path.join(folder_path,'*ssvr')):
    n_ves_files += 1
    x = filename.split('/')
    di = pickle.load(open(filename,'rb'))

#--------save the data----
    f.write(x[3].split('_')[0])
    f.write('\t')
    f.write(str(np.median(di)))
    f.write('\t')
    f.write(str(np.std(di)))
    f.write('\n')
f.close()
