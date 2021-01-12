# Function call: gcd(252, 105)
# Function return: 21

# Function call: gcd(147, 105)
# Function return: 21

A, B = [252, 147, 270], [105, 105, 192]


def gcd(A, B):

    r = A % B

    if r == 0:
        print(B)
    else:
        gcd(B, r)


print(1, "\n")
gcd(A[0], B[0])
gcd(A[1], B[1])
gcd(A[2], B[2])
print("\n")

# Առաջինում return-ով չեմ կարողացել աշխատեցնել։


def gcd(A, B):

    while True:

        res = A % B

        if res == 0:
            return (B)
            break

        else:
            A, B = B, res


print(2, "\n")
print(gcd(A[0], B[0]))
print(gcd(A[1], B[1]))
print(gcd(A[2], B[2]))
