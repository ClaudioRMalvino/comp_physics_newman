import numpy as np
import matplotlib.pyplot as plt

"""
Exercise 3.3: Plotting scenning tunneling microscope data for silicon

Textbook: Computational Physics by Mark Newman

You can find the data stm.txt @ https://public.websites.umich.edu/~mejn/cp/  
"""
# Reads data from stm.txt into an array
data = np.loadtxt("stm.txt", float)

# Creates a 2D plot of the surface of silicon structure
plt.imshow(data, origin="lower")
plt.title("STM Visualization of Silicon")
plt.show()
