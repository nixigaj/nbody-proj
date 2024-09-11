import sys
import matplot
import utils
import simulation as sim
import constants


def usage():
    print(f"Usage: {sys.argv[0]} [no_iterations] [input_file] [output_file]")
    exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()

    no_iterations = 1
    try:
        no_iterations = int(sys.argv[1])
    except ValueError:
        print(f"Invalid number of iterations: {sys.argv[1]}")
        usage()

    init_particles = utils.load_particles_file(sys.argv[2])
    resulting_particles = sim.symplectic_euler(init_particles, sim.calculate_force, constants.dt, no_iterations)

    utils.write_particles_file(sys.argv[3], resulting_particles[-1])

    def update_fun(frame, particles):
        index = frame % no_iterations
        updated_particles = resulting_particles[index]

        particles['x_position'][:] = updated_particles['x_position']
        particles['y_position'][:] = updated_particles['y_position']

    matplot.show_particles_multi(init_particles, no_iterations, update_fun)
