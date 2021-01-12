#10 12
#1 2

def swimmer(a,b,x,y):

    return min(x,y) if x <= a/2 and y <= b/2 else min([a-x,b-y])

print(swimmer(10,12,1,2))
print(swimmer(10,12,7,8))