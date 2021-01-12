from math import sin,cos,pi


def cylinder(height, radius):

    V = pi*radius**2*height

    A = 2*pi*radius*height+2*pi*(radius**2)

    return {'Volume': V, 'Area': A}


def sphere(radius):

    V = 4/3 * pi * radius**3

    A = 4*pi*radius**2

    return {'Volume': V, 'Area': A}


def radian(degree):

    radian = degree/57.29577951308232

    return radian


def ctg(x):
    return (cos(x)/sin(x))


def polygon(number_sides, length_side):

    S = (number_sides/4)*length_side**2*ctg(pi/number_sides)

    return S
