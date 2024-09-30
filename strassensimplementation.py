import math

def create_matrix(file):
    with open(file, 'r') as file:
        content = file.read()
    content = content.replace(" ", "")
    content = content.replace("{", "")

    matrix = []
    row = []
    num = ''
    i = 0
    stop = len(content)
    while i != stop:
        if content[i] == '}':
            num = int(num)
            row.append(num)
            num = ''
            matrix.append(row)
            row = []
            i += 2
        elif content[i] == ',':
            num = int(num)
            row.append(num)
            num = ''
            i += 1
        else:
            num += content[i]
            i += 1

    return matrix

def pad_matrix(matrix, n):
    matrixxl = len(matrix[0])
    matrixyl = len(matrix)
    for row in matrix:
        for i in range(matrixxl, n):
            row.append(0)
    for i in range(matrixyl, n):
        matrix.append([0 for i in range(n)])
    return matrix


def create_and_pad_matrices(file1, file2):
    matrix1 = create_matrix(file1)
    matrix2 = create_matrix(file2)
    matrix1xL = len(matrix1[0])
    matrix1yL = len(matrix1)
    matrix2xL = len(matrix2[0])
    matrix2yL = len(matrix2)
    n = max(matrix1xL, matrix1yL, matrix2xL, matrix2yL)
    while math.log(n, 2) % 1 != 0:
        n += 1
    print(n)
    matrix1 = pad_matrix(matrix1,n)
    matrix2 = pad_matrix(matrix2,n)

    return [matrix1, matrix2]



print(create_and_pad_matrices('1a-1.txt', '1b-1.txt'))
