# Function call: gcd(252, 105)
# Function return: 21

# Function call: gcd(147, 105)
# Function return: 21

A, B = [252, 147, 270], [105, 105, 192]


def gcd(A, B):

    r = A % B

    if r == 0:
        return B

    return gcd(B,r)

print(gcd(A[0], B[0]))
print(gcd(A[1], B[1]))
print(gcd(A[2], B[2]))
