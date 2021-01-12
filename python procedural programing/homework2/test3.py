a = "abc", "xyz"
print(a[0])


a = "abc , xyz"
a = a.split(",")
print(a[0])
a = "abc , xyz"
print(a.replace(a[0:2],a[6:8])[:-6],a.replace(a[6:8],a[0:2])[6:])

#a = "Hello, World!"
#a = a.split(",")
#print(a[0])

