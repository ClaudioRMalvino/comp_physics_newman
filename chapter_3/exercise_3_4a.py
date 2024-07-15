from vpython import *

"""
Exercise 3.4 Part a): Construct a 3D representation of sodium chloride lattice

Textbook: Computational Physics by Mark Newman
"""
# Set up the scene
scene = canvas(title='3D Sodium Chloride', width=800,
               height=600, background=color.white)

# Parameters
L = 5
R = 0.3

# Create spheres
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if abs(i+j+k) % 2 == 0:
                sphere(pos=vector(i, j, k), radius=R, color=color.red)
            else:
                sphere(pos=vector(i, j, k), radius=R, color=color.blue)


# Create connecting lines
for i in range(-L, L):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            curve(pos=[vector(i, j, k), vector(i+1, j, k)], color=color.black)

for i in range(-L, L+1):
    for j in range(-L, L):
        for k in range(-L, L+1):
            curve(pos=[vector(i, j, k), vector(i, j+1, k)], color=color.black)

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L):
            curve(pos=[vector(i, j, k), vector(i, j, k+1)], color=color.black)

# Add orbital controls
scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, use scroll wheel or middle button drag or Alt/Option depressed with right button drag."""

# Keep the script running
while True:
    rate(30)
