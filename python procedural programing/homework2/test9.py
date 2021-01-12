a = float(input())

#1
print("{:.2f}".format(a),)

#2
a =str(a)
x = int(a[4])
if x < 5:
    print(a[:4])
elif x >= 5:
    a1 = int(a[3])+1
    a = a.replace(a[3],str(a1))
    print(a[:-1])

