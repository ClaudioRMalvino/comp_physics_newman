"""
Exercise 6.5: Solving for the voltage of a circuit 

Textbook: Computational Physics by Mark Newman
"""

import numpy as np
from cmath import polar

R1, R3, R5 = (1.0e3, 1.0e3, 1.0e3)  # [Ohms]
R2, R4, R6 = (2.0e3, 2.0e3, 2.0e3)  # [Ohms]
C1 = 1.0e-6  # [Farads]
C2 = 0.5e-6  # [Farads]
x_plus = 3.0  # [Volts]
omega = 1 / 1000  # [seconds]

A = np.array(
    [
        [(1 / R1) + (1 / R4) + (1j * omega * C1), (1j * omega * C1), 0],
        [
            -1j * omega * C1,
            (1 / R2) + (1 / R5) + (1j * omega * C1 + 1j * omega * C2),
            -1j * omega * C2,
        ],
        [0, -1j * omega * C2, (1 / R3) + (1 / R6) + (1j * omega * C2)],
    ],
)

v = [x_plus / R1, x_plus / R2, x_plus / R3]

x = np.linalg.solve(A, v)

V = np.exp(1j * omega * 1) * x

for voltage in V:
    r, theta = polar(voltage)
    print(f"Amplitude = {r :.2f}")
    print(f"theta = {theta*180/np.pi :.2f}")
