list1 = [[3, 4, 5], [1, 0, 0], [4, 5, 4], [8, 8, -1]] ,[[ 8, 35, 2], [8], [5, 6, -5 , -6], [1, 3, -9, 0, -1]]  ,[[1], [2], [3], [4]]
def lists_sums(num_list):
    sums = []
    for num_sum in num_list:
        sums.append(sum(num_sum))
    return sums
for num_list in list1:
    print(lists_sums(num_list))