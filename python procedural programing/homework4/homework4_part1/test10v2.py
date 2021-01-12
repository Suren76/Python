list1 = [[21,  -9, 15, 2116, -71, 33], [ 36, -12, 47, -58, 148, -55, -19, 10],[5, 46, 17, -2, 89, 0, 26 ]]
list2 = [-71 ,-56 ,36]

def num_id(inpt_array,find_num):
    c = []
    for num in inpt_array:
        if num == find_num:
            return find_num,inpt_array.index(num)
        else:
            if num-find_num < 0:
                c.append((num-find_num)*-1)
                continue
    for min_id in c:
        if min(c) == min_id:
            for _ in inpt_array:
                if min_id == ((_-find_num)*-1):
                    return find_num,inpt_array.index(_)

x = 0
while x < len(list1):
    print(num_id(list1[x],list2[x]))
    x +=1