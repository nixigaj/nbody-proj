import numpy as np

particle_type = np.dtype([
    ('x_position', np.float64),
    ('y_position', np.float64),
    ('mass', np.float64),
    ('x_velocity', np.float64),
    ('y_velocity', np.float64),
    ('brightness', np.float64)
])

vector2d_type = np.dtype([('x', np.float64), ('y', np.float64)])
