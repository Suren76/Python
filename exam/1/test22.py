def boxBlur(image):

    def pixel(matrix, i, j):
        total = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                total += matrix[x][y]
        return total//9

    return [[pixel(image, i, j) for j in range(1, len(image[0])-1)] for i in range(1, len(image)-1)]


image = [
    [1, 1, 1],
    [1, 7, 1],
    [1, 1, 1]]

print(boxBlur(image))
