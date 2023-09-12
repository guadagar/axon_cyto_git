import bpy
import numpy as np
import pickle
import cellblender as cb

'''This file calculates the distance from each vesicle to the az (the minimun distance). If it's a MSB
I caclulate the distance only to one AZ (the one that gives the name to the cloud).
05-27-21
'''
# First select all the axons

ax_name = 'ax79'
bpy.context.scene.objects.active = bpy.data.objects[ax_name]
obj = bpy.context.scene.objects.active
az = []
az.append(obj.mcell.regions.region_list.keys())

reg = obj.mcell.regions.region_list['d04c32ax79']
reg.select_region_faces(bpy.context)
#this leave us in edit mode
bpy.ops.object.mode_set(mode='OBJECT')
selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
#print('aca',i, len(selectedVerts))
n_az = len(selectedVerts)
verts_az = np.zeros((n_az,3))
for j,v in enumerate(selectedVerts):
    verts_az[j,0] = v.co[0]
    verts_az[j,1] = v.co[1]
    verts_az[j,2] = v.co[2]
#going back to object mode
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.object.mode_set(mode='OBJECT')

#select the vesicles associated with this az

name = 'd04c32ax79' + str('_ssvr')

bpy.context.scene.objects.active = bpy.data.objects[name]
print('found it',name)
obj_n = bpy.context.scene.objects.active    #selecciono las vesicles
n = len(obj_n.data.vertices)
verts = np.zeros((n,3))
obj_name = obj_n.name

for i in range(0,n):
    verts[i,0] = obj_n.data.vertices[i].co[0]
    verts[i,1] = obj_n.data.vertices[i].co[1]
    verts[i,2] = obj_n.data.vertices[i].co[2]

#euclidean distance
def dist(x1,y1,z1,x2,y2,z2):
    d = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return d

dm = np.zeros((n,n_az))
dmin = np.zeros((n))
nb_min = np.zeros((n))

for i in range(0,n):
    for j in range(0,n_az):
        dm[i,j] = dist(verts[i,0],verts[i,1],verts[i,2], verts_az[j,0],verts_az[j,1], verts_az[j,2])

for i in range(0,n):
    dmin[i] = np.min(dm[i,:])
    nb_min[i] = np.argmin(dm[i,:])

#generate the distances
edges = []
new_verts = np.zeros((2*n,3))
for i,p in enumerate(verts):
        #i = 0,1,2,...
    j = nb_min[i]
    print(int(j))
    new_verts[i,0] = verts[i,0]
    new_verts[i,1] = verts[i,1]
    new_verts[i,2] = verts[i,2]
    k = i + n
    #print(k)
    new_verts[k,0] = verts_az[int(j),0]
    new_verts[k,1] = verts_az[int(j),1]
    new_verts[k,2] = verts_az[int(j),2]
    edges.append([i,i+n])

mymesh = bpy.data.meshes.new(bpy.context.object.data.name+"_dis_az")
myobject = bpy.data.objects.new(bpy.context.object.data.name+"_dis_az",mymesh)
bpy.context.scene.objects.link(myobject)

mymesh.from_pydata(new_verts,edges,[])
mymesh.update()

##print(np.mean(dmin))
bpy.context.scene.objects.active = bpy.data.objects[obj.name]
#the_filename = obj_name+'_az_dis'
#with open(the_filename, 'wb') as f:#
 #   pickle.dump(dmin, f)
print(np.median(dmin))