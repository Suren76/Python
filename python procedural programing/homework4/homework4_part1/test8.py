arr = [[1, "10", "hi", 2, 3],[1, 4, "i am a string", "456"]]
def characters(array):
    number = 0
    string = 0
    for char in array:
        if type(char) == int :
            number += 1
        if type(char) == str:
            string += 1
    return "Numbers:",number,"Strings:",string

x = 0
while x < len(arr):
    print(characters(arr[x]))
    x +=1