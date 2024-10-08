# nbody-proj

Erik Junsved and Felix Ljungkvist

Programatically simulating bodies interaction in space.

## Usage

This program is only tested on Glibc-based Linux distributions.

### Dependencies

- Python
- Pip
- Make
- GCC (optional, for helper tools)
- Go (optional, for helper tools)

### Running simulation

Install Python dependencies:

```sh
pip install -r requirements.txt
```

Execute the program with `./src/main.py`

```
Usage: ./src/main.py calc [no_iterations] [input_file] [output_file] [full_sim_output_file (optional)]
       ./src/main.py show [no_iterations] [full_sim_input_file]
```

### Building helper tools

```sh
make
```

The executables for the helper tools are now available as `./cmp_gal` for comparing GAL files
and `./print` for printing the contents of GAL files in a human readable fashion.

## Results

### Machine specifications

- **OS:** Red Hat Enterprise Linux 9.3
- **Kernel version:** 5.14.0
- **Python/Pip version:** 3.12.1
- **CPU:** AMD Ryzen 5 5600 at 3.5 GHz (6 cores, 12 threads, AVX2 support)
- **RAM:** 64GB Dual-channel ECC DDR4 at 3000 MT/s

### Data table for 3000 bodies and 100 steps

| Test                      | Real (s) | User (s) | Kernel (s) |
|---------------------------|----------|----------|------------|
| Original                  | 3099.676 | 3091.845 | 1.010      |
| Key-value array access    | 7046.221 | 7027.264 | 2.022      |
| Traditional optimizations | 4018.918 | 4008.826 | 0.918      |
| Numba JIT for force       | 3.181    | 4.556    | 0.136      |

Note that the original force function could not be JIT compiled by Numba.

### Data table for 10000 bodies and 1000 steps

| Test                | Real (s) | User (s) | Kernel (s) |
|---------------------|----------|----------|------------|
| Numba JIT for force | 220.46   | 221.173  | 0.300      |
