a = input()
d=l=0
for b in a:
    if b.isdigit():
        d += 1
    elif b.isalpha():
        l += 1
print("Letters", l)
print("Digits", d)