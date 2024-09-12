from utils import load_particles_file
from constants import *
import numpy as np
import custom_types


def symplectic_euler(init_particles, calc_force_func, dt, n_steps):
    # Create a structured array to store results for all time steps
    res_partic_seq = np.zeros((n_steps + 1, len(init_particles)), dtype=custom_types.particle_type)
    res_partic_seq[0] = init_particles  # This should now work correctly

    for n in range(n_steps):
        # Determine the forces acting on each celestial body
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



def calculate_force(paricles):
    no_particles = len(paricles)  # Number of celestial bodies
    G = 100 / no_particles  # Gravitational constant
    force = np.zeros(no_particles, dtype=custom_types.vector2d_type)
    R_ij =  np.array([0.0, 0.0], dtype=np.float64)

    for i in range(no_particles):
        for j in range(i + 1, no_particles):
            R_ij[0] = paricles[i]['x_position'] - paricles[j]['x_position']
            R_ij[1] = paricles[i]['y_position'] - paricles[j]['y_position']

            r_ij = np.sqrt(pow(R_ij[0], 2) + pow(R_ij[1],2))

            fx = R_ij[0] * -G * paricles[i]['mass'] * paricles[j]['mass'] / (r_ij + epsilon) ** 3
            fy = R_ij[1] * -G * paricles[i]['mass'] * paricles[j]['mass'] / (r_ij + epsilon) ** 3

            force[i]['x'] += fx
            force[i]['y'] += fy
            force[j]['x'] += -fx
            force[j]['y'] += -fy

    return force


if __name__ == "__main__":
    particles = load_particles_file('../input_data/circles_N_2.gal')
    #print(particles)
    #print(np.transpose(particles))

    #resulting_particles = integrate.solve_ivp(nbody_function, [0, dt*ITERATIONS], particles, t_eval=np.arange(0, dt*ITERATIONS, dt))
    #resulting_particles = symplectic_euler(particles, calculate_force, dt, 1)
    #show_particles_single(resulting_particles[-1])
    #ref_particles = load_bodies_file('../ref_output_data/ellipse_N_00010_after200steps.gal')
    #show_particles_single(ref_particles)

    #print("particles: {}\n\n".format(resulting_particles[-1]))
    #print("ref particles: {}\n\n".format(ref_particles))
