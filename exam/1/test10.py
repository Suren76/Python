def isLucky(n):
    if type(n) == int and len(str(n)) % 2 == 0 and 10 <= n <= 10**6:
        list_n = [int(c) for c in list(str(n))]
        if sum(list_n[:int(len(str(n))/2)]) == sum(list_n[int(len(str(n))/2):]):
            return True

    return False


print(isLucky(1230))
