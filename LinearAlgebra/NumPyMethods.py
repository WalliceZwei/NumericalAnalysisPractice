import numpy as np

# arrays
matrix = np.array([[1, 2], [3, 4]])
matrix3 = np.array([[1.5, 2], [3, 4]])
matrix2 = np.array([[1, 1], [1, 1.0001]])
vector1 = np.array([1, 2])
vector2 = np.array([3, 4])
vector3 = np.array([0, 1])
orthomatrix = np.array(
    [[1 / np.sqrt(2), 1 / np.sqrt(2)], [-1 / np.sqrt(2), 1 / np.sqrt(2)]]
)

# shape
print(np.shape(matrix))

# determinant
num = np.linalg.det(matrix)
print(num)

# condition number
num2 = np.linalg.cond(matrix2)
print(num2)

# rank
fullrank = np.linalg.matrix_rank(matrix3)
fullrank2 = np.linalg.matrix_rank(matrix2)
print(fullrank)
print(fullrank2)

# Matrix Vector, Vector Vector, Matrix Matrix

print(matrix @ matrix3)
print(vector1 @ vector2)
print(matrix @ vector1)


# inverse
num = np.linalg.inv(orthomatrix)
print(num)

# Solves Ax=b
numsy = np.linalg.solve(matrix, vector3)
print(numsy)

# Identity Matrix

matri = np.eye(4)
print(matri)

# Matrix Filling

matri = np.full((3, 5), 11)
print(matri)

# Matrix Powers


# Transpose

# np.transpose()
matri = matrix.T

print(matri)
