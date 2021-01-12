list1 = [[21,  -9, 15, 2116, -71, 33], [ 36, -12, 47, -58, 148, -55, -19, 10],[5, 46, 17, -2, 89, 0, 26 ]]
list2 = [-71 ,-56 ,36]

def num_id(array,find_num):
    c = {}
    for num in array:
        if num == find_num:
            return find_num,array.index(num)
        else:
            if num-find_num < 0:
                c[num] = (num-find_num)*-1
                continue
            c[num] = num-find_num
            
    for min_id in c.items():
        if min(c.values()) == min_id[1]:
            for _ in array:
                if min_id[0] == _:
                    return find_num,array.index(_)

x = 0
while x < len(list1):
    print(num_id(list1[x],list2[x]))
    x +=1