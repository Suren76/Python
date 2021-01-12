arr = ["anymore", "raven", "me", "communicate"],["wish", "slightly", "understand", "longer" , "unexpected", "heart"]
def sum_maxmin(array):
    maximum = 0
    for word in array:
        if len(word) > maximum:
            maximum = len(word)
    minimum = maximum
    for word in array:
        if len(word) < minimum:
            minimum = len(word)
    return maximum+minimum

x = 0
while x < len(arr):
    print(sum_maxmin(arr[x]))
    x +=1