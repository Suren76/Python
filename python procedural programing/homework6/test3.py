# Function call:  float_to_ratio(4.2)
# Function return: 21/5

# Function call:  float_to_ratio(3.5)
# Function return: 7/2


def float_to_ratio(num):

    num_B = round(num - int(num), 2)

    # A and B is mathematics termin
    B = int(1/num_B)
    A = int(num*B)

    return "{}/{}".format(A, B)


print(float_to_ratio(4.2))
print(float_to_ratio(3.5))
