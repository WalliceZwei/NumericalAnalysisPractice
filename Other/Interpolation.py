import numpy as np
import matplotlib.pyplot as plt
import math

# Newton's, approximate sine

numpartitions = 6

xlist = [math.pi * x / ((numpartitions - 1) * 2) for x in range(numpartitions)]

ylist = [
    math.sin(math.pi * x / ((numpartitions - 1) * 2)) for x in range(numpartitions)
]


def NewtonInterpolation(samplenum, xpoints, ypoints):
    newtoncoefficientmatrix = [[0] * samplenum for _ in range(samplenum)]

    for h in range(samplenum):
        newtoncoefficientmatrix[0][h] = ypoints[h]

    for x in range(1, samplenum):
        for y in range(samplenum - x):
            newtoncoefficientmatrix[x][y] = (
                newtoncoefficientmatrix[x - 1][y + 1]
                - newtoncoefficientmatrix[x - 1][y]
            ) / (xpoints[x + y] - xpoints[y])

    newarr = [0] * samplenum
    for x in range(samplenum):
        newarr[x] = newtoncoefficientmatrix[x][0]

    def PolynomialMaker(x):
        val = 0

        for u in range(samplenum - 2, -1, -1):
            val += newarr[u + 1]
            val *= x - xpoints[u]
        val += newarr[0]

        return val

    return PolynomialMaker


parts = 500

# X = np.linspace(0, math.pi, parts)
# Y = np.sin(X)
X = np.linspace(-1, 1, parts)
Y = 1 / (1 + (12 * (X * X)))

basex = [-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0]

basey = [1 / (1 + (12 * x * x)) for x in basex]

funcsy = NewtonInterpolation(
    9, [-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0], basey
)

# funcsy = NewtonInterpolation(4, [0,math.pi/6,math.pi/3,math.pi/2], [0,.5,math.sin(math.pi/3), 1])


plt.plot(X, Y)

funclist = [funcsy(x) for x in X]

plt.plot(X, funclist)

plt.show()
