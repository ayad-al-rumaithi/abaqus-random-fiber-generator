"""
Input parameters for the model.
"""

config = {
    "BOX_DIMS": (60.0, 40.0, 50.0),  # Box dimensions (X, Y, Z)
    "FIBER_LENGTH": 25.0,  # Fiber length
    "NUM_FIBERS": 1000,  # Number of fibers to place
    "MAX_ATTEMPTS": 100000,  # Maximum random placement attempts
    "RANDOM_SEED": 42,  # Random seed for reproducibility
}