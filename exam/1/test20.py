def isIPv4Address(inputString):

    return True if len(inputString.split(".")) == 4 and [False for n in (inputString.split(".")) if not n.isdigit()] == [] and [False for n in inputString.split(".") if len(n) != len(str(int(n))) or int(n) not in range(0, 256)] == [] else False


print(isIPv4Address("0.253.123.54"))
