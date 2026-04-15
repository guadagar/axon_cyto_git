import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay

'''
This script calculates the number of SVs forming the convex hull for each bouton and saves the name of the bouton and the number of SVs in that form the convex hull. 
GCG
11.30.22
'''

my_pat = re.compile('.*_ssvr_vert_hull_alone$')
my_obj = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_obj:
    i.select=  True

f = open('./nr_ves_out','w')

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        #print(obj.name)
        n = len(obj.data.vertices)
        verts = np.zeros((n,3))
        obj_name = obj.name

        f.write(xname)
        f.write('\t')
        f.write(str(n))
        #f.write('\t')
        #f.write(str(n_in))
        #f.write('\n')
f.close()
