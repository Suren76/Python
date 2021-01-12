# Call function: simple_numbers(0)
# Function return: ()

# Call function:  simple_numbers(8)
# Output: (2, 3, 5, 7)

# Call function:  simple_numbers(97)
# Function return: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


def simple_numbers(input_num):
    
    all_num = list(range(2, input_num+1))

    for num in all_num:

        if num != 0:

            for candidate_num in range(2 * num, input_num+1, num):
                all_num[candidate_num-2] = 0

    all_num = tuple(list(set(all_num))[1:])

    return all_num


print(simple_numbers(0), "\n")
print(simple_numbers(8), "\n")
print(simple_numbers(97))
