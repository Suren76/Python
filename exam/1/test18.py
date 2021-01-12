def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return True if max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft, friendsRight) else False

print(areEquallyStrong(15,10,10,15))