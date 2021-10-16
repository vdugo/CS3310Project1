import math

def multiply(A, B, n):
    # initialize the result n x n matrix with 0's
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def mult(A, B):
    size = len(A)
    # initialize the result n x n matrix with 0's
    result = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
    return result


def strassenHelp(A, B):
    if len(A) <= 100:
        return mult(A, B)
    size = len(A)
    resize = size // 2
    A11 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    A12 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    A21 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    A22 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    B11 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    B12 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    B21 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    B22 = [[0 for _ in range(0, resize)] for _ in range(0, resize)]

    AResult = [[0 for _ in range(0, resize)] for _ in range(0, resize)]
    BResult = [[0 for _ in range(0, resize)] for _ in range(0, resize)]

    for i in range(0, resize):
        for j in range(0, resize):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j + resize]
                A21[i][j] = A[i + resize][j]
                A22[i][j] = A[i + resize][j + resize]

                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j + resize]
                B21[i][j] = B[i + resize][j]
                B22[i][j] = B[i + resize][j + resize]
    
    AResult = add(A11, A22)
    BResult = add(B11, B22)
    p1 = strassenHelp(AResult, BResult)
    AResult = add(A21, A22)
    p2 = strassenHelp(AResult, B11)
    BResult = subtract(B12, B22)
    p3 = strassenHelp(A11, BResult)
    BResult = subtract(B21, B11)
    p4 = strassenHelp(A22, BResult)
    AResult = add(A11, A12)
    p5 = strassenHelp(AResult, B22)
    AResult = subtract(A21, A11)
    BResult = add(B11, B12)
    p6 = strassenHelp(AResult, BResult)
    AResult = subtract(A12, A22)
    BResult = add(B21, B22)
    p7 = strassenHelp(AResult, BResult)
    
    C12 = add(p3, p5)
    C21 = add(p2, p4)
    AResult = add(p1, p4)
    BResult = add(AResult, p7)
    C11 = subtract(BResult, p5)
    AResult = add(p1, p3)
    BResult = add(AResult, p6)
    C22 = subtract(BResult, p2)

    # Merging into 1 matrix
    C = [[0 for _ in range(0, size)] for _ in range(0, size)]
    for i in range(0, resize):
        for j in range(0, resize):
            C[i][j] = C11[i][j]
            C[i][j + resize] = C12[i][j]
            C[i + resize][j] = C21[i][j]
            C[i + resize][j + resize] = C22[i][j]
    return C

def strassen(A,B):
    # Make the matrices dimensions of 2 for the Strassen algorithm
    nextPowerOfTwo = lambda n: 2 ** int(math.ceil(math.log(n, 2)))
    size = len(A)
    m = nextPowerOfTwo(size)
    APrep = [[0 for _ in range(m)] for _ in range(m)]
    BPrep = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(size):
        for j in range(size):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenHelp(APrep, BPrep)
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = CPrep[i][j]
    return C

def add(A, B):
    size = len(A)
    result = [[0 for _ in range(0, size)] for _ in range(0, size)]
    for i in range(0, size):
        for j in range(0, size):
            result[i][j] = A[i][j] + B[i][j]
    return result

def subtract(A, B):
    size = len(A)
    result = [[0 for _ in range(0, size)] for _ in range(0, size)]
    for i in range(0, size):
        for j in range(0, size):
            result[i][j] = A[i][j] - B[i][j]
    return result
