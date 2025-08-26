import numpy as np


# Least Squares (Normal Equations)

matrixA = np.array([[1, 0, 1], [2, 3, 5], [5, 3, -2], [3, 5, 4], [-1, 6, 3]])
vecB = np.array([4, -2, 5, -2, 1])

matrixB = matrixA.T @ matrixA
vecY = matrixA.T @ vecB

G = np.linalg.cholesky(matrixB)

solvevec1 = np.linalg.solve(G, vecY)
solvevec2 = np.linalg.solve(G.T, solvevec1)

print(solvevec2)

# Least Squares (QR Decomp)
