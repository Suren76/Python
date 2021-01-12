# Function call: sphere(radius)
# Function return: {'Volume': value, 'Area': value}
from math import pi


def sphere(radius):

    V = 4/3 * pi * radius**3

    A = 4*pi*radius**2

    return {'Volume': V, 'Area': A}


print(sphere(5))
