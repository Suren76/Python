"""a = input()
b = input()"""
input_a = ["_, we have a _." ,"If at _ you don’t _, try, try _.","May the _ _ _ _."]
input_b = [["Houston", "problem"],["first", "succeed", "again"],["Force", "be", "with", "you"]]
def replace_char(input_a, input_b):
    d = []
    x =0
    xy = str()
    for char in input_a :
        if char == "_":
            char = input_b[x]
            x +=1
        d.append(char)
        xy +=char
    input_a = xy
    return input_a


x = 0
while x < len(input_a):
    print(replace_char(input_a[x],input_b[x]))
    x +=1