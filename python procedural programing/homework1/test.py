a = int(input())
b = int(input())
c = int(input())
d = int(input())

a = a * 1000
b = b * 100
c = c * 10

x = a + b + c + d
print(x)

# 1
a = a * 5

x = a + b + c + d
print(x)

# 2
a = a / 5
c = (c / 10) ** 4 * 10

x = a + b + c + d
print(x)

# 3
c = (c / 10) ** 0.25 * 10
d = d + 8

x = a + b + c + d
print(x)
