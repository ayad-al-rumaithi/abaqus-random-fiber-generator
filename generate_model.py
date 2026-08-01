from abaqus import *
from abaqusConstants import *

def generate_model(config, fiber_data):
    """
    Build an Abaqus model with a box and line fibers inside.

    Parameters:
        config : dict
            Configuration dictionary containing box dimensions
            and model specifications.

        fiber_data : list of tuples (center, angles, points)
            Information about fibers: center coordinates,
            Euler angles, and fiber end point coordinates.
    """
    # Extract parameters from the config dictionary
    BOX_W, BOX_H, BOX_D = config["BOX_DIMS"]

    model_name = 'GeneratedModel'

    # Delete existing model if it exists
    if model_name in mdb.models:
        del mdb.models[model_name]

    model = mdb.Model(name=model_name)
    assembly = model.rootAssembly

    # Create the main box part
    sketch_box = model.ConstrainedSketch(
        name='__box__',
        sheetSize=200.0
    )

    sketch_box.rectangle(
        (0.0, 0.0),
        (BOX_W, BOX_H)
    )

    box_part = model.Part(
        name='Box',
        dimensionality=THREE_D,
        type=DEFORMABLE_BODY
    )

    box_part.BaseSolidExtrude(
        sketch=sketch_box,
        depth=BOX_D
    )

    # Add box instance to the assembly
    assembly.Instance(
        name='Box-1',
        part=box_part,
        dependent=ON
    )

    # Create a single part containing all fiber lines
    fiber_part = model.Part(
        name='Fibers',
        dimensionality=THREE_D,
        type=DEFORMABLE_BODY
    )

    for _, _, points in fiber_data:

        fiber_part.WirePolyLine(
            points=(
                tuple(points[0]),
                tuple(points[1])
            ),
            mergeType=IMPRINT,
            meshable=ON
        )

    # Add fiber instance to the assembly
    assembly.Instance(
        name='Fibers-1',
        part=fiber_part,
        dependent=ON
    )