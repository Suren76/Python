def avoidObstacles(inputArray):

    jumps_length = []

    for i in range(1, max(inputArray)):

        a = True

        for n in inputArray:

            if n % i == 0:
                a = False

        if a == True:

            jumps_length.append(i)

    if jumps_length == []:
        return max(inputArray)+1

    return min(jumps_length)


print(avoidObstacles([5, 3, 6, 7, 9]))
