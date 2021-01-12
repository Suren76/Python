a = "Hello, ","World! Heyy"
ab = "01234","56789"
print(a[:1]+a.replace(a[0][2],ab[0][1])[1:])