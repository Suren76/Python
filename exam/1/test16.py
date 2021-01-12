def arrayChange(inputArray):
    step = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            step += f
    return step

inputArray = [1, 1, 1]

print(arrayChange(inputArray))