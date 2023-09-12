# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import sys
import importlib.util

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

MCELL_PATH = os.environ.get('MCELL_PATH', '')
if MCELL_PATH:
    lib_path = os.path.join(MCELL_PATH, 'lib')
    if os.path.exists(os.path.join(lib_path, 'mcell.so')) or \
        os.path.exists(os.path.join(lib_path, 'mcell.pyd')):
        sys.path.append(lib_path)
    else:
        print("Error: Python module mcell.so or mcell.pyd was not found in "
              "directory '" + lib_path + "' constructed from system variable "
              "MCELL_PATH.")
        sys.exit(1)
else:
    print("Error: system variable MCELL_PATH that is used to find the mcell "
          "library was not set.")
    sys.exit(1)

import Scene_geometry as geo
import re
import mcell as m
from Scene_parameters import *
from Scene_subsystem import *

# ---- create instantiation object and add components ----

geo_l = dir(geo)
hull_pat = '.*_hull$'
hull_l = [ (eval('geo.%s' % obj)) for obj in geo_l if re.match(hull_pat,obj) ]
print(hull_l)

for i in hull_l:
    if i.name == 'd01c16ax35_ssvr_vert_hull':
        selected_obj = i
        print('object_selected')
#rel_a = m.ReleaseSite(
 #   name = 'rel_a',
  #  complex = m.Complex('a'),
   # region = d01c16ax35_ssvr_vert_hull,
   # number_to_release = 157
   # )

#instantiation = m.Instantiation()
#instantiation.add_geometry_object(d01c16ax35_ssvr_vert_hull)
#instantiation.add_release_site(rel_a)

# load seed species information from bngl file
#instantiation.load_bngl_compartments_and_seed_species(os.path.join(MODEL_PATH, 'Scene_model.bngl'), None, shared.parameter_overrides)
