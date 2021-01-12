from random import randrange
a = randrange(1,9)
b = int(input())
if a == b:
    print("Well guessed!")
elif a > b:
    while True: 
        #print("more by "+ str(int(a-b)) +" units")
        b = int(input())
        if a == b:
            print("Well guessed!")
            break
elif b > a:
    while True:
        #print("less by "+ str(int(b-a)) +" units")
        b = int(input())
        if a == b:
            print("Well guessed!")
            break
print(a)