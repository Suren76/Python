def evenDigitsOnly(n):
    
    return True if set([False if int(num)%2 != 0 else True for num in str(n)]) == set([True]) else False
    
    #for num in str(n):
    #    if int(num)%2 != 0:
    #        return False
    #return True

print(evenDigitsOnly(12248))