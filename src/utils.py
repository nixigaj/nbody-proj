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


def load_particles_file(path):
    data = np.fromfile(path, dtype=np.float64)

    # Ensure the data is reshaped into chunks of 6 values (for each particle)
    num_particles = data.size // 6
    reshaped_data = data.reshape((num_particles, 6))

    # Convert the reshaped data into the particle_type structured array
    particles = np.array([tuple(row) for row in reshaped_data], dtype=custom_types.particle_type)

    return particles


def write_particles_file(path, particles):
    # Convert structured array into a flat array of float64 values for saving to file
    flattened_data = np.hstack([particles[field].reshape(-1, 1) for field in particles.dtype.names]).flatten()

    flattened_data.astype(np.float64).tofile(path)
