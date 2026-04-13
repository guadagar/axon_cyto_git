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
This scrip generates the labels from PCA
GCG
'''

params = {'axes.labelsize': 6,
           'axes.titlesize': 6,
          'legend.fontsize': 6,
           'xtick.labelsize': 6,
           'ytick.labelsize': 6}
mpl.rcParams.update(params)

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')

data['den_ves'] = (data['nr_ves_b'])/data['final_chull_mvv_ax']
data['loc_den'] = 1/data['med_ass_ves_vol_final_ax']

d = data.loc[  (data['med_ass_ves_vol_final_ax'] > 0) & (data['mito_vol'] == 0)]
dm = data.loc[ (data['med_ass_ves_vol_final_ax'] > 0) & (data['mito_vol'] > 0)]

labels = d['Condition']

dim = 5
n = len (d['den_ves'])
X = np.zeros((n, dim))

var1 = np.log(d['den_ves'])
var2 = np.log(d['final_med_mean_dis'])
var3 = np.log(d['loc_den'])
var4 = np.log(d['b_vol'])
var5 = np.log(d['disp_cm'])

for idx, (den, dis, vor,bsa, disp) in enumerate(zip(var1, var2, var3,var4,var5)):
    X[idx, 0] = ((den - np.median(var1)) / np.std(var1))
    X[idx, 1] = (dis - np.median(var2)) / np.std(var2)
    X[idx, 2] = (vor - np.median(var3)) / np.std(var3)
    X[idx, 3] = (bsa - np.median(var4)) / np.std(var4)
    X[idx, 4] = (disp - np.median(var5)) / np.std(var5)

pca = decomposition.PCA(n_components=dim)
pca.fit(X)
xt = pca.transform(X)

principalDf = pd.DataFrame(data = xt, columns = ['PC1','PC2','PC3','PC4','PC5'])
principalDf_red = pd.DataFrame(data = xt[:,0:2], columns = ['PC1','PC2'])

print('PC components',pca.components_)
print("Explained variance:", pca.explained_variance_ratio_)
print("Cumulative:", np.cumsum(pca.explained_variance_ratio_))

finalDf = principalDf_red.copy()
finalDf['Condition'] = labels

kmeans = KMeans(n_clusters = 2).fit(principalDf_red)
centroids_n = kmeans.cluster_centers_

labels = kmeans.labels_

#with open('./labels_nm', 'wb') as f:
 #   pickle.dump(labels, f)

labels = pickle.load(open('./labels_nm','rb'))

fig, axs = plt.subplots(figsize=(1.7, 1.3))
fig.subplots_adjust(right=0.97, left = 0.25, bottom =0.23, top = 0.98)

labels_let = []
for i in labels:
    if i==1:
        labels_let.append('purple')
    else:
        labels_let.append('orange')


d['labels'] = labels_let

labels_m = pickle.load(open('./labels_m','rb'))
labels_letm = []
for i in labels_m:
    if i==1:
        labels_letm.append('yellow')
    else:
        labels_letm.append('green')

dm['labels'] = labels_letm

plt.scatter(d['den_ves'],d['final_med_mean_dis'],c=d['labels'],edgecolor="gray",linewidths=0.2,s=3,zorder=10)
plt.scatter(dm['den_ves'],dm['final_med_mean_dis'],c=dm['labels'],edgecolor="gray",linewidths=0.2,s=3,zorder=10)

d_p = d.loc[(d['labels'] == 'purple')] #CONTROL/Stable -M
d_o = d.loc[(d['labels'] == 'orange')] #LTP/Potentiated -M

d_y = dm.loc[(dm['labels'] == 'yellow')] #LTP/Potentiated +M
d_g = dm.loc[(dm['labels'] == 'green')] #CONTROL/Stable +M

slopecnm, interceptcnm, r_valuecnm, p_valuec, std_errc = stats.linregress(np.log(d_p['den_ves']),np.log(d_p['final_med_mean_dis']))
slopenm, interceptnm, r_valuenm, p_value, std_err = stats.linregress(np.log(d_o['den_ves']),np.log(d_o['final_med_mean_dis']))

a = np.exp(interceptcnm)
b = slopecnm
x = d_p['den_ves']
plt.plot(x, a*(x**b),color='purple',zorder=5)

a1 = np.exp(interceptnm)
b1 = slopenm
x1 = d_o['den_ves']
plt.plot(x1, a1*(x1**b1),color='orange',zorder=5)

slopecm, interceptcm, r_valuecm, p_valuecm, std_errcm = stats.linregress(np.log(d_g['den_ves']),np.log(d_g['final_med_mean_dis']))
slopem, interceptm, r_valuem, p_valuem, std_errm = stats.linregress(np.log(d_y['den_ves']),np.log(d_y['final_med_mean_dis']))

a = np.exp(interceptcm)
b = slopecm
x = d_g['den_ves']
plt.plot(x, a*(x**b),color='green',zorder=5)

a1 = np.exp(interceptm)
b1 = slopem
x1 = d_y['den_ves']
plt.plot(x1, a1*(x1**b1),color='yellow',zorder=5)

yText1 = r'R$^2$ = %.2f ' %(np.round(r_valuecnm**2,decimals=2))
yText2 = r'R$^2$ = %.2f ' %(np.round(r_valuenm**2,decimals=2))
yText3 = r'R$^2$ = %.2f ' %(np.round(r_valuecm**2,decimals=2))
yText4 = r'R$^2$ = %.2f ' %(np.round(r_valuem**2,decimals=2))
#dis
plt.text(860,0.019, yText1, fontsize=6,color='purple')#Control -M
plt.text(860,0.025, yText2, fontsize=6,color='orange')
plt.text(860,0.012, yText3, fontsize=6,color='green') #Contol +M
plt.text(860,0.015, yText4, fontsize=6,color='gold')

axs.set_ylabel(r'D$\rm_{Neigh}$ ($\mu m$)',fontsize=6,labelpad=0.01)
axs.set_xlabel(r'SV Den$\rm_{C}$ ($\mu m^{-3}$)',fontsize=6,labelpad=0.01)

plt.xscale('log')
plt.yscale('log')

plt.ylim(0.01,0.25) #med dis

circ1 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="orange",markeredgewidth=0.2,mec='gray')
circ2 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2,markerfacecolor="purple",markeredgewidth=0.2,mec='gray')
circ3 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2, markerfacecolor="yellow",markeredgewidth=0.2,mec='gray')
circ4 = Line2D([0], [0], linestyle="none", marker="o",  markersize=2,markerfacecolor="green",markeredgewidth=0.2,mec='gray')

plt.legend((circ1, circ2,circ3,circ4), ("Potentiated -M", "Stable -M","Potentiated +M", "Stable +M"),fontsize = 6, numpoints=1,loc = 'upper left',mode ='expand', ncol=2, frameon = False,prop={'size': 5}, labelspacing=0.1,borderaxespad=0.001,handletextpad=0.01, handlelength=0.7)
#plt.savefig('/Users/guadagar/Documents/trabajo/mito_project/axon_cytoplasm/figures/new_5_2025/den_vs_dis_all_w_reg_clusters.png',dpi =600)


plt.show()