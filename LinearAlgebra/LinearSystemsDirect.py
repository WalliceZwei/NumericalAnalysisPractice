import numpy as np
from scipy.linalg import lu


test = np.array([[3,-1,2],[0,4,-1],[0,0,2]])
testb = np.array([12,1,4])

gaussiantest = np.array([[1,-4], [0.5,-1]])

vex = np.array([-10,-2])

def BackwardSub(matrix,b): 
    vec = [0] * len(b)
    for x in range (len(matrix)-1,-1,-1):
        if x == len(matrix)-1: 
            vec[x] = b[x] / matrix[x][x]
        else:
            temp = 0
            for _ in range(x+1, len(matrix)):
                temp+=matrix[x][_] * vec[_]
            vec[x] = (b[x] - temp) / matrix[x][x]
    return vec

print(BackwardSub(test,testb))

def GaussianElim(matrix, b): 
    for x in range (len(matrix)):
        for y in range(x+1, len(matrix)):
            div = matrix[y][x] / matrix[x][x]
            for z in range(x+1, len(matrix)):
                matrix[y][z] -= (matrix[x][z]*div)
            b[y] -= (div*b[x])
    return BackwardSub(matrix,b)

print(GaussianElim(gaussiantest, vex))

# LU Decomp solving Ax=b 

lumatrix = np.array([[1,-1,3],[1,1,0],[3,-2,1]])
b = np.array([2,4,1])

# A = LU

L, U = lu(lumatrix, permute_l=True)

# Ly = b
vec1 = np.linalg.solve(L,b)
# Ux = y
vec2 = np.linalg.solve(U,vec1)

print(vec2)



# 5.9.3

matr = np.array([[1,2],[3,4]])

lumatrix = np.array([[7,10],[15,22]])


L,U = lu(lumatrix, permute_l=True)

b = np.array([1,3])

# Ly = b
vec1 = np.linalg.solve(L,matr@b)
# Ux = y
vec2 = np.linalg.solve(U,vec1)

print(vec2)


# Cholesky Decomposition

mat = np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])


def Cholesky(matrix):
    # An n*n matrix
    for x in range(len(matrix)-1):
        matrix[x][x] = np.sqrt(matrix[x][x])
        for y in range(x+1, len(matrix)):
            matrix[y][x] /= matrix[x][x]
        for z in range(x+1, len(matrix)):
            for a in range(z, len(matrix)):
                matrix[a][z] -= (matrix[a][x]*matrix[z][x])
    
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if y > x:
                matrix[x][y] = 0
    
    matrix[len(matrix)-1][len(matrix)-1]=np.sqrt(matrix[len(matrix)-1][len(matrix)-1])
    
    return matrix

print(Cholesky(mat))