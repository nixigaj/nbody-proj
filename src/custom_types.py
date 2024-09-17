import numpy as np

# This type stores the information about one particle
particle_type = np.dtype([
    ('x_position', np.float64),
    ('y_position', np.float64),
    ('mass', np.float64),
    ('x_velocity', np.float64),
    ('y_velocity', np.float64),
    ('brightness', np.float64)
])

# A simple 2D vector
vector2d_type = np.dtype([('x', np.float64), ('y', np.float64)])
