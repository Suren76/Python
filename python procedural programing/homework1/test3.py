x = int(input())
if x <= -8 :
    print("1.0 "bool(x))         #1.0
elif x > 12 :
    print("1.2 "bool(x))         #1.2
if x > 10 and x <= 50:
    print("2 "bool(x))         #2
if x > -10 and x < 10:
    print("3.0 "bool(x))         #3.0
elif x != 20 :
    print("3.1 "bool(x))         #3.1
elif x > 50 :
    print("3.2 "bool(x))         #3.2
if x > -10 and (x < 10 or x != 20 or x > 50):
    print("3 "bool(x))         #3