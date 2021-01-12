def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if elemToReplace == inputArray[i]:
            inputArray[i] = substitutionElem
            
    return inputArray

print(arrayReplace([1,2,1],1,3))