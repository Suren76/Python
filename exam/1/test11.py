def sortByHeight(a):
    if type(a) == list and 1 <= len(a) <= 1000:
        skip_tree =sorted([n for n in a if type(n) == int and 1<= n<=1000 and n != -1])
        sort_a = []
        i = 0
        for n in a:
            if n == -1:
                sort_a.append(n)
                continue
            n = skip_tree[i]
            sort_a.append(n)
            i +=1
        return sort_a

a = [-1, 150, 190, 170, -1, -1, 160, 180]

print(sortByHeight(a))