
input_list = [[8, 0, 1, "hey", 12, 5 , True, "2", None, 7, 3] ,[8, 8, "meh", 6] ,[None, None, 1, 5, 9, False]]

def filter_num(list_1):
    # Filtering by digit
    list_2 = []
    for char in list_1:
        if type(char) == int:
            list_2.append(char)

    # Filtering by even or odd
    list_even = []
    list_odd = []
    for num in list_2:
        if num % 2:
            list_even.append(num)
        else:
            list_odd.append(num)
    # Union
    list_2 = list_even + list_odd
    return list_2

x = 0
while x < len(input_list):
    print(filter_num(input_list[x]))
    x +=1