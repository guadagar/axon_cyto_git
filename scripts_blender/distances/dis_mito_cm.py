import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay
import re

'''This script calculates the distance from the center of the cloud to the mito. The output is a python file per bouton
with the distances.
GCG
12.05.23
'''

objs = bpy.context.scene.objects
my_pat = re.compile('.*_ssvr$')
#my_pat = re.compile('.*_ssvr_vert_hull$')
my_obj = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_obj:
    i.select=  True

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        n = len(obj.data.vertices)
        verts = np.zeros((n,3))
        obj_name = obj.name

        for i in range(0,n):
            verts[i,0] = obj.data.vertices[i].co[0]
            verts[i,1] = obj.data.vertices[i].co[1]
            verts[i,2] = obj.data.vertices[i].co[2]

        #euclidean distance
        def dist(x1,y1,z1,x2,y2,z2):
            d = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            return d

        try:
            mito_name = obj.name.split('_')[0] + str('_mito1')
            bpy.context.scene.objects.active = bpy.data.objects[mito_name]
            obj_n = bpy.context.scene.objects.active    #select the vesicles
            nves_m = len(obj_n.data.vertices)
            verts_m = np.zeros((nves_m,3))

            for k in range(0,nves_m):
                verts_m[k,0] = obj_n.data.vertices[k].co[0]
                verts_m[k,1] = obj_n.data.vertices[k].co[1]
                verts_m[k,2] = obj_n.data.vertices[k].co[2]

            dm = np.zeros((n,nves_m))
            #dis ves to mito
            for k in range(0,n):
                for s in range(0,nves_m):
                    dm[k,s] = dist(verts[k,0],verts[k,1],verts[k,2], verts_m[s,0],verts_m[s,1], verts_m[s,2])

            dmin = np.zeros((n))

            for k in range(0,n):
                dmin[k] = np.min(dm[k,:])

            cm_verts = np.zeros((3,1))
            cm_verts[0] = np.mean(verts[:,0])
            cm_verts[1] = np.mean(verts[:,1])
            cm_verts[2] = np.mean(verts[:,2])

        #dis mito to cm
            dis_m = np.zeros((nves_m))
            for s in range(0,nves_m):
                dis_m[s] = dist(cm_verts[0],cm_verts[1],cm_verts[2], verts_m[s,0],verts_m[s,1], verts_m[s,2])

            min_d_m = np.min(dis_m)

            out = np.zeros((2))

            out[0] = min_d_m
            out[1] = np.median(dmin)

            the_filename = obj_name
            with open(the_filename, 'wb') as f:#
                pickle.dump(out, f)
        except:
            print('no_mito')
