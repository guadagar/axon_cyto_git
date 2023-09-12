#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''
GCG
'''


folder_path = './dis_ves_ol/fp/'
f = open('./dis_ves_ol/fp_stats.txt','w')
#g = open('fh_az_dis_nmito_n.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_ssvr')):
    x = filename.split('/')
    #print(x)
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))
    #print(di[di!= 0])
    a_di = np.array(di[di!= 0])
    #print(filename, np.mean(di_min))
    f.write(xname)
    f.write('\t')
    f.write(str(np.median(a_di)))
    f.write('\t')
    f.write(str(np.std(a_di)))
    f.write('\n')
f.close()
