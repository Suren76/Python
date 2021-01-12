def matrixElementsSum(matrix):

    if type(matrix) == list and len(matrix) <= 5:
        sum_matrix = 0

        haunted_room = list()
        for i in range(0, len(matrix)):
            if type(matrix[i]) == list and len(matrix[i]) <= 5:
                for j in range(len(matrix[0])):
                    if type(matrix[i][j]) == int and 0 <= matrix[i][j] <= 10:
                        if matrix[i][j] == 0:
                            haunted_room.append(j)
                    else:
                        return "You input incorrect data"

                for k in range(len(matrix[0])):
                    if k not in haunted_room:
                        sum_matrix += matrix[i][k]
            else:
                return "You input incorrect data"

        return sum_matrix
        
    else:
        return "You input incorrect data"


matrixs = [

    [1, 1, 1, 0],
    [0, 5, 0, 1],
    [2, 1, 3, 10]

], [

    [0, 1, 1, 2],
    [0, 5, 0, 0],
    [2, 0, 3, 3]

]
print(matrixElementsSum(matrixs[0]))
print(matrixElementsSum(matrixs[1]))
