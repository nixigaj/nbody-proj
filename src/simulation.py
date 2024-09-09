import numpy as np
N = 2 # Number of celestial bodies
G = 100./N # Gravitational constant
# LxW dimentionless domain L=W=1 such that the x and y positions will be between 0 and 1
L = 1.
W = 1.
dt = 10e-5 # (Delta time) Change in time per iteration in simulation (in seconds)

def gravitational_force_on_particle(particle_i, remaining_particles):
    Force = 0
    for particle_j in remaining_particles:
        # Vector describing the position of particle_i relative to particle_j
        R_ij = np.array(particle_i['x_position'] - particle_j['x_position'],
                        particle_i['y_position'] - particle_j['y_position'] )

        # r_ij describles the distance between particle_i and particle_j
        r_ij = np.sqrt(np.pow(R_ij[0], 2)  + np.pow(R_ij[1], 2))
        F += r_ij
    return F
