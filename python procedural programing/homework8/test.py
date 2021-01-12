def odd_number(num):

    try:
        if int(str(num)[0]) % 2 == 0:

            return False

        return odd_number(int(str(num)[1:]))

    except ValueError:
        return True


print(1)
print(odd_number(5))
print(odd_number(7791))
print(odd_number(4211133))


def odd_number(num):

    if int(str(num)[0]) % 2 == 0:
        return False
    if len(str(num)) == 1:
        return True

    return odd_number(int(str(num)[1:]))


print(2)
print(odd_number(5))
print(odd_number(7791))
print(odd_number(4211133))

