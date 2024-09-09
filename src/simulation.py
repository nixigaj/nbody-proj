from custom_types import particle_type
from utils import load_bodies_file
from constants import *
import numpy as np

# Constants for better readability in code
X = 0
Y = 1


def gravitational_force_on_particle(particle_i, all_particles):
    N = all_particles.size # Number of celestial bodies
    G = 100./N # Gravitational constant
    force = np.array([0.,0.])
    
    # sum up all of the masses in proportion to their distance from particle_j
    for particle_j in all_particles:
        # Vector describing the position of particle_i relative to particle_j
        R_ij = np.array([particle_i['x_position'] - particle_j['x_position'],
                        particle_i['y_position'] - particle_j['y_position']] )

        # r_ij describles the distance between particle_i and particle_j
        r_ij = np.sqrt(pow(R_ij[X], 2)  + pow(R_ij[Y], 2))
        coefficient = particle_j['mass']/(r_ij + epsilon)
        force += [R_ij[X] * coefficient, R_ij[Y] * coefficient]

    # Complete the equation for force
    force *= G * particle_i['mass']
    return force


def set_new_particle_velocity(particle, acting_force):
    print("prev velocity: [{}, {}]".format(particle['x_velocity'], particle['y_velocity']))
    particle['x_velocity'] += dt * acting_force[X]
    particle['y_velocity'] += dt * acting_force[Y]
    print("new velocity: [{}, {}]".format(particle['x_velocity'], particle['y_velocity']))

if __name__ == "__main__":
    particles = load_bodies_file('../input_data/circles_N_2.gal')
    force = gravitational_force_on_particle(particles[0], particles)
    print("force: {}".format(force))
    set_new_particle_velocity(particles[0], force)

