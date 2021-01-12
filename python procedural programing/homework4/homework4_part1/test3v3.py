num_list = [[1, 10, 2, 2, 3],[1, 4, 43, -112],[-1,-4,-43,-112]]
def max_num(numbers):
    max_num = numbers[0]
    for num1 in numbers:
            if max_num < num1 :
                max_num = num1
    return max_num
x = 0
while x < len(num_list):
    print(max_num(num_list[x]),"\n")
    x +=1