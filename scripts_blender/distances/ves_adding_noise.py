import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay

'''
GCG
02.04.22
'''

np.random.seed(93613380)

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        n = len(obj.data.vertices)
        verts = np.zeros((n,3))
        obj_name = obj.name
       
        for i in range(0,n):
            verts[i,0] = obj.data.vertices[i].co[0]
            verts[i,1] = obj.data.vertices[i].co[1]
            verts[i,2] = obj.data.vertices[i].co[2] + 0.5*0.062*(2*np.random.random()-1)

        mymesh = bpy.data.meshes.new(bpy.context.object.data.name+"_noise")
        myobject = bpy.data.objects.new(bpy.context.object.data.name+"_noise",mymesh)

        bpy.context.scene.objects.link(myobject)

        mymesh.from_pydata(verts,[],[])
        mymesh.update()

