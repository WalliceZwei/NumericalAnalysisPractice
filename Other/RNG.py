import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import qmc


# returns a list of random numbers of length [number]
def LCG(m, a, b, randseed, number):
    listy = [0] * number
    for x in range(number):
        if x == 0:
            xi = (a * randseed + b) % m
        else:
            xi = (a * listy[x - 1] + b) % m
        listy[x] = xi
    return [x / m for x in listy]


# Small Example

print(LCG(31, 13, 0, 3, 10))

# Minimum Standard RNG


def MSRNG(randseed, number):
    return LCG(2**31 - 1, 7**5, 0, randseed, number)


# RandU


def RandU(randseed, number):
    return LCG(2**31, 2**16 + 3, 0, randseed, number)


a = 0.5

randomnums = MSRNG(58, 2000)

transformed = [-1 * math.log(1 - x) / a for x in randomnums]

print(transformed)

data = pd.Series(transformed)

# a = .5
x = np.linspace(0, 10, 1000)
y = a * np.exp(-a * x)

fig, ax = plt.subplots(figsize=(8, 6))

sns.histplot(data, kde=False, stat="density", ax=ax, bins=100)
sns.lineplot(x=x, y=y, ax=ax, color="red")
plt.legend()
plt.show()
# Monte Carlo Problems

# Area Problem

sampler = qmc.Sobol(d=2, scramble=True)

# Generate 10,000 quasi-random numbers
quasi_random = sampler.random(n=200000)


# 4*(2*x - 1)**4 + 8*(2*y-1)**8 < 1+2*(2*y-1)**3 * (3*x-2)**2
def ineq(x, y):
    return y < x**2


testpoints = MSRNG(2309888787, 200000)
testpoints2 = MSRNG(7181, 200000)

totalnum = 0
for x in range(len(testpoints)):
    if ineq(testpoints[x], testpoints2[x]):
        totalnum += 1

print(totalnum / 200000)

totals = 0
for x in range(len(testpoints)):
    if ineq(quasi_random[x][0], quasi_random[x][1]):
        totals += 1

print(totals / 200000)


# Monte Carlo (Exiting Strategy)

simulationnum = 1000
topexit = 0

# Brownian Motion Graph

timesteps = 1 / 100000

plus = math.sqrt(timesteps)

constant = int(1 / timesteps)
time = [int(x) * timesteps for x in range(constant)]

brownlist = [0] * constant


def BrownianDrift(blist, driftconst):
    for x in range(constant):
        if x == 0:
            if np.random.random() > 0.5:
                blist[x] = plus
            else:
                blist[x] = -1 * plus
        else:
            if np.random.random() > 0.5:
                blist[x] = plus + blist[x - 1]
            else:
                blist[x] = -1 * plus + blist[x - 1]

        blist[x] += timesteps * driftconst
    return blist


# brownlist = BrownianDrift(brownlist, 0)


def TrueBrownian():
    blist = [0] * constant
    for x in range(1, constant):
        blist[x] = blist[x - 1] + plus * np.random.randn()
    return blist


brownlist = TrueBrownian()

df = pd.Series(brownlist, index=time)

plt.figure(figsize=(10, 6))
plt.plot(df.index, df, label="Brownian Motion", color="black")
plt.title("Standard Brownian Motion")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
