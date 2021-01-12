print("Input lengths of the triangle sides:  ")
x = int(input())
y = int(input())
z = int(input())
if x == y and y == z:
    print("An equilateral triangle")
elif x == y or y == z or z == x:
    print("An isosceles triangle")
elif x != y and y != z and z != x:
    print("A scalene triangle")