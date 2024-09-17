#!/usr/bin/env python

import sys
import matplot
import utils
import simulation as sim
import constants


def usage():
    print(
        f"Usage: {sys.argv[0]} calc [no_iterations] [input_file] [output_file] [full_sim_output_file (optional)]\n"
        f"       {sys.argv[0]} show [no_iterations] [full_sim_input_file]")
    exit(1)


def calculate(no_iterations, input_file, output_file, full_sim_output_file=None):
    init_particles = utils.load_particles_file(input_file)
    resulting_particles = sim.symplectic_euler(init_particles, sim.calculate_force, constants.dt, no_iterations)

    utils.write_particles_file(output_file, resulting_particles[-1])

    if full_sim_output_file is not None:
        utils.write_particles_arr_file(full_sim_output_file, resulting_particles)


def show(no_iterations, full_sim_input_file):
    resulting_particles = utils.load_particles_arr_file(full_sim_input_file, no_iterations)

    def update_fun(frame, particles):
        index = frame % no_iterations
        updated_particles = resulting_particles[index]

        particles['x_position'][:] = updated_particles['x_position']
        particles['y_position'][:] = updated_particles['y_position']

    matplot.show_particles_multi(resulting_particles[0], no_iterations, update_fun)


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        usage()

    no_iterations = 1
    try:
        no_iterations = int(sys.argv[2])
    except ValueError:
        print(f"Invalid number of iterations: {sys.argv[2]}")
        usage()

    if sys.argv[1] == "calc" and 5 <= len(sys.argv) <= 6:
        if len(sys.argv) == 6:
            calculate(no_iterations, sys.argv[3], sys.argv[4], sys.argv[5])
        else:
            calculate(no_iterations, sys.argv[3], sys.argv[4])
        exit(0)

    if sys.argv[1] == "show" and len(sys.argv) == 4:
        show(no_iterations, sys.argv[3])
        exit(0)

    usage()
