def areSimilar(a, b):
    if type(a) == list and type(b) == list and 3<= len(a) <= 10**5 and len(a)==len(b):
        if a==b:
            return True
        i = 0
        while i<len(a):
            if a[i]==b[i] and 3<=a[i]<=1000 and 3<=b[i]<=1000:
                a.pop(i)
                b.pop(i)
            else:
                i += 1
        if len(a)!=2:
            return False
        b.reverse()
        if a==b:
            return True
        else:
            return False


a = [3, 4, 6]
b = [6, 4, 3]

print(areSimilar(a,b))