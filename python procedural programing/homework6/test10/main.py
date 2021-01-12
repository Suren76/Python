import syunik_itc.geometry as geometry
import syunik_itc.mathematica as mathematica

A, B = [252, 147, 270], [105, 105, 192]


print(mathematica.simple_numbers(0), "\n")
print(mathematica.simple_numbers(8), "\n")
print(mathematica.simple_numbers(97))

print(mathematica.quad_equation(5, 20, 10))

print(mathematica.float_to_ratio(4.2))
print(mathematica.float_to_ratio(3.5))

print(mathematica.gcd(A[0], B[0]))
print(mathematica.gcd(A[1], B[1]))
print(mathematica.gcd(A[2], B[2]))


print(mathematica.points_distance([23.5, 67.5], [25.5, 69.5]))

print(geometry.cylinder(3, 5))

print(geometry.sphere(5))

print(geometry.radian(90))

print(geometry.polygon(2,3))