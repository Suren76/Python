# 2	        2
# 13	        31
# 815796	697518
# 1000      1
# 0001      1

def revers(input_str):

    if len(input_str) == 0:
        return input_str
    
    input_str = str(int(input_str))

    return str(int(input_str[-1] + revers(input_str[0:-1])))


print(revers("2"))
print(revers("13"))
print(revers("815796"))
print(revers("1000"))
print(revers("0001"))
