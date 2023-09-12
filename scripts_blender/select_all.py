import bpy
import re

objs = bpy.context.scene.objects
my_pat = re.compile('.*_ssvr_ra$')
#my_pat = re.compile('.*_ssvr_vert_hull$')
my_obj = [obj for obj in objs if my_pat.match(obj.name)!=None]
for i in my_obj:
    i.select=  True