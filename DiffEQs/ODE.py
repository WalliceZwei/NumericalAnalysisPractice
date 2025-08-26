import numpy as np
import matplotlib.pyplot as plt
import math

# Base Euler's Method


def Euler(fun, input, h, iterations):
    listy = [0] * iterations
    for x in range(iterations):
        if x == 0:
            listy[x] = input
        else:
            listy[x] = (
                h * x + input[0],
                listy[x - 1][1] + h * fun(h * x + input[0], listy[x - 1][1]),
            )
    return listy


def ExplicitTrapezoid(fun, input, h, iterations):
    listy = [0] * iterations
    for x in range(iterations):
        if x == 0:
            listy[x] = input
        else:
            put = h * x + input[0]
            output = fun(put, listy[x - 1][1])
            output2 = fun(put + h, listy[x - 1][1] + (h * output))
            listy[x] = (put, listy[x - 1][1] + (h / 2) * (output + output2))
    return listy


def Midpoint(fun, input, h, iterations):
    listy = [0] * iterations
    for x in range(iterations):
        if x == 0:
            listy[x] = input
        else:
            newx = h * x + input[0]
            output = fun(newx, listy[x - 1][1])
            output2 = fun(newx + h / 2, listy[x - 1][1] + ((h / 2) * output))
            listy[x] = (newx, listy[x - 1][1] + h * output2)
    return listy


def RK4(fun, input, h, iterations):
    listy = [0] * iterations
    for x in range(iterations):
        if x == 0:
            listy[x] = input
        else:
            newx = h * x + input[0]
            s1 = fun(newx, listy[x - 1][1])
            s2 = fun(newx + h / 2, listy[x - 1][1] + ((h / 2) * s1))
            s3 = fun(newx + h / 2, listy[x - 1][1] + ((h / 2) * s2))
            s4 = fun(newx + h, listy[x - 1][1] + (h * s3))
            listy[x] = (newx, listy[x - 1][1] + (h / 6) * (s1 + 2 * s2 + 2 * s3 + s4))
    return listy


x_line = np.linspace(0, 2.5, 700)
y_line = 3 * np.exp((x_line**2) / 2) - (x_line**2) - 2


def func(t, y):
    return t * y + t**3


solution_points = Euler(func, (0, 1), 0.01, 250)
solution_points2 = ExplicitTrapezoid(func, (0, 1), 0.01, 250)
solution_points3 = Midpoint(func, (0, 1), 0.01, 250)
solution_points4 = RK4(func, (0, 1), 0.01, 250)

# --- Extract t and y values for plotting ---
# Use list comprehensions for a clean way to separate the tuples
t_values = [point[0] for point in solution_points]
y_values = [point[1] for point in solution_points]

t_values2 = [point[0] for point in solution_points2]
y_values2 = [point[1] for point in solution_points2]

t_values3 = [point[0] for point in solution_points3]
y_values3 = [point[1] for point in solution_points3]

t_values4 = [point[0] for point in solution_points4]
y_values4 = [point[1] for point in solution_points4]

# --- Plotting ---
plt.figure(figsize=(10, 6))  # Create a figure and set its size
plt.plot(x_line, y_line, label="Euler's Method Solution")  # Plot the data
plt.scatter(t_values2, y_values2, label="Trapezoid Solution", color="red", marker="o")
plt.scatter(t_values, y_values, label="Normal Euler Method", color="blue", marker="o")
plt.scatter(t_values3, y_values3, label="Midpoint", color="black", marker="x")
plt.scatter(t_values3, y_values3, label="RK4", color="yellow", marker="1")

plt.title("Solution of dy/dt = ty + t^3 using Euler's Method")  # Set the plot title
plt.xlabel("t")  # Label for the x-axis
plt.ylabel("y(t)")  # Label for the y-axis
plt.grid(True)  # Add a grid for better readability


plt.legend()
plt.show()
