import sys

from src.utils import load_bodies_file, print_body_arr

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} [input_file] [output_file]")
    exit(1)


bodies = load_bodies_file(sys.argv[1])

print_body_arr(bodies)
