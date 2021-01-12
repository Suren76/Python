input_n =  [5, 9, 23, 0, -2, -1]  #Output:   [[5, 9, 23], [5, 9, 0], [5, 9, -2], [5, 9, -1], [5, 23, 0], [5, 23, -2], [5, 23, -1], [5, 0, -2], [5, 0, -1], [5, -2, -1], [9, 23, 0], [9, 23, -2], [9, 23, -1], [9, 0, -2], [9, 0, -1], [9, -2, -1], [23, 0, -2], [23, 0, -1], [23, -2, -1], [0, -2, -1]]
def combo_2(lst,n):
    if n==0:
        return [[]]
    list1=[]
    for i in range(0,len(lst)):
        num1=lst[i]
        skp_list=lst[i+1:]
        for other_list in combo_2(skp_list,n-1):
            list1.append([num1]+other_list)
    return list1

print(combo_2(input_n,3))