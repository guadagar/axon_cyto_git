import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay, Voronoi,ConvexHull,Delaunay,voronoi_plot_2d


'''This script generates the convex hull for a set of vertices. The intersection with mitos in the bouton is considered. The meshes are also triangulated to calculate the volumes.
GCG
06.02.22
'''

if bpy.context.selected_objects != []: # ssvr all
    for obj in bpy.context.selected_objects:

        n = len(obj.data.vertices)
        points = np.zeros((n,3))
        obj_name = obj.name

        for i in range(0,n):
            points[i,0] = obj.data.vertices[i].co[0]
            points[i,1] = obj.data.vertices[i].co[1]
            points[i,2] = obj.data.vertices[i].co[2]
        verts = []
        #n = len(points)
        for i in range(n):
            verts.append((points[i,0],points[i,1],points[i,2]))
        chull_name = obj_name + str('_vert_hull_alone')
        mymesh = bpy.data.meshes.new(chull_name)
        myobject = bpy.data.objects.new(chull_name,mymesh)
        bpy.context.scene.objects.link(myobject)
        mymesh.from_pydata(verts,[],[])
        mymesh.update()

        #convex-hull of the vertices
        bpy.context.scene.objects.active = myobject
        myobject.select = True
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.convex_hull()
        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.object.editmode_toggle()

          #     # triangulate the meshe to calculate vol
        bpy.context.scene.objects.active = myobject
        myobject.select = True
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.object.editmode_toggle()
        #

#plt.show()
