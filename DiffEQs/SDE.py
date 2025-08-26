import numpy as np
import matplotlib.pyplot as plt
import math


def EulerMaruyama(f, g, input, h, iterations):
    listy = [0] * iterations
    blist = [0] * iterations
    plus = math.sqrt(h)
    for x in range(iterations):
        if x == 0:
            listy[x] = input
        else:
            firstterm = h * f(h * x + input[0], listy[x - 1][1])
            blist[x] = blist[x - 1] + plus * np.random.randn()
            secondterm = (blist[x] - blist[x - 1]) * g(
                h * x + input[0], listy[x - 1][1]
            )
            listy[x] = (h * x + input[0], listy[x - 1][1] + firstterm + secondterm)
    return (listy, blist)


# def funcf(t,y):
#     return (3-y)/(2-t)
# def funcg(t,y):
#     return 1

rate = 0.09
volatility = 0.2


def funcf(t, y):
    return rate * y


def funcg(t, y):
    return volatility * y


solution_points = EulerMaruyama(funcf, funcg, (0, 6270), 0.05, 20)

for x in range(len(solution_points[1])):
    solution_points[1][x] = 6270 * math.exp(
        (rate - (0.5) * (volatility**2)) * solution_points[0][x][0]
        + volatility * solution_points[1][x]
    )


t_values = [point[0] for point in solution_points[0]]
y_values = [point[1] for point in solution_points[0]]

t_values2 = [point[0] for point in solution_points[0]]
y_values2 = [point for point in solution_points[1]]


plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, label="Normal Euler Method", color="blue")
plt.plot(t_values2, y_values2, label="Real Solution", color="red")


plt.title(
    "Solution of Geometric Brownian Motion, 1 year, rate = .09, volatility = .2"
)  # Set the plot title
plt.xlabel("t")  # Label for the x-axis
plt.ylabel("y(t)")  # Label for the y-axis
plt.grid(True)  # Add a grid for better readability

plt.legend()
plt.show()
