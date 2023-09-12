#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv

'''New code that loops over the distances and generate text files with the minimum distance to the active zone
I consider all the active zones present and for each vesicle I get the minimum distance
02.01.22
GCG
'''


folder_path = './dis_cm_az/fh/'
f = open('./dis_cm_az/fh_az_dis_median.txt','w')
#g = open('fh_az_dis_nmito_n.txt','w')

for filename in glob.glob(os.path.join(folder_path,'*_az_dis_cm')):
    x = filename.split('/')
    xname = x[3].split('_')[0]
    di = pickle.load(open(filename,'rb'))

    di_min = []
    for i in range(len(di)):
        di_min.append(np.min(di[i,:]))
    di = np.array(di_min)
    #print(xname,di[0])
    print(filename, np.mean(di_min))
    f.write(xname)
    f.write('\t')
    f.write(str(di[0]))
    #f.write('\t')
    #f.write(str(np.std(di)))
    f.write('\n')
f.close()
