#Function call: polygon(number sides, length side)
#Function return: Area of polygon

from math import sin,cos,pi

def ctg(x):
    return (cos(x)/sin(x))

def polygon(number_sides, length_side):

    S = (number_sides/4)*length_side**2*ctg(pi/number_sides)

    return S

