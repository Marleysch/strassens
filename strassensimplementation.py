import math
import time

def add_matrices(matrix1, matrix2):
    matrix3 = []
    row = []
    for i in range(len(matrix1)):
        if i != 0:
            matrix3.append(row)
            row =[]
        for j in range(len(matrix1)):
            row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)
    return matrix3
    
def n3mult(matrix1, matrix2):
    matrix3 = [[0 for x in range(len(matrix1))] for k in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                matrix3[i][j] += matrix1[i][k]*matrix2[k][j]
    return matrix3

def sub_matrices(matrix1, matrix2):

    matrix3 = []
    row = []
    for i in range(len(matrix1)):
        if i != 0:
            matrix3.append(row)
            row =[]
        for j in range(len(matrix1)):
            row.append(matrix1[i][j] - matrix2[i][j])
    matrix3.append(row)
    return matrix3

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
    matrix1yL = len(matrix1)
    matrix1xL = len(matrix1[0])
    matrix2yL = len(matrix2)
    matrix2xL = len(matrix2[0])
    n = max(matrix1yL, matrix2yL, matrix1xL, matrix2xL)
    while math.log(n, 2) % 1 != 0:
        n += 1
    matrix1 = pad_matrix(matrix1,n)
    matrix2 = pad_matrix(matrix2,n)

    return [matrix1, matrix2]

def strassens(matrix1, matrix2):
    # print()
    # print()
    # print(f'matrix1:{matrix1}')
    # print(f'matrix2:{matrix2}')
    if len (matrix1) <= 512:
        return n3mult(matrix1, matrix2)
        # return n3mult(matrix1, matrix2)
    
    a11 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2):
        for j in range(len(matrix1)//2):
            a11[i][j] = matrix1[i][j]
    # print(f'a11 = {a11}')
    
    a12 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2):
        for j in range(len(matrix1)//2, len(matrix1)):
            a12[i][j-len(matrix2)//2] = matrix1[i][j]

    a21 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2, len(matrix1)):
        for j in range(len(matrix1)//2):
            a21[i-len(matrix1)//2][j] = matrix1[i][j]
    
    a22 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2, len(matrix1)):
        for j in range(len(matrix1)//2, len(matrix1)):
            a22[i-len(matrix1)//2][j-len(matrix1)//2] = matrix1[i][j]

    b11 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2):
        for j in range(len(matrix1)//2):
            b11[i][j] = matrix2[i][j]
    # print(f'a11 = {a11}')
    
    b12 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2):
        for j in range(len(matrix1)//2, len(matrix1)):
            b12[i][j-len(matrix1)//2] = matrix2[i][j]

    b21 = [[0 for x in range(len(matrix1) // 2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2, len(matrix1)):
        for j in range(len(matrix1)//2):
            b21[i-len(matrix1)//2][j] = matrix2[i][j]
    
    b22 = [[0 for x in range(len(matrix1)//2)] for k in range(len(matrix1)//2)]
    for i in range(len(matrix1)//2, len(matrix1)):
        for j in range(len(matrix1)//2, len(matrix1)):
            b22[i-len(matrix1)//2][j-len(matrix1)//2] = matrix2[i][j]

    
    # print('calculating m1:')
    m1 = strassens(add_matrices(a11,a22),add_matrices(b11, b22))
    # print('calculating m2:')
    m2 = strassens(add_matrices(a21,a22), b11)
    # print('calculating m3:')
    m3 = strassens(a11,sub_matrices(b12,b22))
    # print('calculating m4:')
    m4 = strassens(a22, sub_matrices(b21,b11))
    # print('calculating m5:')
    m5 = strassens(add_matrices(a11,a12),b22)
    # print('calculating m6:')
    m6 = strassens(sub_matrices(a21,a11), add_matrices(b11,b12))
    # print('calculating m7:')
    m7 = strassens(sub_matrices(a12,a22),add_matrices(b21,b22))

    tl = add_matrices(sub_matrices(add_matrices(m1,m4),m5),m7)
    # print(tl)
    tr = add_matrices(m3,m5)
    bl = add_matrices(m2,m4)
    br = add_matrices(sub_matrices(add_matrices(m1,m3),m2),m6)

    final_matrix = []
    for i in range(len(tl)):
        row = [k for k in tl[i]] + [k for k in tr[i]]
        final_matrix.append(row)
    for i in range(len(bl)):
        row = [k for k in bl[i]] + [k for k in br[i]]
        final_matrix.append(row)

    # print(final_matrix)
    return final_matrix

def sum_matrix(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum

for i in range(1,11):
    time1=time.time()
    file1 = str(i) + "a.txt"
    file2 = str(i) + "b.txt"
    print(f'Problem : {i}')

    matrices = create_and_pad_matrices(file1, file2)
    matrix1 = matrices[0]
    matrix2 = matrices[1]

    print(sum_matrix(strassens(matrix1, matrix2)))
    time2 = time.time()
    print(f'time: {time2-time1}')
    print()
    print()

