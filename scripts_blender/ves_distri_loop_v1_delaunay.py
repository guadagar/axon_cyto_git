import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay

'''this script calculates the delaunay mehs for a group of vertices. For the veritices connected to each, I compute
the distance, and calculate the average
GCG
11.30.22
'''

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

        tri = Delaunay(verts)
        indptr, indices = tri.vertex_neighbor_vertices
        av_de_ne = np.zeros((n)) #average distance to the Delaunay neighbors

        nei = []
        for i in range(0,n):
            idx = indices[indptr[i]:indptr[i+1]] #indices of the neighbors of i
            d_t = []
            nei.append(len(idx))
            if len(idx)==0:
                print(i,'no neighbor')
            #print(nei)
            for j in idx:
                d_t.append(dist(verts[i,0],verts[i,1],verts[i,2],verts[j,0],verts[j,1],verts[j,2]))

            av_de_ne[i] = np.mean(d_t)
        #print(av_de_ne)
        av_f = av_de_ne[np.logical_not(np.isnan(av_de_ne))]
        #print(np.mean(av_f),np.std(av_f), np.median(av_f))
        #generate delaunay mesh
        #edges = []

        #for i,p in enumerate(verts):
         #   ve = p
            #edges = []
          #  idx = indices[indptr[i]:indptr[i+1]] #indices of the neighbors of i\\
           # print('neig',indices[indptr[i]:indptr[i+1]])
           # for j in idx:
             #   verts[j,0],verts[j,1],verts[j,2] neighbors
            #    edges.append([i,j])
#
 #       mymesh = bpy.data.meshes.new(bpy.context.object.data.name+"_del")
  #      myobject = bpy.data.objects.new(bpy.context.object.data.name+"_del",mymesh)

#        bpy.context.scene.objects.link(myobject)

#        mymesh.from_pydata(verts,edges,[])
 #       mymesh.update()


        #print((nei))
        dma = np.zeros((n,n))

        for i in range(0,n):
            for j in range(0,n):
                dma[i,j] = dist(verts[i,0],verts[i,1],verts[i,2],verts[j,0],verts[j,1],verts[j,2])

        min_dist = np.zeros((n))
        #max_dist = np.zeros((n))


       # for i in range(0,n):
        #    min_dist[i] = np.min((dma[i,np.nonzero(dma[i,:])]))
        #    max_dist[i] = np.max((dma[i,:]))


        #the_filename = 'mind_'+obj_name

        #    with open(the_filename, 'wb') as f:#
        #    pickle.dump(max_dist, f)

        #the_filename = obj_name+'_dis'
        #with open(the_filename, 'wb') as f:#
         #   pickle.dump(min_dist, f)
        #print(np.shape(dma[np.nonzero(np.triu(dma))]))
        #print(av_de_ne,np.mean(av_de_ne),np.std(av_de_ne))
        the_filename = obj_name
        with open(the_filename, 'wb') as f:#
            pickle.dump(av_f, f)
