import bpy
import numpy as np
import pickle
import re


'''This script calculates the volumes of all convex hulls for all the synapses.
GCG
12.21.21
'''
#deselect all first
 
objs = bpy.context.scene.objects
my_pat = re.compile('.*_vert_hull$') #name of the convex hull of the SV cluster
my_chull = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_chull:
    i.select=  True

mcell = bpy.context.scene.mcell

bpy.ops.object.select_all(action='TOGGLE')

objs = bpy.context.scene.objects

for j in my_chull:
    myobject = j
    bpy.context.scene.objects.active = myobject
    myobject.select = True
    bpy.ops.object.editmode_toggle()
    #bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.object.editmode_toggle()

    #bpy.ops.object.select_all(action='TOGGLE')
    #j.select =  True
    #bpy.ops.object.editmode_toggle()
    #bpy.ops.mesh.select_all(action='TOGGLE')
    #bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
    #bpy.ops.mesh.select_all(action='TOGGLE')
    #bpy.ops.object.editmode_toggle()

my_pat = re.compile('.*_vert_hull$')
my_chull = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_chull:
    i.select=  True

mcell.meshalyzer.report_name = './'+'xr_ch_hull_inter_all_vol.txt'
mcell.meshalyzer.save_external = True
bpy.ops.mcell.gen_meshalyzer_report()
bpy.ops.object.select_all(action='TOGGLE')
