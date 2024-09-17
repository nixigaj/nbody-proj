from constants import *
import numpy as np
import custom_types
from numba import njit


# This function is the main entry point for the algorithm implemented from the provided equations.
# @param init_particles Initial position and velocity of a frame of particles
# @param calc_force_func Function that calculates the force of each of the individual particles at a given frame
# @param dt The time delta for each frame step
# @param n_steps The number of frames to calculate
def symplectic_euler(init_particles, calc_force_func, dt, n_steps):
    # Create a structured array to store results for all time steps and set the initial state
    res_partic_seq = np.zeros((n_steps + 1, len(init_particles)), dtype=custom_types.particle_type)
    res_partic_seq[0] = init_particles

    for n in range(n_steps):
        # Determine the forces acting on each celestial body as an array of 2D vectors
        force = calc_force_func(res_partic_seq[n])

        # Update velocity
        res_partic_seq[n + 1]['x_velocity'] = (
                res_partic_seq[n]['x_velocity'] + dt * force['x'] / res_partic_seq[n]['mass'])
        res_partic_seq[n + 1]['y_velocity'] = (
                res_partic_seq[n]['y_velocity'] + dt * force['y'] / res_partic_seq[n]['mass'])

        # Update position
        res_partic_seq[n + 1]['x_position'] = (
                res_partic_seq[n]['x_position'] + dt * res_partic_seq[n + 1]['x_velocity'])
        res_partic_seq[n + 1]['y_position'] = (
                res_partic_seq[n]['y_position'] + dt * res_partic_seq[n + 1]['y_velocity'])

        # Copy mass and brightness
        res_partic_seq[n + 1]['mass'] = res_partic_seq[n]['mass']
        res_partic_seq[n + 1]['brightness'] = res_partic_seq[n]['brightness']

    return res_partic_seq


# This function is the one that does the most grunt work and uses 99+% of the CPU time during larger calculations.
# Its time complexity is n^2 where n is the number of particles.
# @param particles The frame of particles to calculate the force of each individual particle from
@njit  # This simple njit decorator gives us insane amounts of optimization with LLVM based JIT compilation
def calculate_force(particles):
    no_particles = len(particles)  # Number of celestial bodies
    G = g_numerator / no_particles  # Gravitational constant, gets weaker with more particles
    force = np.zeros(no_particles, dtype=custom_types.vector2d_type)  # Initial array of forces
    R_ij = np.array([0.0, 0.0], dtype=np.float64)  # The 2D vector between two particles

    for i in range(no_particles):
        for j in range(i + 1, no_particles):
            R_ij[0] = particles[i]['x_position'] - particles[j]['x_position']
            R_ij[1] = particles[i]['y_position'] - particles[j]['y_position']

            # Calculate distance between two particles
            r_ij = np.sqrt(pow(R_ij[0], 2) + pow(R_ij[1], 2))

            fx = R_ij[0] * -G * particles[i]['mass'] * particles[j]['mass'] / (r_ij + epsilon) ** 3
            fy = R_ij[1] * -G * particles[i]['mass'] * particles[j]['mass'] / (r_ij + epsilon) ** 3

            # The force on particle i from j is the above calculated force
            force[i]['x'] += fx
            force[i]['y'] += fy
            # The force acting on particle j in relation to particle i is the same force as on particle i but inverted
            force[j]['x'] += -fx
            force[j]['y'] += -fy

    return force
