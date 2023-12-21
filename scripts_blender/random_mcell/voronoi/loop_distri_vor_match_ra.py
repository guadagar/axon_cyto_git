    #!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os,glob
from scipy.stats import variation
import csv
from scipy.stats import skew
import pandas as pd

folder_path = './fh_vor'

f = open('fh_vor_med_distri_stats_v3.txt','w')

na = []

data = pd.read_csv('../../../../data/all_data.csv')

#xr = data.loc[(data['Condition'] == 'LTP')  & (data['Animal'] == 'JB023')]
#fp = data.loc[(data['Condition'] == 'Control')  & (data['Animal'] == 'JB023')]
fh = data.loc[(data['Condition'] == 'Control')  & (data['Animal'] == 'JB024')]
#fw = data.loc[(data['Condition'] == 'LTP')  & (data['Animal'] == 'JB024') ]

for name_cloud, nr_ves in zip(fh['name'], fh['nr_ves_in']):
    na.append(name_cloud)


name_match = [] # to save in a list
vor_match = []
vol_match = []
nr_ves_match =[]
n_ves_files = 0
n_ves_files_m = 0
#I read all the voronoi volumes with intersection
for filename in glob.glob(os.path.join(folder_path,'*.txt')):
#for filename in glob.glob(os.path.join(folder_path,'d02c32Dax56_ssvr_vor_vol.txt')):
    n_ves_files += 1
    x = filename.split('/')
    name = x[2].split('_')[0]
    #print(name)
    vor_final = []

    vor_vol_winter = []
    name_vor_winter = []

    #upload all the volumes with the intersection
    p = open(filename,'r')
    lines = p.readlines()[1:]
    p.close()
#    print(filename)
    for line in lines:
        #print(line)
        vor_vol_winter.append(float(line.split()[2]))
        print(line.split()[0].split('_'))
        name_vor_winter.append(float(line.split()[0].split('_')[4]))

    # upload all the volumes without intersection
    filename1 = name + '_ssvr_ra.txt'
    folder_path1 = './fh_vor_original'

    #save the voronoi that were not intersected (?)
    filename2 = name + '_ssvr.txt'
    folder_path2 = './fh_vor_con/'
    file = open(os.path.join(folder_path2,filename2),'w')
    try:
        p = open(os.path.join(folder_path1,filename1),'r')
        lines = p.readlines()
        p.close()
        vor_vol = []
        name_vor = []
        for line in lines:
            #print(line)
            vor_vol.append(float(line.split()[1]))
            name_vor.append(float(line.split()[0]))
        #print(name)
        for i,j in enumerate(vor_vol_winter):
                #print(name,j,(vor_vol[name_vor.index(int(name_vor_winter[i]))]),vor_vol[name_vor.index(int(name_vor_winter[i]))] - j)
                if (vor_vol[name_vor.index(int(name_vor_winter[i]))] - j) < 1e-8:
                    #print(name_vor_winter[i],np.round(vor_vol[name_vor.index(int(name_vor_winter[i]))],decimals = 9), np.round(j, decimals = 9))
                    vor_final.append(vor_vol[name_vor.index(int(name_vor_winter[i]))])
                    #print()
                    file.write(str(name_vor.index(int(name_vor_winter[i]))))
                    file.write('\t')
                    file.write(str(vor_vol[name_vor.index(int(name_vor_winter[i]))]))
                    file.write('\n')


        if vor_final!=[] and name in na:
            avor = np.array(vor_final)
            #print(avor[p5_nl], np.std(avor[p5_nl]))
            j = na.index(name)
            #print('empty',name)
            #print(x[2].split('_')[0], mito[j])
            avor = np.array(vor_final)
            n_ves_files_m +=1
            f.write(str(name))
            f.write('\t')
            f.write(str(np.median(avor)))
            f.write('\t')
            f.write(str(np.std(avor)))
            f.write('\t')
            f.write(str(skew(avor)))
            f.write('\n')
        else:
            print('no esta',name, vor_final)

    except FileNotFoundError:
        print(name,'no file')


f.close()
