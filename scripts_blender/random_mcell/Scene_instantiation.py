# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from Scene_parameters import *
from Scene_subsystem import *
from Scene_geometry import *

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- create instantiation object and add components ----
#rel_a = m.ReleaseSite(
 #   name = 'rel_a',
 #   complex = m.Complex('a'),
 #   region = d01c16ax35_ssvr_vert_hull,
 #   number_to_release = 157
 #   )

instantiation = m.Instantiation()
#instantiation.add_geometry_object(d01c16ax35_ssvr_vert_hull)
#instantiation.add_release_site(rel_a)

# load seed species information from bngl file
#instantiation.load_bngl_compartments_and_seed_species(os.path.join(MODEL_PATH, 'Scene_model.bngl'), None, shared.parameter_overrides)
