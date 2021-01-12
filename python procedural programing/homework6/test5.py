from geopy.distance import great_circle
from math import sin, cos, sqrt, atan2, radians

# Function call: points_distance([23.5, 67.5], [25.5, 69,5])
# Function return : 300.67


def points_distance(point1, point2):

    R = 6373.0

    x1 = radians(point1[0])
    x2 = radians(point2[0])
    y1 = radians(point1[1])
    y2 = radians(point2[1])

    x = x2 - x1
    y = y2 - y1

    a = sin(x / 2)**2 + cos(x1) * cos(x2) * sin(y / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


print(points_distance([23.5, 67.5], [25.5, 69.5]))

a = [23.5, 67.5]
b = [25.5, 69.5]
print(great_circle(a, b))
