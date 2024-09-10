import sys

import numpy as np

import custom_types


def print_body(body):
    print(f"  Position X: {body['x_position']}\n"
          f"  Position Y: {body['y_position']}\n"
          f"  Mass:       {body['mass']}\n"
          f"  Velocity X: {body['x_velocity']}\n"
          f"  Velocity Y: {body['y_velocity']}\n"
          f"  Brightness: {body['brightness']}\n")


def print_body_arr(bodies):
    for i, body in enumerate(bodies):
        print(f"Body {i + 1}:")
        print_body(body)


def load_bodies_file(path):
    data = np.fromfile(path, dtype=np.float64)

    # Ensure the data is reshaped into chunks of 6 values (for each body)
    num_bodies = data.size // 6
    reshaped_data = data.reshape((num_bodies, 6))

    # Convert the reshaped data into the body_type structured array
    bodies = np.array([tuple(row) for row in reshaped_data], dtype=custom_types.particle_type)
    return bodies
