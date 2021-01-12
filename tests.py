"""from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(23.5)
lon1 = radians(67.5)
lat2 = radians(25.5)
lon2 = radians(69.5)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)"""

"""def spiral_numbers(n):
    mtx = [[0]*n for i in range(n)]
    num = 0

        for i in range(n//2+1):

            for j in range(i, n-i):
            num += 1
            mtx[i][j] = num

            for j in range(i+1, n-i):
            num += 1
            mtx[j][n-i-1] = num

            for j in range(n-i-2, i-1, -1):
            num += 1
            mtx[n-i-1][j] = num

            for j in range(n-i-2, i, -1):
            num += 1
            mtx[j][i] = num

        return mtx

for item in spiral_numbers(4):
#print(item) """


# file = open("random_text.txt")


# print(lines_in_list)
# print(x,type(x))

# def sum_digits(number):
#    if number == 0:
#        return 0
#
#    return (number%10) + sum_digits(int(number//10))
#
# print(sum_digits(12345))
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
    return


"You input incorrect data"


# x = "0123456789"
# xa = [1,2,3,4,5,6,7,8,9,0]
# print(x[::-1])


def matrixElementsSum(matrix):
    sum_matrix = 0

    haunted_room = list()
    for i in range(0, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                haunted_room.append(j)
        for k in range(len(matrix[0])):

            if k not in haunted_room:
                sum_matrix += matrix[i][k]

    return sum_matrix


# print(matrixElementsSum([[1, 1, 1, 0],[0, 5, 0, 1],[2, 1, 3, 10]]))


# print(list(range(1,10)))
# a = ["2"]
# print("".join(a))
n = 1230
b = int(len(str(n)) / 2)
# print(sum(int(list(str(n)[:b]))))
# print(list(str(n)[:2:]))
a = {str({"s": "e4"}): "Pass", str({"s": "e3"}): "Pass", str({"s": "e2"}): "Pass", str({"s": "e1"}): "Fail"}
# skip_tree =[n for n in a if n != -1]
programs = [{"program_name": 'matem', "grade": 56}, {"program_name": 'english', "grade": 76}]
for h in programs:
    print(h["grade"])


class Libray:

    def __init__(self, address, books, readers):
        self.address = address
        self.books = books
        self.readers = readers

    @property
    def books_quantity(self):
        return len(self.books)

    def add_book(self, new_book):
        pass


a = Libray("jjj", "kkkk", "j")
ak = Libray("jjjk", "kkkkk", "jl")
j = Libray("jkjj", "kkkk", "j")
k = Libray("jljj", "kkkk", "j")
an = Libray("jjj", "kkkk", "j")
b = [ak, k]
d = [a, j]
print(type(d), len(d), type(ak), "\n", d)
d.append(an)
print(d)
d.append(b)
print(str(d))
