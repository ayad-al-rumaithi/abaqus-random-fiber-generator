import random
import math
import numpy as np

from rotation_matrix_zxz import rotation_matrix_zxz
from fibers_coordinates import fibers_coordinates

def generate_fibers(config):
    """
    Generate randomly oriented line fibers inside a 3D box.

    Parameters:
        config : dict
            Configuration dictionary containing box/fiber dimensions,
            count, maximum attempts, and random seed.

    Returns:
        list of tuples: (center, (alpha, beta, gamma), fiber_points)
            Center coordinates, ZXZ Euler angles (degrees),
            and fiber end point coordinates.
    """
    # Extract parameters from the config dictionary
    BOX_W, BOX_H, BOX_D = config["BOX_DIMS"]
    fiber_length = config["FIBER_LENGTH"]
    num_fibers = config["NUM_FIBERS"]
    max_attempts = config["MAX_ATTEMPTS"]
    random_seed = config["RANDOM_SEED"]

    random.seed(random_seed)
    np.random.seed(random_seed)

    fiber_data = []
    attempts = 0

    while len(fiber_data) < num_fibers and attempts < max_attempts:
        attempts += 1

        # Random ZXZ Euler angles
        # Alpha is fixed because the fiber is a line aligned with local Z-axis
        alpha = 0.0
        gamma = random.uniform(0, 360)
        beta = math.degrees(math.acos(2 * random.random() - 1))

        R = rotation_matrix_zxz(alpha, beta, gamma)

        # Random fiber center inside the box
        center = (
            random.uniform(0, BOX_W),
            random.uniform(0, BOX_H),
            random.uniform(0, BOX_D)
        )

        # Compute fiber end points
        fiber_points = fibers_coordinates(
            center,
            fiber_length,
            R
        )

        # Check if fiber is inside the box
        box_limit = np.array([BOX_W, BOX_H, BOX_D])

        if np.any(fiber_points.min(axis=0) < 0) or np.any(fiber_points.max(axis=0) > box_limit):
            continue

        fiber_data.append(
            (center, (alpha, beta, gamma), fiber_points)
        )

    print(f"Placed {len(fiber_data)} fibers after {attempts} attempts.")
    return fiber_data