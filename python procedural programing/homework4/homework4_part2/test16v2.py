input_n =  [5, 9, 23, 0, -2, -1]  #Output:   [[5, 9, 23], [5, 9, 0], [5, 9, -2], [5, 9, -1], [5, 23, 0], [5, 23, -2], [5, 23, -1], [5, 0, -2], [5, 0, -1], [5, -2, -1], [9, 23, 0], [9, 23, -2], [9, 23, -1], [9, 0, -2], [9, 0, -1], [9, -2, -1], [23, 0, -2], [23, 0, -1], [23, -2, -1], [0, -2, -1]]
def subsets(n,Set):
    return [[i for i,s in zip(Set, status) if int(s)  ] for status in [(format(bit,'b').zfill(len(Set))) for bit in range(2**len(Set))] if sum(map(int,status)) == n][::-1]
print(subsets(3,input_n))