"""a = input()
b = input()"""
input_a = ["_, we have a _." ,"If at _ you don’t _, try, try _.","May the _ _ _ _."]
input_b = [["Houston", "problem"],["first", "succeed", "again"],["Force", "be", "with", "you"]]
def replace_char(input_a, input_b):
    i =0 #index
    full_str = str()
    for char in input_a :
        if char == "_":
            char = input_b[i]
            i +=1
        full_str +=char
    return full_str


x = 0
while x < len(input_a):
    print(replace_char(input_a[x],input_b[x]))
    x +=1