arr = [[3, 7, 12, 5, 20, 0], [1, 1, 4, 32, 6]]
def multiplication_of_two(array):
    x = 0
    res = []
    while x < len(array)-1:
        multiplication = array[x]*array[x+1]
        x +=1
        res.append(multiplication)
    return res

x = 0
while x < len(arr):
    print(multiplication_of_two(arr[x]))
    x +=1