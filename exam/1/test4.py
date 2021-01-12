# For n = 2, the output should be
# shapeArea(n) = 5;
# For n = 3, the output should be
# shapeArea(n) = 13.


def shapeArea(n):

    if type(n) == int and 1 <= n <= 10**4:
        return (n**2+(n-1)**2)
    else:
        return "You input incorrect data"


print(shapeArea(2))
print(shapeArea(3))
