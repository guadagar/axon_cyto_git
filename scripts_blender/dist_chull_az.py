import bpy
import numpy as np
import pickle
import cellblender

'''This file calculates the distance from each vesicle to the az (the minimun distance). I used a list with the active zones
in case the terminal is a MSB - it plots the values
02-02-22
'''

#This is a list with the azs for each bouton
the_filename = 'xr_az_lists'
azs = pickle.load(open(the_filename,'rb'))#
    #euclidean distance
def dist(x1,y1,z1,x2,y2,z2):
    d = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return d

for i in azs:
    ax_nr = i[0].split('ax')[1] #axon of the bouton
    ax_name = 'ax'+ax_nr #axon name
    #print(obj)
    nr_az = len(i)
    #the name of the cloud of vesicles
    name = i[0] + str('_ssvr_vert_hull_alone')
    bpy.context.scene.objects.active = bpy.data.objects[name]
    obj_n = bpy.context.scene.objects.active    #select the vesicles
    n = len(obj_n.data.vertices)
    verts = np.zeros((n,3))
    obj_name = obj_n.name
    for k in range(0,n):
        verts[k,0] = obj_n.data.vertices[k].co[0]
        verts[k,1] = obj_n.data.vertices[k].co[1]
        verts[k,2] = obj_n.data.vertices[k].co[2]

    dmin = np.zeros((n,nr_az)) #now is a matrix, I consider all the azs in the bouton

    bpy.context.scene.objects.active = bpy.data.objects[ax_name]
    obj = bpy.context.scene.objects.active
    regions = []
    regions.append(obj.mcell.regions.region_list.keys())
    #here are the azs and the bouton volume, I only get the distance to one of them.
    flat_reg = [item for sublist in regions for item in sublist]
    nr_az_indx = 0
    #print(i,obj_n,ax_name,flat_reg)

    for j in i: #loopeo in the azs
        if j in flat_reg:
            bpy.context.scene.objects.active = bpy.data.objects[ax_name]
            obj = bpy.context.scene.objects.active
            reg = obj.mcell.regions.region_list[j]
          #  print(reg.select_region_faces)
            reg.select_region_faces(bpy.context)
            #this leave us in edit mode
            bpy.ops.object.mode_set(mode='OBJECT')
            selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]

            n_az = len(selectedVerts)
            verts_az = np.zeros((n_az,3))
            print(n_az)
            for k,v in enumerate(selectedVerts):
                verts_az[k,0] = v.co[0]
                verts_az[k,1] = v.co[1]
                verts_az[k,2] = v.co[2]

             #going back to object mode
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.mode_set(mode='OBJECT')
             #select the vesicles associated with this az
            dm = np.zeros((n,n_az))
            for k in range(0,n):
                for s in range(0,n_az):
                    dm[k,s] = dist(verts[k,0],verts[k,1],verts[k,2], verts_az[s,0],verts_az[s,1], verts_az[s,2])

            #print(np.shape(dm),nr_az,dm)
            for k in range(0,n):
                dmin[k,nr_az_indx] = np.min(dm[k,:])
            nr_az_indx = nr_az_indx + 1
            #bpy.ops.object.editmode_toggle()
            #bpy.context.scene.objects.active = bpy.data.objects[obj.name]
        else:
            print('this region not found',j)

    the_filename = obj_name+'_az_dis_chull'
    with open(the_filename, 'wb') as f:#
        pickle.dump(dmin, f)
