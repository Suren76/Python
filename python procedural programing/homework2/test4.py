a = str(input())
if "ing" not in a[-3:] and len(a)>=3:
    a = a+"ing"
    print(a)
elif "ing" in a[-3:] and len(a)>=3:
    a = a+"ly"
    print(a)
else:
    print(a)