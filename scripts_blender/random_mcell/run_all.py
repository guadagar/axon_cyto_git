import os,sys
import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from itertools import zip

'''This script runs mcell
GCG
08.27.23
'''

data = pd.read_csv('../../../../latest_results/data/all_data_together/all_data.csv')


#xr = data.loc[(data['Condition'] == 'LTP')  & (data['Animal'] == 'JB023')]
#fp = data.loc[(data['Condition'] == 'Control')  & (data['Animal'] == 'JB023')]
#fh = data.loc[(data['Condition'] == 'Control')  & (data['Animal'] == 'JB024')]
fw = data.loc[(data['Condition'] == 'LTP')  & (data['Animal'] == 'JB024')]

python_path ='/Applications/Blender-2.93-CellBlender/blender.app/Contents/Resources/2.93/python/bin/python3.9'
run_file = 'Scene_model.py'
tdir = './'

#I select the name of the SV cluster and the SV number inside the cluster
for name_cloud, nr_ves in zip(fw['name'], fw['nr_ves_in']):
    #I pass these parameters to mcell, and run it
    name = str(name_cloud) + '_ssvr'
    seed_nr = 1
    print(name,type(str(nr_ves)))
    Proc = sp.call([python_path, run_file, '-seed', '1', name, str(nr_ves)],cwd = tdir)
    if Proc != 0:
        print('MCell did not run')
    else:
        print('MCell sim done')