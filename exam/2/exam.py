import re

s1 = "America"
s2 = "Japan"
# AJ rp an
res = s1[0] + s2[0] + s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)] + s1[-1] + s2[-1]

print(res)


# 2

def chars_count(string):
    return {char: string.count(char) for char in set(string)}


print(chars_count("Ararat"))


def chars_count(string):
    return {char: len(re.findall(char, string)) for char in set(string)}


print(chars_count("Ararat"))

# 3

list_a = [1, 2, 3, 4, 5]

list_b = [n * n for n in list_a]
print(list_b)

# 4
# class ZeroDivisionError(Exception):
#    pass


f = open("e.txt")
file_content = [n.rstrip('\n') for n in f]

try:

    a = int(file_content[0]) / int(file_content[1])

    if not file_content[0].isdigit() or not file_content[1].isdigit():
        raise TypeError

    print(a)

except ZeroDivisionError:
    print("input have a 0")

except TypeError:
    print("incorrect Data")

finally:
    f.close()


def print_num(n):
    if n == 0:
        return 0
    print_num(n - 1)
    print(n)


print_num(10)

s = "(abc(def)ghi)"
a = re.findall(r"\w+", (re.findall(r"\(\w+\)", s)[0]))[0]
print(a)


class A(object):
    def __init__(self):
        print('class A')


class B(object):
    def __init__(self):
        print('class B')


class C(A, B):
    def __init__(self):
        print('class C')
        super().__init__()


obj1 = C()
print(C.mro())
