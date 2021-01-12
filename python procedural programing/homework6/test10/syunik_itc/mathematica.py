from math import sin, cos, sqrt, atan2, radians


def simple_numbers(input_num):

    all_num = list(range(2, input_num+1))

    for num in all_num:

        if num != 0:

            for candidate_num in range(2 * num, input_num+1, num):
                all_num[candidate_num-2] = 0

    all_num = tuple(list(set(all_num))[1:])

    return all_num


def quad_equation(a, b, c):
    """
    Find the root
    """

    d = (b**2) - (4*a*c)

    if d > 0:
        sol1 = (-b-(d**0.5))/(2*a)
        sol2 = (-b+(d**0.5))/(2*a)
        return (round(sol1, 6), round(sol2, 6))
    elif d == 0:
        sol - b/2*a
        return (round(sol, 6))
    else:
        return "The equation has no root."


def float_to_ratio(num):

    if len(str(num)) <= 3:
        num_B = round(num - int(num), 2)

        # A and B is mathematics termin
        B = int(1/num_B)
        A = int(num*B)

    if len(str(num)) > 3:

        A = int(num*10**(len(str(num))-2))
        B = 10**(len(str(num))-2)

        while A % 2 == 0 and B % 2 == 0 or A % 5 == 0 and B % 5 == 0:
            if A % 2 == 0:
                A /= 2
                B /= 2
            if A % 5 == 0:
                A /= 5
                B /= 5

    return "{}/{}".format(int(A), int(B))


def gcd(A, B):

    while True:

        res = A % B

        if res == 0:
            return (B)
            break

        else:
            A, B = B, res


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
