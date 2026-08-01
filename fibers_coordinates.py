import numpy as np

def fibers_coordinates(center, length, rotation_matrix):
    """
    Compute the two end points of a line fiber in 3D space given
    its center, length, and rotation.

    Parameters:
        center : list or array-like [x, y, z]
            The fiber's center coordinates.
        length : float
            Fiber length along local Z-axis.
        rotation_matrix : np.ndarray, shape (3,3)
            Rotation applied to the fiber (local → global coordinates).

    Returns:
        np.ndarray, shape (2,3)
            Array of 3D coordinates for the fiber end points.
    """
    dz = length / 2.0

    # Define fiber in local reference frame (aligned with Z-axis)
    local_coords = np.array([
        [0, 0, -dz],
        [0, 0,  dz]
    ])

    # Apply rotation
    rotated = (rotation_matrix @ local_coords.T).T

    # Translate to global coordinates
    translated = rotated + np.array(center)

    return translated