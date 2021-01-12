num_list = [[1, 10, 2, 2, 3],[1, 4, 43, -112]]
def max_num(numbers):
    for num1 in numbers:
        for num2 in numbers:
            if num1 < num2 :
                max_num = num2
    return max_num
x = 0
while x < len(num_list):
    print(max_num(num_list[x]))
    x +=1