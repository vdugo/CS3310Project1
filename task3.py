import time
import random

from matrix import multiply, strassen

n = int(input("Enter n for an n x n matrix:"))

# list comprehension to generate an n x n matrix
# populated with random integer values from 0 to 1000
A = [[random.randint(0,1000 + 1) for _ in range(n)] for _ in range(n)]

B = [[random.randint(0,1000 + 1) for _ in range(n)] for _ in range(n)]

print(A)
print(B)

startTimeMultiply = time.time()

C = multiply(A,B,n)

print(C)

endTimeMultiply = time.time()

totalTimeMultiply = endTimeMultiply - startTimeMultiply

print(totalTimeMultiply, "seconds to complete normal matrix multiplication of",n,"by",n,"matrix.")

D = strassen(A,B,n)

print(D)



