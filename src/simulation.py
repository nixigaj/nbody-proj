from custom_types import particle_type
from utils import load_bodies_file, print_body
from constants import *
import numpy as np

# Constants for better readability in code
ITERATIONS = 200
X = 0
Y = 1


def get_gravitational_force_on_particle(particle_i, all_particles):
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


# Updates the particle values for t+1
def update_particle_values(particle, acting_force):
    # Determine the new velocity
    particle['x_velocity'] += dt * acting_force[X]
    particle['y_velocity'] += dt * acting_force[Y]

    # Determine the new position of the particle
    particle['x_position'] += dt * particle['x_velocity']
    particle['y_position'] += dt * particle['y_velocity']






if __name__ == "__main__":
    particles = load_bodies_file('../input_data/ellipse_N_00010.gal')
    for n in range(ITERATIONS):
        force = np.zeros((particles.size, 2))
        for i in range(particles.size):
            force[i] = get_gravitational_force_on_particle(particles[i], particles)
            #print("force: {}".format(force))

        for i in range(particles.size):
            update_particle_values(particles[i], force[i])

#    for particle in particles:
#        print_body(particle)
    ref_particles = load_bodies_file('../ref_output_data/ellipse_N_00010_after200steps.gal')
    print("particles: {}\n\n".format(particles))
    print("ref particles: {}\n\n".format(ref_particles))

