#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
import os
from scipy.stats import skew
from scipy.stats import norm

#con intersection
name = 'd02c19ax46'
filename = './dis_ves_ol/fw/'+name+'_ssvr'
di = pickle.load(open(filename,'rb'))
print('ltp',skew(di), np.median(di), len(di))


name = 'd03c07ax07'
filename = './dis_ves_ol/fh/'+name+'_ssvr'
di1 = pickle.load(open(filename,'rb'))
print('ltp',skew(di1), np.median(di1), len(di1))

#distance OL
# filename = './latest_blend_11_22/dis_ves_ol/xr/'+name+'_ssvr'
# di = pickle.load(open(filename,'rb'))
# print('ltp',np.median(di))
#
# vor_vol1 = []
# filename = './new_vor/new_blend_vor/xr_vor_original/'+ name +'_ssvr.txt'
# p = open(filename,'r')
# lines = p.readlines()[1:]
# p.close()
# n1 = 0
# for line in lines:
#     vor_vol1.append(float(line.split()[1]))
#     n1 = n1 + 1
# #
# print('ltp-original',skew(vor_vol1),np.median(vor_vol1),n1)
#
# #con intersection
# vor_vol3 = []
# filename = './latest_blend_11_22/mcell_sim/mcell_sim_all/random/xr_vor_con/'+name+'_ssvr.txt'
# p = open(filename,'r')
# lines = p.readlines()[1:]
# p.close()
# n3 = 0
# for line in lines:
#     vor_vol3.append(float(line.split()[1]))
#     n3 = n3 + 1
# print('ltp',skew(vor_vol3),np.median(vor_vol3),n3)
#
# #distance OL
# filename = './latest_blend_11_22/mcell_sim/mcell_sim_all/random/dis_ves_ol/xr/'+name+'_ssvr_ra'
# di = pickle.load(open(filename,'rb'))
# print('ltp',np.median(di))
#
# # name = 'd01c10ax03'
# # filename = '../latest_blend_11_22/mcell_sim/mcell_sim_all/random/dis_ves_ol/xr/'+name+'_ssvr.txt'
# #
# # for line in lines:
# #     print(line)
# #     vor_vol.append(float(line.split()[1]))
# #     n = n + 1
# # print('ltp',skew(vor_vol), np.median(vor_vol),n)
# #
# vor_vol4 = []
# filename = './latest_blend_11_22/mcell_sim/mcell_sim_all/random/xr_vor_original/'+name+'_ssvr_ra.txt'
# p = open(filename,'r')
# lines = p.readlines()[1:]
# p.close()
# n4 = 0
# for line in lines:
#     vor_vol4.append(float(line.split()[1]))
#     n4 = n4 + 1
# print('ltp-original-ra',skew(vor_vol4),np.median(vor_vol4),n4)


w = 5e-2
bins = np.arange(0, 1,w)
#ov_l = #[(i - v)/v  for i in vor_vol]
#ov1_l = #[(i - v)/v  for i in vor_vol1]
#ov_c = #[(i - v)/v  for i in vor_vol2]

aov_l = np.array(di)
aov_l1 = np.array(di1)
#aov_l3 = np.array(vor_vol3)



#print(np.median(ov_l),np.median(ov_c))
plt.figure(1)

hist, bin_edges = np.histogram((aov_l),bins)
plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'r', label ='LTP',alpha =0.5)

hist, bin_edges = np.histogram((aov_l1),bins)
plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'b', label ='C',alpha =0.5)

#hist, bin_edges = np.histogram((aov_l3),bins)
#plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'g', label ='random',alpha =0.5)

#hist, bin_edges = np.histogram((aov_c1),bins)
#plt.bar(bin_edges[:-1], hist/len(hist), width = w, color = 'lightblue', label ='CTRL',alpha =0.8)

plt.ylabel('Frequency (#/N)')
plt.xlabel(r'Dis Ves OL')
plt.legend()
#plt.savefig('two_distri_vol_ssb_nm')
plt.show()
