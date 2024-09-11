from utils import load_bodies_file
from constants import *
import numpy as np
#import scipy.integrate as integrate

# Constants for better readability in code
ITERATIONS = 200
X = 0
Y = 1


def symplectic_euler(bodies, force_func, dt, n_steps):
    resulting_bodies = np.zeros((n_steps + 1, bodies[:,0].size, bodies[0,:].size))
    resulting_bodies[0,:] = bodies 

    column_size = bodies[:,0].size

    body_pos = resulting_bodies[:,:,0:2]
    #print("body_pos: {}".format(body_pos))
    body_vel = resulting_bodies[:,:,3:5]
    #print("body_vel: {}".format(body_vel))
    mass = bodies[:,2]
    for n in range(n_steps):
        # Determine the forces acting on each celestial body
        force = force_func(body_pos[n], mass)

        acceleration = np.zeros((force.size, 2))

        for i in range(column_size):
            acceleration[i][X] = force[i][X]/mass[i]
            acceleration[i][Y] = force[i][Y]/mass[i]

        for i in range(column_size):
            body_vel[n + 1][i][X] = body_vel[n][i][X] + dt * acceleration[i][X]
            body_vel[n + 1][i][Y] = body_vel[n][i][Y] + dt * acceleration[i][Y]

        for i in range(column_size):
            body_pos[n+1][i][X] = body_pos[n][i][X] + dt * body_vel[n+1][i][X]
            body_pos[n+1][i][Y] = body_pos[n][i][Y] + dt * body_vel[n+1][i][Y]

    return resulting_bodies



def calculate_force(position, mass):
    N = position[:,0].size # Number of celestial bodies
    G = 100./N # Gravitational constant
    force = np.zeros((N, 2), dtype=np.float64)

    # sum up all of the masses in proportion to their distance from particle_j
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            # Vector describing the position of particle_i relative to particle_j
            R_ij = np.array([position[i][X] - position[j][X],
                            position[i][Y] - position[j][Y]], dtype=np.float64)

            # r_ij describles the distance between particle_i and particle_j
            r_ij = np.sqrt(pow(R_ij[X], 2)  + pow(R_ij[Y], 2))

            coefficient = mass[j]/pow(r_ij + epsilon, 3)

            force[i] += [R_ij[X] * coefficient, R_ij[Y] * coefficient]

        # Complete the equation for force
        force[i] *= (-1) * G * mass[i]
    return force


if __name__ == "__main__":
    particles = load_bodies_file('../input_data/circles_N_2.gal')
    #resulting_particles = integrate.solve_ivp(nbody_function, [0, dt*ITERATIONS], particles, t_eval=np.arange(0, dt*ITERATIONS, dt))
    resulting_particles = symplectic_euler(particles, calculate_force, dt, ITERATIONS)
    #ref_particles = load_bodies_file('../ref_output_data/ell.gal')
    

    print("particles: {}\n\n".format(resulting_particles[-1]))
    #print("ref particles: {}\n\n".format(ref_particles))

