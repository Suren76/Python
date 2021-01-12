# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

inputArray = [3, 6, -2, -5, 7, 3]


def adjacentElementsProduct(inputArray):

    if type(inputArray) == list and 2 <= len(inputArray) <= 10:

        for elm in inputArray:
            if type(elm) != int or elm not in range(-1000, 1001):
                return "You input incorrect data"

        i = 0
        max_prod = -1000

        while i < len(inputArray)-1:
            if max_prod < inputArray[i]*inputArray[i+1]:
                max_prod = inputArray[i]*inputArray[i+1]
                print(max_prod)
            i += 1

        return max_prod

    else:

        return "You input incorrect data"


print(adjacentElementsProduct([-23, 4, -3, 8, -12]))
