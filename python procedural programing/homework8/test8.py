def print_num_list(n, a=1):

    if n == a:
        return a

    return a, print_num_list(n, a+1)


print(print_num_list(13))
# print((list(range(1,14))))


def print_num_list(n):
    if n >= 0:
        print_num_list(n - 1)
        print(n)


print_num_list(13)
