# V=πr^2h  and   A=2πrh+2πr^2
# Function call: cylinder(height, radius)
# Function return: {'Volume': value, 'Area': value}


from math import pi


def cylinder(height, radius):

    V = pi*radius**2*height

    A = 2*pi*radius*height+2*pi*(radius**2)

    return {'Volume': V, 'Area': A}


print(cylinder(3, 5))
