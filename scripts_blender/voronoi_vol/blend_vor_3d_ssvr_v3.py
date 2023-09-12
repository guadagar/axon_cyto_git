import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay, Voronoi,ConvexHull,Delaunay,voronoi_plot_2d


'''This script generates the voronoi cells of a set of points. The closed voronoi cells are considered, the intersection with the convex-hull (intersected with the mito)
of the vertices is performed. The meshes are also triangulated to calculate the volumes.
GCG
09.1.23
'''

objs = []
for i in bpy.context.selected_objects:
    objs.append(i)

for obj in objs:
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
        #I use the chull intersected with the mito name_vor_winter
    chull_name = obj_name + str('_vert_hull')
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

    bpy.context.scene.objects.active = bpy.data.objects[chull_name]
    myobject = bpy.context.scene.objects.active
    myobject.select = True


    try:
        mito_name = obj_name.split('_')[0] + str('mito1')
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[mito_name]
        bpy.context.object.modifiers["Boolean"].solver = 'CARVE'
        bpy.ops.object.modifier_apply(apply_as = 'DATA', modifier = 'Boolean')
        bpy.ops.object.editmode_toggle()
            #bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
        bpy.ops.mesh.select_all(action='TOGGLE')
        bpy.ops.object.editmode_toggle()

    except:
        print('no mito')

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.object.editmode_toggle()


    def dist(x1,y1,z1,x2,y2,z2):
        d = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
        return d

        #Generate the delaunay mesh
    tri = Delaunay(verts)
    indptr, indices = tri.vertex_neighbor_vertices

    edges = set()
    def sorted_tuple(a,b):
        return (a,b) if a < b else (b,a)

    #calculate voronoi cells of the vertices
    v = Voronoi(verts)
    vol_vor = np.zeros((len(v.point_region)))
    ve = v.vertices
    n_vor = 0
    f = open(obj.name +'.txt','w')

    #Association of delanay vertices to voronoi cells
    #only with close cells
    for i, reg_num in enumerate(v.point_region):
            #ax.plot(points[4,0],points[4,1],color = c[i] ,marker='s')
        indices = v.regions[reg_num] #vertices of the region reg_num
        ve = v.vertices[indices]
        ve_vor = []
        for s in ve:
            ve_vor.append((s[0],s[1],s[2]))
        #print((i[0],i[1],0))
        if -1 in indices: # some regions can be opened
            gr_zero = np.where(np.array(indices) >= 0)
        #ind = np.array(indices)
                #print('open')
            continue
        else:
            n_vor =+ 1
            hull = ConvexHull(v.vertices[indices]) #for the region, reg_num, compute convex hull of the vornoi cell
            vol_vor[i] = ConvexHull(ve).volume
                #print(vol_vor[i],i, len(ve))
            f.write(str(i))
            f.write('\t')
            f.write(str(vol_vor[i]))
            f.write('\n')

            mymesh = bpy.data.meshes.new(obj_name +str('vor_ich_')+str(i))
            myobject = bpy.data.objects.new(obj_name +str('vor_ich_')+str(i),mymesh)
            mymesh.from_pydata(ve_vor,[],[])
            mymesh.update()
            bpy.context.scene.objects.link(myobject)

                #convex-hull vertices
            bpy.context.scene.objects.active = myobject
            myobject.select = True
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.convex_hull()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.editmode_toggle()

                #boolean vornoi cell with convex-hull vertices
            bpy.context.scene.objects.active = myobject
            myobject.select = True
            bpy.ops.object.modifier_add(type='BOOLEAN')
            bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[obj_name +str('_vert_hull')]
            bpy.context.object.modifiers["Boolean"].solver = 'CARVE'
            bpy.ops.object.modifier_apply(apply_as = 'DATA', modifier = 'Boolean')

                # triangulate the meshe to calculate vol
            bpy.context.scene.objects.active = myobject
            myobject.select = True
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.editmode_toggle()


    f.close()
