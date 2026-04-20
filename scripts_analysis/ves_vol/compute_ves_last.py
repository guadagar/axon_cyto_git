#!/usr/bin/env python
import numpy as np
import  matplotlib.pyplot as plt
import pickle
import csv
from scipy import stats

'''
I do boostraping to estimate the volume of the vesicles
'''

mi = []
rad = []
with open('../latest_results/data/vesicles/xr_ves.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        #print(float(row[3]),row[5])
        rad.append(float(row[3]))
        mi.append(row[5])

idx_m = []
idx_nm = []

for i,j in enumerate(mi):
    if j=='y':
        idx_m.append(i)
    else:
        idx_nm.append(i)

a_rad = np.array(rad)

rad_nm = a_rad[idx_nm]
rad_m = a_rad[idx_m]

sampled_ves_vol_nm = (4.0/3.0)*np.pi*rad_nm**3
sampled_ves_vol_m = (4.0/3.0)*np.pi*rad_m**3

f = open('../latest_results/data/vesicles/tot_ves_vol_xr.txt','w')

name = []
nrv = []
miv = []

with open('../latest_results/data/all_data_together/xr_all_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader, None)
    for row in reader:
        name.append(row[0])
        nrv.append(float(row[3]))
        miv.append(float(row[5]))

idx_m = []
idx_nm = []

for i,j in enumerate(miv):
    if j==0:
        idx_nm.append(i)
    else:
        idx_m.append(i)

a_nrv = np.array(nrv)

nrv_nm = a_nrv[idx_nm]
na_nm =[]
for i in idx_nm:
    na_nm.append(name[i])

nrv_m = a_nrv[idx_m]
na_m = []
for i in idx_m:
    na_m.append(name[i])

nrep = 10000 #number of times I repeat
f_ves_vol_nm = np.zeros((2,len(nrv_nm)))
for i,j in enumerate(nrv_nm):
    ves_tot = np.zeros((nrep))
    for k in range(0,nrep):
        #rad_nm = stats.norm.rvs(loc=mu_nm, scale=sigma_nm, size=int(j), random_state=rng)
        x = np.random.choice(sampled_ves_vol_nm,size = int(j), replace = True)
        ves_vol_nm = x
        ves_tot[k] = np.sum(ves_vol_nm)
        #plt.errorbar(k,np.mean(ves_tot[np.nonzero(ves_tot)])/j,marker = 'o',color='r')
    f_ves_vol_nm[0,i] = np.mean(ves_tot) #Mean
    f_ves_vol_nm[1,i] = np.std(ves_tot) #SEM
    #plt.errorbar(np.arange(100),(4/3.0)*np.pi*(mu_nm)**3*1e-9*np.ones(100),marker = 'o',color='k')

f_ves_vol_m = np.zeros((2,len(nrv_m)))

for i,j in enumerate(nrv_m):
    ves_tot = np.zeros((nrep))
    for k in range(0,nrep):
        x = np.random.choice(sampled_ves_vol_m, size = int(j), replace=True)
        ves_vol_m = x
        ves_tot[k] = np.sum(ves_vol_m)
    f_ves_vol_m[0,i] = np.mean(ves_tot)
    f_ves_vol_m[1,i] = np.std(ves_tot)

for i,j in enumerate(nrv_nm):
    #print(f_ves_vol_nm[0,i]/j)
    f.write(na_nm[i])
    f.write('\t')
    f.write(str(f_ves_vol_nm[0,i])) #mean
    f.write('\t')
    f.write(str(f_ves_vol_nm[1,i])) #std
    f.write('\t')
    f.write(str(j)) #std
    f.write('\n')

for i,j in enumerate(nrv_m):
    #print(f_ves_vol_nm[0,i]/j)
    f.write(na_m[i])
    f.write('\t')
    f.write(str(f_ves_vol_m[0,i])) #mean
    f.write('\t')
    f.write(str(f_ves_vol_m[1,i])) #std
    f.write('\t')
    f.write(str(j)) #std
    f.write('\n')

plt.show()
