import bpy
import numpy as np
import pickle
#from scipy.spatial import Delaunay, Voronoi,ConvexHull,Delaunay,voronoi_plot_2d
#import re

'''This script calculates the volumes of all voronoi cells for all the synapses.
GCG
10.06.21
'''
mcell = bpy.context.scene.mcell
boutons_name = []
if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        n = len(obj.data.vertices)
        points = np.zeros((n,3))
        obj_name = obj.name 
        boutons_name.append(obj_name)
        
bpy.ops.object.select_all(action='TOGGLE')

for j in boutons_name:   
 #   #j.split('_')[0]    
    for k in bpy.data.objects:
        #try:
        a = k.name.split('_')
        print(a,len(a))
        if len(a)==4:
            print(a[0], a[1])
            if a[0] == j.split('_')[0] and a[1] == 'ssvrvor':
                print(k.name)
                bpy.data.objects[k.name].select = True
    
    
    bpy.ops.mcell.gen_meshalyzer_report()
    bpy.ops.object.select_all(action='TOGGLE')
    text_ref = bpy.data.texts['mesh_analysis.txt']
    destination = './'+str(j)+'_vor_vol.txt'
    with open(destination, 'w') as outfile:
        outfile.write(text_ref.as_string())
    foo = bpy.data.texts['mesh_analysis.txt']
    bpy.data.texts.remove(foo)
    