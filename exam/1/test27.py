def alphabeticShift(inputString):
    import string as st
    inputString = list(inputString)
    string_list = list(st.ascii_letters)
    for i in range(len(inputString)):
        if inputString[i] == "z":
            inputString[i] = "a"
        elif inputString[i] == "Z":
            inputString[i] = "A"
        else:
            inputString[i] = string_list[string_list.index(inputString[i])+1]
    return "".join(inputString)

print(alphabeticShift("codesignal"))