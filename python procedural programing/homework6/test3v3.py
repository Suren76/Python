def float_to_ratio(num):

    if len(str(num)) <= 3:
        num_B = round(num - int(num), 2)

        # A and B is mathematics termin
        B = int(1/num_B)
        A = int(num*B)

    if len(str(num)) > 3:

        A = int(num*10**(len(str(num))-2))
        B = 10**(len(str(num))-2)

        while A % 2 == 0 and B % 2 == 0 or A % 5 == 0 and B % 5 == 0:
            if A % 2 == 0:
                A /= 2
                B /= 2
            if A % 5 == 0:
                A /= 5
                B /= 5

    return "{}/{}".format(int(A), int(B))

print(float_to_ratio(4.22))
print(float_to_ratio(3.5))