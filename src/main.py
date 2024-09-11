import sys
import matplot
import utils

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} [input_file] [output_file]")
    exit(1)

particles = utils.load_bodies_file(sys.argv[1])


def update_fun(frame, particles):
    particles['x_position'] = (particles['x_position'] + 0.01) % 1  # Shift positions right


matplot.show_particles_multi(particles, update_fun)
