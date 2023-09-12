import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay
import re

'''this script calculates the distance from the vesicles to the convex hull (to the vesicles in the outer layer). GCG
08.31.23
'''

objs = bpy.context.scene.objects
my_pat = re.compile('.*_ssvr$')
#my_pat = re.compile('.*_ssvr_vert_hull$')
my_obj = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_obj:
    i.select=  True

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        #print(obj.name)
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

        chull_name = obj.name.split('_')[0] + str('_ssvr_vert_hull_alone')
        bpy.context.scene.objects.active = bpy.data.objects[chull_name]
        obj_n = bpy.context.scene.objects.active    #select the vesicles
        nves_ol = len(obj_n.data.vertices)
        verts_ol = np.zeros((nves_ol,3))

        for k in range(0,nves_ol):
            verts_ol[k,0] = obj_n.data.vertices[k].co[0]
            verts_ol[k,1] = obj_n.data.vertices[k].co[1]
            verts_ol[k,2] = obj_n.data.vertices[k].co[2]

        dm = np.zeros((n,nves_ol))
        for k in range(0,n):
            for s in range(0,nves_ol):
                dm[k,s] = dist(verts[k,0],verts[k,1],verts[k,2], verts_ol[s,0],verts_ol[s,1], verts_ol[s,2])

        dmin = np.zeros((n))
        for k in range(0,n):
            dmin[k] = np.min(dm[k,:])

        the_filename = obj_name
        with open(the_filename, 'wb') as f:#
            pickle.dump(dmin, f)
