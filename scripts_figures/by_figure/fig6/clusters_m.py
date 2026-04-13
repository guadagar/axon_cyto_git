#!/usr/bin/env python

import numpy as np
import  matplotlib.pyplot as plt
import pickle
import pandas as pd
import matplotlib as mpl
import mpl_toolkits.mplot3d  # noqa: F401
from sklearn.cluster import KMeans
from sklearn import decomposition
from matplotlib.lines import Line2D
from scipy import stats
'''
This script generated the labels from PCA for the boutons with mito
GCG
'''
params = {'axes.labelsize': 10,
           'axes.titlesize': 10,
          'legend.fontsize': 6,
           'xtick.labelsize': 10,
           'ytick.labelsize': 10}
mpl.rcParams.update(params)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

data['den_ves'] = (data['nr_ves_b'])/data['final_chull_mvv_ax']
data['loc_den'] = 1/data['med_ass_ves_vol_final_ax']

d = data.loc[ (data['med_ass_ves_vol_final_ax'] > 0) & (data['mito_vol'])>0]
labels = d['Condition']

dim = 5
n = len (d['den_ves'])
X = np.zeros((n, dim))

var1 = np.log(d['den_ves'])  # d['den_ves'] #
var2 = np.log(d['final_med_mean_dis'])  # d['final_med_mean_dis'] #
var3 = np.log(d['loc_den'])  # d['med_ass_ves_vol_final_ax']#np.log(d['med_ass_ves_vol_final_ax'])
var4 = np.log(d['b_vol'])  # d['med_ass_ves_vol_final_ax']#np.log(d['med_ass_ves_vol_final_ax'])
var5 = np.log(d['disp_cm'])  # d['med_ass_ves_vol_final_ax']#np.log(d['med_ass_ves_vol_final_ax'])

for idx, (den, dis, vor,bsa, disp) in enumerate(zip(var1, var2, var3,var4,var5)):
    X[idx, 0] = ((den - np.median(var1)) / np.std(var1))
    X[idx, 1] = (dis - np.median(var2)) / np.std(var2)
    X[idx, 2] = (vor - np.median(var3)) / np.std(var3)
    X[idx, 3] = (bsa - np.median(var4)) / np.std(var4)
    X[idx, 4] = (disp - np.median(var5)) / np.std(var5)

pca = decomposition.PCA(n_components=dim)
pca.fit(X)
xt = pca.transform(X)

principalDf = pd.DataFrame(data = xt, columns = ['PC1','PC2','PC3','PC4','PC5'])#,'PC6'])
principalDf_red = pd.DataFrame(data = xt[:,0:2], columns = ['PC1','PC2'])

print('PC components',pca.components_)
print("Explained variance:", pca.explained_variance_ratio_)
print("Cumulative:", np.cumsum(pca.explained_variance_ratio_))

finalDf = principalDf_red.copy()
finalDf['Condition'] = labels

kmeans = KMeans(n_clusters = 2).fit(principalDf_red)
centroids_n = kmeans.cluster_centers_

labels = kmeans.labels_

#with open('./labels_m', 'wb') as f:
 #   pickle.dump(labels, f)

labels = pickle.load(open('./labels_m','rb'))

fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(2.66, 2.057))
fig.subplots_adjust(right=0.95, left = 0.26, bottom =0.25, top = 0.93)

labels_let = []
for i in labels:
    if i==1:
        labels_let.append('orange')
    else:
        labels_let.append('purple')

d['labels'] = labels_let


plt.scatter(d['den_ves'],d['final_med_mean_dis'],c=d['labels'],edgecolor="k",linewidths=0.4,s=5)

axs.set_ylabel(r'Dis Neigh SVs ($\mu m$)',fontsize=10,labelpad=0.01)
axs.set_xlabel(r'Global SV Den ($\mu m^{-3}$)',fontsize=10,labelpad=0.01)

plt.xscale('log')
plt.yscale('log')
plt.ylim(0.01,0.25) #med dis

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3, markerfacecolor="orange",markeredgewidth=1,mec='orange')
circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=3,markerfacecolor="purple",markeredgewidth=0.3,mec='purple')

plt.legend((circ1, circ2), ("Potentiated", "Stable"), numpoints=1,fontsize=6, loc="upper right", frameon = False)#, bbox_to_anchor=(-1.0, 1))

#plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/den_vs_dis_cluster.png',dpi =600)

ltp = d.loc[(d['labels'] == 'purple')]# & (data['med_ass_ves_vol_final_ax'] > 0 )]# & (data['pval_d_ves_ol'] <0.05)]
c = d.loc[(d['labels'] == 'orange')]# &  (data['med_ass_ves_vol_final_ax'] > 0 )]# & (data['pval_d_ves_ol'] <0.05)]


plt.show()