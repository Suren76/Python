a = input()

t="" 
for i in a: 
    if i not in t: 
        t+=i 
print(t)

a = ''.join(set(a))
print(a)

