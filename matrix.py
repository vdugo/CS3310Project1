import numpy as np

def multiply(A, B, n):
    # initialize the result n x n matrix with 0's
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def strassen(A, B, n):
    if n == 1:
        return A * B
    a11, a12, a21, a22 = split(A)
    b11, b12, b21, b22 = split(B)
    p1 = strassen(a11 + a22, b11 + b22,n)  # p1 = (a11 + a22) * (b11 + b22)
    p2 = strassen(a21 + a22, b11,n)        # p2 = (a21 + a22) * b11
    p3 = strassen(a11, b12 - b22,n)        # p3 = a11 * (b12 - b22)
    p4 = strassen(a22, b21 - b11,n)        # p4 = a22 * (b21 - b11)
    p5 = strassen(a11 + a12, b22,n)        # p5 = (a11 + a12) * b22
    p6 = strassen(a21 - a11, b11 + b12,n)  # p6 = (a21 - a11) * (b11 + b12)
    p7 = strassen(a12 - a22, b21 + b22,n)  # p7 = (a12 - a22) * (b21 + b22)
    c11 = p1 + p4 - p5 + p7  # c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5            # c12 = p3 + p5
    c21 = p2 + p4            # c21 = p2 + p4
    c22 = p1 + p3 - p2 + p6  # c22 = p1 + p3 - p2 + p6
    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    return C



    

    
