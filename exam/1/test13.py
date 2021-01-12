def alternatingSums(a):
    if type(a) == list and 1<=len(a)<=10**5:
        if {True} == set([True if type(n)==int and 45<= n <=100 else False for n in a ]):
            return [sum(a[::2]),sum(a[1::2])]

a=[50, 60, 60, 45, 70]

print(alternatingSums(a))