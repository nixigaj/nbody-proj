import utils
import constants
import numpy as np
import matplot
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
    g = 100 / no_particles  # Gravitational constant
    force = np.zeros(no_particles, dtype=custom_types.vector2d_type)

    # Sum up all masses in proportion to their distance from particle_j
    for i in range(no_particles):
        for j in range(no_particles):
            if i == j:
                continue

            # Vector describing the position of particle_i relative to particle_j
            R_ij = np.array((paricles[i]['x_position'] - paricles[j]['x_position'],
                             paricles[i]['y_position'] - paricles[j]['y_position']),
                            dtype=custom_types.vector2d_type)

            # r_ij describes the distance between particle_i and particle_j
            r_ij = np.sqrt(R_ij['x'] ** 2 + R_ij['y'] ** 2)

            coefficient = paricles[j]['mass'] / (r_ij + constants.epsilon) ** 3

            force[i]['x'] += R_ij['x'] * coefficient
            force[i]['y'] += R_ij['y'] * coefficient

        # Complete the equation for force
        force[i]['x'] *= -g * paricles[i]['mass']
        force[i]['y'] *= -g * paricles[i]['mass']

    return force


if __name__ == "__main__":
    particles = utils.load_particles_file('input_data/ellipse_N_00010.gal')

    # maybe TODO? solve_ivp
    #resulting_particles = integrate.solve_ivp(nbody_function, [0, dt*ITERATIONS], particles, t_eval=np.arange(0, dt*ITERATIONS, dt))

    iterations = 200
    resulting_particles = symplectic_euler(particles, calculate_force, constants.dt, iterations)
    matplot.show_particles_single(resulting_particles[-1])
    ref_particles = utils.load_particles_file('ref_output_data/ellipse_N_00010_after200steps.gal')

    print("particles:", resulting_particles[-1])
    print("\nref particles:", ref_particles)
