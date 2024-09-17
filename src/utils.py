import numpy as np
import custom_types


def print_particle(particle):
    print(f"  Position X: {particle['x_position']}\n"
          f"  Position Y: {particle['y_position']}\n"
          f"  Mass:       {particle['mass']}\n"
          f"  Velocity X: {particle['x_velocity']}\n"
          f"  Velocity Y: {particle['y_velocity']}\n"
          f"  Brightness: {particle['brightness']}\n")


def print_body_arr(particles):
    for i, particle in enumerate(particles):
        print(f"Particle {i + 1}:")
        print_particle(particle)


# @param path The file path to the GAL-file containing the state of a collection of particles
def load_particles_file(path):
    data = np.fromfile(path, dtype=np.float64)

    # Ensure the data is reshaped into chunks of 6 values (for each particle)
    num_particles = data.size // 6
    reshaped_data = data.reshape((num_particles, 6))

    # Convert the reshaped data into the particle_type structured array
    particles = np.array([tuple(row) for row in reshaped_data], dtype=custom_types.particle_type)

    return particles


# @param path The file path to where to write the resulting particles as a GAL-file
# @param particles The frame of particles to write to the file
def write_particles_file(path, particles):
    # Convert structured array into a flat array of float64 values for saving to file
    flattened_data = np.hstack([particles[field].reshape(-1, 1) for field in particles.dtype.names]).flatten()

    flattened_data.astype(np.float64).tofile(path)


# TODO This function does not actually currently work properly
def load_particles_arr_file(path, no_iterations):
    data = np.fromfile(path, dtype=np.float64)

    # Calculate the number of particles based on the total size and number of iterations
    num_particles = data.size // (6 * no_iterations)

    # Reshape the data into a 3D array: (no_iterations, num_particles, 6)
    reshaped_data = data.reshape((no_iterations, num_particles, 6))

    # Convert the reshaped data into an array of particle_type structured arrays
    particles_arr = np.array([
        np.array([tuple(particle) for particle in frame], dtype=custom_types.particle_type)
        for frame in reshaped_data
    ])

    return particles_arr


# TODO This function does not actually currently work properly
def write_particles_arr_file(path, particles_arr):
    # Ensure particles_arr is a 2D array of particle_type structured arrays
    assert particles_arr.ndim == 2 and particles_arr.dtype == custom_types.particle_type

    # Flatten the structured array into a 3D array of float64 values
    flattened_data = np.array([
        np.hstack([frame[field].reshape(-1, 1) for field in custom_types.particle_type.names]).flatten()
        for frame in particles_arr
    ])

    # Further flatten to 1D for file writing
    flattened_data = flattened_data.flatten()

    flattened_data.astype(np.float64).tofile(path)
