import bpy
import numpy as np
import pickle
import re

'''
This script triangulates the objects in the my_chull list. Objects have to be triangulated to calculate the volumes.
GCG
12.21.21
'''
#deselect all first

objs = bpy.context.scene.objects
name = 'd04c22ax27'
my_pat = re.compile(name+'_ssvrvor_ich')
my_chull = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_chull:
    i.select=  True

mcell = bpy.context.scene.mcell

bpy.ops.object.select_all(action='TOGGLE')

objs = bpy.context.scene.objects

#print(my_chull)

for j in my_chull:
    myobject = j
    bpy.context.scene.objects.active = myobject
    myobject.select = True
    bpy.ops.object.editmode_toggle()
    #bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.object.editmode_toggle()

for i in my_chull:
    i.select=  True

bpy.ops.mcell.gen_meshalyzer_report()
bpy.ops.object.select_all(action='TOGGLE')
text_ref = bpy.data.texts['mesh_analysis.txt']
destination = './'+name+'_ssvr_vor_vol.txt'
with open(destination, 'w') as outfile:
    outfile.write(text_ref.as_string())
foo = bpy.data.texts['mesh_analysis.txt']
bpy.data.texts.remove(foo)
