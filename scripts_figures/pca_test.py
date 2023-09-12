#!/usr/bin/python
from os import system
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
import csv
import pandas as pd
'''
This script calculates the PCA of a dataset, it gives back the eigenvalues and vectors, along with
the percentage variance
GCG
11.20
'''


data = pd.read_csv('../../../latest_results/data/all_data_together/all_data.csv')

#data['cyto_per'] = 100*(data['b_vol']-data['mito_vol']-data['mean_ves_vol'])/data['b_vol']
data['mito_per'] = 100*(data['mito_vol'])/data['b_vol']
#data['ves_per'] = 100*(data['mean_ves_vol'])/data['b_vol']

data['den'] = data['nr_ves']/data['convex_hull_inter_mito']
data['dis_ves'] = data['final_med_mean_dis']

ltp = data.loc[(data['Condition'] == 'LTP') & (data['final_dis_AZ']>0) & (data['med_ass_ves_vol']>0)]
c = data.loc[(data['Condition'] == 'Control') & (data['final_dis_AZ']>0) & (data['med_ass_ves_vol']>0)]

nd = 6
n = len(data)
x = np.zeros((n,nd))

x[:,0] = data['dis_ves']/np.std(data['dis_ves'])
x[:,1] = data['med_ass_ves_vol']/np.std(data['med_ass_ves_vol'])
x[:,2] = data['den']/np.std(data['den'])
x[:,3] = data['disp_cm']/np.std(data['disp_cm'])
x[:,4] = data['b_sa']/np.std(data['b_sa'])
x[:,5] = data['nr_ves']/np.std(data['nr_ves'])

#fig = plt.figure(1, figsize=(4, 3))
fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.15, top = 0.87)

y = np.zeros((n,nd))

y[:,0] = x[:,0] - np.mean(x[:,0])
y[:,1] = x[:,1] - np.mean(x[:,1])
y[:,2] = x[:,2] - np.mean(x[:,2])
y[:,3] = x[:,3] - np.mean(x[:,3])
y[:,4] = x[:,4] - np.mean(x[:,4])
y[:,5] = x[:,5] - np.mean(x[:,5])

#print(np.mean(x[:,0]),np.mean(x[:,0]),np.mean(x[:,0]))

#plt.clf()

pca = decomposition.PCA(n_components=nd)
pca.fit(y)
xt = pca.transform(y)

principalDf = pd.DataFrame(data = xt, columns = ['PC1', 'PC2','PC3','PC4','PC5','PC6'])
finalDf = pd.concat([principalDf, data[['Condition']]], axis = 1)

targets = ['LTP', 'Control']
colors = ['r', 'b']

fig, axs = plt.subplots(figsize=(1.8, 1.3))
fig.subplots_adjust(right=0.99, left = 0.3, bottom =0.35, top = 0.98)

for target, color in zip(targets,colors):
    indicesToKeep = finalDf['Condition'] == target
    axs.scatter(finalDf.loc[indicesToKeep, 'PC1']
               , finalDf.loc[indicesToKeep, 'PC2']
               , c = color
               , s = 2)
#axs.legend(targets)

print('eigenvectors:',pca.components_)
print('norm:', np.sqrt(pca.components_[0]**2+pca.components_[1]**2+pca.components_[2]**2+pca.components_[3]**2+pca.components_[4]**2+pca.components_[5]**2))
print('eigenvalues:', pca.explained_variance_)
print('%variance:',pca.explained_variance_ratio_)
#print(np.shape(xt))
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.savefig('./Figures/pca_all.png', dpi = 600)
#ax.scatter(xt[:, 0], xt[:, 1], xt[:, 2], cmap=plt.cm.nipy_spectral,edgecolor='k')
#ax.scatter(xt[:, 0], xt[:, 1], cmap ='plasma')
#print(np.sum(x[:, 0]),np.sum(x[:, 1]),np.sum(x[:, 2]))
#fig = plt.figure(figsize =(4,3))
#fig.subplots_adjust(right=0.95, left = 0.15, bottom =0.2, top = 0.98)

#targets = ['LTP', 'Control']
#colors = ['r', 'b']
#for target, color in zip(targets,colors):
 #   indicesToKeep = data['Condition'] == target
  #  plt.scatter(principal_breast_Df.loc[indicesToKeep, 'principal component 1']
   #             , principal_breast_Df.loc[indicesToKeep, 'principal component 2'],

    #for color, i, target_name in zip(colors, [0, 1, 2], target_names):
     #   plt.scatter(
      #      X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name
      #  )

#for color, i, target_name in zip(colors, [0, 1, 2], target_names):
 #   plt.scatter(
  #      X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name
   # )
plt.show()
