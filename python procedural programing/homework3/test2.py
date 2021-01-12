a = input("Years : ")
if a == int:
    if a <= 2:
        dy = a*10.5
        print("{:.0f}".format(dy))
    elif a > 2:
        dy = 2*10.5
        dy = dy+(4*(a-2))
        print("{:.0f}".format(dy))
else:
        print("Input only number")
    