# This file contains hooks to override default MCell4 model
# code behavior for models generated from CellBlender
import sys
import os
import shared
import mcell as m

name_cloud = ''
nr_ves_in = ''

def custom_argparse_and_parameters():
     # When uncommented, this function is called to parse
    # custom commandline arguments.
    # It is executed before any of the automatically generated
    # parameter values are set so one can override the parameter
    # values here as well.
    # To override parameter values, add or overwrite an item in dictionary
    # shared.parameter_overrides, e.g. shared.parameter_overrides['SEED'] = 10

    if len(sys.argv) != 5 or sys.argv[1] != '-seed':
        sys.exit("Expected following arguments: -seed N name_cloud nr_ves")

    # overwrite value of seed defined in module parameters
#    shared.parameter_overrides['SEED'] = int(sys.argv[2])

    # and remember selected variant,
    # cannot use parameter_overrides because its values must be always floats
    global name_cloud,nr_ves_in
    name_cloud = sys.argv[3]
    nr_ves_in = sys.argv[4]


#def custom_config(model):
    # When uncommented, this function is called to set custom
    # model configuration.
    # It is executed after basic parameter setup is done and
    # before any components are added to the model.

def custom_init_and_run(model):
    # When uncommented, this function is called after all the model
    # components defined in CellBlender were added to the model.
    # It allows to add additional model components before initialization
    # is done and then to customize how simulation is ran.
    # The module parameters must be imported locally otherwise
    # changes to shared.parameter_overrides done elsewhere won't be applied.
    import Scene_parameters as parameters
    import Scene_geometry as geo
    import re
   # import mcell as m

    #geo_l = dir(geo)

    hull_pat = '.*_hull$'
    #hull_l = [(eval('geo.%s' % obj)) for obj in geo_l if re.match(hull_pat, obj)]
    #print(eval('geo.' + name_cloud))
    try:
         selected_obj = eval('geo.' + name_cloud + '_vert_hull')
    except:
        print('Cloud not found')

    species_a = m.Species(
        name = 'a',
        diffusion_constant_3d = 0
    )

    rel_a = m.ReleaseSite(
        name = 'rel_a',
        complex = species_a,
        region = selected_obj,
        number_to_release = float(nr_ves_in)
        )

    viz_output = m.VizOutput(
        mode=m.VizMode.ASCII,
        output_files_prefix='./viz_data/seed_00001/'+name_cloud,
    )

    model.add_species(species_a)
    model.add_geometry_object(selected_obj)
    model.add_release_site(rel_a)
    model.add_viz_output(viz_output)

    #viz_output = m.VizOutput(
     #   mode=m.VizMode.ASCII,
      #  output_files_prefix='./viz_data/seed_' + str(1).zfill(5) + '/'+ name_cloud,
       # every_n_timesteps=1
   # )
   # observables = m.Observables()
    #observables.add_viz_output(viz_output)

    #model.add_observables(observables)

    model.initialize()

    model.run_iterations(parameters.ITERATIONS)
    model.end_simulation()
