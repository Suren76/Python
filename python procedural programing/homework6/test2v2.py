# Quadratic function : (a * x^2) + b*x + c
# a = 5, b = 20, c = 10
# There are 2 roots: -0.585786 and -3.414214

# Call function:    quad_equation(5, 20, 10)
# Function return: (-0.585786, -3.414214)


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
        sol -b/2*a
        return (round(sol, 6))
    else:
        return "The equation has no root."

    


print(quad_equation(5, 20, 10))
