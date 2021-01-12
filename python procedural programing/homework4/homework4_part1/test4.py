arr = [["hello", "," , "world"],["a", "c", "a"]]
def arr_to_str(array):
    string = str()
    for chars in array :
        string +=chars
    return string

x = 0
while x < len(arr):
    print(arr_to_str(arr[x]))
    x +=1