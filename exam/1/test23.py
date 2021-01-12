def neighbors(matrix,i,j,row,col):

    mine = 0

    if not ((i < 1) or (j < 1)):
        if matrix[i - 1][j - 1]:
            mine+=1

    if not (i < 1):
        if matrix[i - 1][j]:
            mine+=1

    if not ((i < 1) or (j >= col-1)):
        if matrix[i - 1][j + 1]:
            mine+=1

    if not (j >= col-1):
        if matrix[i][j + 1]:
            mine+=1

    if not ((i >= row-1) or (j >= col-1)):
        if matrix[i + 1][j + 1]:
            mine+=1

    if not (i >= row-1):
        if matrix[i + 1][j]:
            mine+=1

    if not ((i >= row-1) or (j < 1)):
        if matrix[i + 1][j - 1]:
            mine+=1

    if not (j < 1):
        if matrix[i][j - 1]:
            mine+=1

    return mine
            
def minesweeper(matrix):
    
    return [[(neighbors(matrix,i,j,len(matrix),len(matrix[0]))) for j in range(len(matrix[0]))] for i in range(len(matrix))]

matrix = [
[True,False,False], 
[False,True,False], 
[False,False,False]]

print(minesweeper(matrix))