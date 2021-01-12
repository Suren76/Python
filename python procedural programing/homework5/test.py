ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for num in ls:
#    if num >= 3 and num <= 8:
#        ls[ls.index(num)]= num*-1
#print(ls)
num = [num*-1  if num >= 3 and num <=8 else num for num in ls]
print(num)