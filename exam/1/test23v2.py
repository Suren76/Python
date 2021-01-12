def minesweeper(matrix):

    def neighbors(matrix, i, j, row, col):

        mine = 0

        if j-1 in range(col)\
            and matrix[i][j-1] == True:
                mine += 1

        if j+1 in range(col)\
            and matrix[i][j+1] == True:
                mine += 1

        if j-1 in range(col) and i+1 in range(row)\
            and matrix[i+1][j-1] == True:
                mine += 1

        if j+1 in range(col) and i+1 in range(row)\
            and matrix[i+1][j+1] == True:
                mine += 1

        if j-1 in range(col) and i-1 in range(row)\
            and matrix[i-1][j-1] == True:
                mine += 1

        if j+1 in range(col) and i-1 in range(row)\
            and matrix[i-1][j+1] == True:
                mine += 1

        if i-1 in range(row)\
            and matrix[i-1][j] == True:
                mine += 1

        if i+1 in range(row)\
            and matrix[i+1][j] == True:
                mine += 1

        return mine

    return [[(neighbors(matrix, i, j, len(matrix), len(matrix[0]))) for j in range(len(matrix[0]))] for i in range(len(matrix))]


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

matrix2 = [[True, False, False, True],
           [False, False, True, False],
           [True, True, False, True]]

print(minesweeper(matrix))
print(minesweeper(matrix2))
