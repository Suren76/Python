def arrayMaximalAdjacentDifference(inputArray):

    max_difference = 0

    for i in range(len(inputArray)-1):
        if abs(inputArray[i]-inputArray[i+1]) > max_difference:
            max_difference = abs(inputArray[i]-inputArray[i+1])

    return max_difference


print(arrayMaximalAdjacentDifference([-1, 1, -3, -4]))
