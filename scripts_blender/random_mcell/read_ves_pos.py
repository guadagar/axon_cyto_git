
import bpy
import os, sys, tempfile
import subprocess as sp
import numpy as np
import re


#dir = os.path.dirname(os.path.abspath(__file__))

#select all the chull alone (no intersection w mito)
objs = bpy.context.scene.objects
my_pat = re.compile('.*_ssvr_vert_hull_alone$')
my_obj = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_obj:
    i.select=  True

if bpy.context.selected_objects != []: # ssvr all
    for obj in bpy.context.selected_objects:
        n = len(obj.data.vertices)
      #  points = np.zeros((n,3))
        obj_name = obj.name
        vertices = []
        red_name = obj_name.split('_')[0]
        for i in range(0,n):
            vertices.append((obj.data.vertices[i].co[0],obj.data.vertices[i].co[1],obj.data.vertices[i].co[2]))

        ves_tmp = '../fh_seed_00001/'+red_name+'_ssvr.ascii.1.dat'
        #print(ves_tmp)
        try:
            f = open(ves_tmp, "r")
            print('found it')
        except:
            'file not found'
            continue

        for line in f:
            line_split = line.split()
            vertices.append((float(line_split[2]),float(line_split[3]),float(line_split[4])))

        edges = []    
        mymesh = bpy.data.meshes.new(red_name+'_ssvr_ra')
        myobject = bpy.data.objects.new(red_name+'_ssvr_ra',mymesh)
        bpy.context.scene.objects.link(myobject)
        mymesh.from_pydata(vertices,edges,[])
        mymesh.update()
