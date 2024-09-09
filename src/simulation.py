from custom_types import particle_type
from utils import load_bodies_file
from constants import *
import numpy as np


def gravitational_force_on_particle(particle_i, all_particles):
    N = all_particles.size # Number of celestial bodies
    G = 100./N # Gravitational constant
    force = np.array([0.,0.])
    for particle_j in all_particles:
        # Vector describing the position of particle_i relative to particle_j
        R_ij = np.array([particle_i['x_position'] - particle_j['x_position'],
                        particle_i['y_position'] - particle_j['y_position']] )

        # r_ij describles the distance between particle_i and particle_j
        r_ij = np.sqrt(pow(R_ij[0], 2)  + pow(R_ij[1], 2))
        coefficient = particle_j['mass']/(r_ij + epsilon)
        force += [R_ij[0] * coefficient, R_ij[1] * coefficient]
    
    force *= G * particle_i['mass']

    return force


if __name__ == "__main__":
#    particles = np.array([[
#    ('x_position', 0.5),
#    ('y_position', 0.5),
#    ('mass', 1.2),
#    ('x_velocity', 5),
#    ('y_velocity', 5),
#    ('brightness', 0)
#],[
#    ('x_position', 0.3),
#    ('y_position', 0.8),
#    ('mass', 0.8),
#    ('x_velocity', -82.0),
#    ('y_velocity', 0),
#    ('brightness', 0)
#]], dtype=particle_type)
    particles = load_bodies_file('../input_data/circles_N_2.gal')
    print(gravitational_force_on_particle(particles[0], particles))
