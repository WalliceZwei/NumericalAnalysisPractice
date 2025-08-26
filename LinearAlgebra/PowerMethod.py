import numpy as np

randomvec = np.random.randn(3)
randomvec /= np.linalg.norm(randomvec)

randommatrix = np.array([[40, 4, 2], [0, 39, 0], [0, 0, 7]])


def PowerMethod(matrix, vector, steps):
    v = vector
    for _ in range(steps):
        v = matrix @ v
        v /= np.linalg.norm(v)
        eigenvalue = v.T @ (matrix @ v)
        if _ == steps - 1:
            return (eigenvalue, v)


print(PowerMethod(randommatrix, randomvec, 1000))

examp = PowerMethod(randommatrix, randomvec, 25)


def InverseIteration(matrix, vector, steps, alpha):
    v = vector
    for _ in range(steps):
        v = np.linalg.solve(matrix - (alpha * np.eye(len(matrix))), v)
        v /= np.linalg.norm(v)
        eigenvalue = v.T @ (matrix @ v)
        if _ == steps - 1:
            return (eigenvalue, v)


print(InverseIteration(randommatrix, randomvec, 100, examp[0]))

# You might want to start out with Rayleigh Quotient Iteration after a few Power Methods


def RayleighQuotientIteration(matrix, vector, steps):
    v = vector
    eigenvalue = v.T @ (matrix @ v)
    for _ in range(steps):
        try:
            v = np.linalg.solve(matrix - (eigenvalue * np.eye(len(matrix))), v)
            v /= np.linalg.norm(v)
            eigenvalue = v.T @ (matrix @ v)
            if _ == steps - 1:
                return (eigenvalue, v)
        except np.linalg.LinAlgError:
            print(
                f"LinAlgError: Singular matrix encountered at step {_+1}. "
                "Eigenvalue estimate likely converged to a true eigenvalue."
            )
            # Return the last valid eigenvalue and vector before the breakdown
            return (eigenvalue, v)


print(RayleighQuotientIteration(randommatrix, examp[1], 10))
