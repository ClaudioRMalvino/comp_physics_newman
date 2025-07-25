"""
Exercise 5.22: Differentating by integrating

Textbook: Computational Physics by Mark Newman 
"""

from cmath import exp
from math import factorial, pi


N = 10000
for m in range(4):
    sum = 0
    for k in range(N):
        sum += exp((-1j * pi * k * m) / N)
    result = (factorial(m) / N) * sum
    print(f"{m}th derivative = {result}")
