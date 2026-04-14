#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''This script goes over all the distances to the AZ for each cluster of SVs and generate a text file with the median distance.
I consider all the active zones present at a given bouton and for each vesicle I get the minimum distance
02.01.22
GCG
'''
#with all the distances
folder_path = './dis_az_latest/fp/'
f = open('./dis_az_latest/fp_az_dis.txt','w')
#g = open('fh_az_dis_nmito_n.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_az_dis')):
    x = filename.split('/')
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))
    di_min = []
    for i in range(len(di)):
        di_min.append(np.min(di[i,:]))
    di = np.array(di_min)
    #print(filename, np.mean(di_min))
    f.write(xname)
    f.write('\t')
    f.write(str(np.median(di)))
    f.write('\t')
    f.write(str(np.std(di)))
    f.write('\n')
f.close()
