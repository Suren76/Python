# Function call: radian(90)
# Function return: 1.5714285714285714

from math import pi, radians, degrees


def radian(degree):

    radian = degree*(pi/180)
    return radian


print(radians(90))

print(radian(90))
