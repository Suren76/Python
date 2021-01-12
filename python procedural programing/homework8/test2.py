
#num = 9568
#
# def s_d(num):
#    sum_d = 0
#    for n in str(num):
#        sum_d += int(n)
#    return sum_d
#
#
#sum_d = s_d()
#
# while len(str(sum_d)) > 1:
#    sum_d = s_d(sum_d)


#print('end', sum_d)

# 1
def sum_digits(num):

    if len(str(num)) == 1:
        return num

    sum_d = 0

    for n in str(num):
        sum_d += int(n)

    return sum_digits(sum_d)


print("1", "\n")
print(sum_digits(14))
print(sum_digits(29))
print(sum_digits(999999999999))
print(sum_digits(85468578245245785785558475))
print("\n")

# 2


def sum_digits(num):

    if len(str(num)) == 1:
        return num

    return sum_digits(num % 10+num//10)


print("2", "\n")
print(sum_digits(14))
print(sum_digits(29))
print(sum_digits(999999999999))
print(sum_digits(85468578245245785785558475))

