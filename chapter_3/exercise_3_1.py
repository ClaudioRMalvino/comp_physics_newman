import numpy as np
import matplotlib.pyplot as plt

"""
Exercise 3.1: Plotting experimental data

Textbook: Computational Physics by Mark Newman
"""


def running_avg(r, y_k):
    """
    Function calculates the running average of the provided data.
    """
    K = np.arange(5, len(y_k)-5)
    M = np.arange(-r, r+1)
    mu = (1 / (2 * r + 1))
    Y_k = []
    for k in K:
        y_sum = 0
        for m in M:
            y_sum += y_k[k + m]
        Y_k.append(mu*y_sum)
    return np.asarray(Y_k, dtype=float)


data = np.loadtxt("sunspots.txt", float)
x = data[:, 0]
y = data[:, 1]
print(running_avg(r=5, y_k=y[0:1000]))

plt.plot(x[0:1000], y[0:1000])
plt.plot(x[5:995], running_avg(r=5, y_k=y[0:1000]))
plt.title("Sunspots vs Time")
plt.xlabel("t, months")
plt.ylabel("Number of Observed Sunspots")
plt.legend(labels=["Sunspots", "Running Avg."])
plt.show()
