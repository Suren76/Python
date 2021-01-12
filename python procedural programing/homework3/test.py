a = input("temperature:unit:  ")
#c/5 = f-32/9
if a[-1:] == "C":
    c = int(a[:-1])
    f = ((9*c)/5)+32
    print("{:.0f}".format(f))
elif a[-1:] == "F":
    f = int(a[:-1])
    c = ((f-32)*5)/9
    print("{:.0f}".format(c))
else:
    print("error:You input incorrect temperature format")