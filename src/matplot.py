import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def show_particles_single(particles: np.ndarray):
    plt.figure(figsize=(6, 6))
    ax = plt.gca()

    # Set background color to black
    ax.set_facecolor('black')

    # Plot the positions of the objects
    plt.scatter(particles[:,0], particles[:,1], c='white', s=10)  # white dots with size 10

    # Add x and y axis decorators
    plt.axhline(0, color='white', linewidth=0.5)  # Horizontal axis
    plt.axvline(0, color='white', linewidth=0.5)  # Vertical axis

    # Set x and y-axis limits to range [0, 1]
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Add labels and grid
    plt.xlabel('X Position', color='white')
    plt.ylabel('Y Position', color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Display the plot
    plt.show()

def show_particles_multi(particles: np.ndarray, update_fun):
    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_facecolor('black')
    scat = ax.scatter(particles[:,0], particles[:,1], c='white', s=10)

    # Set x and y-axis limits to range [0, 1]
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Add labels and grid
    plt.xlabel('X Position', color='white')
    plt.ylabel('Y Position', color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    def update(frame):
        update_fun(frame, particles)
        scat.set_offsets(np.c_[particles['x_position'], particles['y_position']])  # Update scatter plot
        return scat,

    # Create the animation
    ani = FuncAnimation(fig, update, frames=200, interval=16, blit=True)

    # Show the animation
    plt.show()
