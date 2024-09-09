import sys



import utils

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} [input_file] [output_file]")
    exit(1)


bodies = utils.load_bodies_file(sys.argv[1])

utils.print_body_arr(bodies)
