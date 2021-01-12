x = 0b00101010
y = 0b10101010
print(x,y)
print (bin (x | y))
print (bin (x & y))
print(bin (x ^ y))
print (bin (x |~ y))
print (bin (x &~ y))
print(bin (x ^~ y))


z1 = int(x) and int(y) # Equal bin (x | y)
z2 = int(x) or int(y) # Equal bin (x & y)
z3 = int(x) ^ int(y)
print (z1,z2,z3)
print (bin(z1))
print (bin(z2))
print (bin(z3))
print (z1,z2,z3)
