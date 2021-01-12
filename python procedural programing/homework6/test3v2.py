# Function call:  float_to_ratio(4.2)
# Function return: 21/5

# Function call:  float_to_ratio(3.5)
# Function return: 7/2


from fractions import Fraction


def float_to_ratio(value):
    
    return Fraction(value).limit_denominator()


print(float_to_ratio(4.22))
print(float_to_ratio(3.5))
