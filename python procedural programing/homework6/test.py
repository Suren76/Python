# Call function: simple_numbers(0)
# Function return: ()

# Call function:  simple_numbers(8)
# Output: (2, 3, 5, 7)

# Call function:  simple_numbers(97)
# Function return: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


def simple_numbers(input_num):
    
    """
    Prints the primes.
    """

    all_num = tuple()

    for num in range(2, input_num+1):
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 \
                or num == 2 or num == 3 or num == 5 or num == 7:
            all_num += (num,)

    return all_num


print(simple_numbers(0), "\n")
print(simple_numbers(8), "\n")
print(simple_numbers(97))