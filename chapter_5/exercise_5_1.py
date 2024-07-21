import numpy as np
import matplotlib.pyplot as plt

"""
Exercise 5.1: Utilizing the Trapezoidal Rule

Textbook: Computational Physics by Mark Newman
"""

def trap_int(t, vel, a, b):
    """
    Function utilizes the extended trapezoidal rule to integrate V(t)
    and solve for x(t).
    """

    N = len(vel)
    h = (b - a)/N
    s = 0
    distance = [0]

    # Iterates from k  [0, 99] as we must move along until we reach k+1
    for k in range(N-1):
        s += 0.5 * h * (vel[k] + vel[k+1])
        # Appends the distance with displacements at time t
        distance.append(distance[-1] + 0.5 * h * (vel[k-1] + vel[k]))
    return s, distance

def plot_func(t, vel):
    """
    Function plots a graph of velocity and distance as a function
    of time.
    """
    # Creates plots
    fig, ax1 = plt.subplots(figsize=(10,6))

    ax1.set_xlabel('Time, s')
    ax1.set_ylabel(r'Velocity, $\frac{m}{s}$', color='b')
    ax1.plot(t, vel, color='b', label='Velocity')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create second axis for distance
    ax2 = ax1.twinx()
    ax2. set_ylabel("Distance, m", color='r')
    ax2.plot(t, distance[1], color='r', label='Distance')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title("Velocity and Displacement vs Time")
    fig.legend(loc="upper right",
        bbox_to_anchor=(1,1),
        bbox_transform=ax1.transAxes)
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":

    data = np.loadtxt("velocities.txt", float)
    t = data[:, 0]
    vel = data[:, 1]
    a = 0
    b = 100

    distance = trap_int(t, vel, a, b)
    print(f"Total displacement: {round(distance[0], 2)}")

    plot_func(t, vel)
