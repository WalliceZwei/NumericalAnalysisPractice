import numpy as np
import matplotlib.pyplot as plt


def FirstOrderDeriv(func, x, h):
    return (func(x + h) - func(x)) / h


def SecondOrderDeriv(func, x, h):
    return (func(x + h) - func(x - h)) / (2 * h)


def SecondOrderSecondDeriv(func, x, h):
    return (func(x + h) + func(x - h) - 2 * func(x)) / (h * h)


x_line = np.logspace(0, -6, 200)


def fun1(x):
    return 1 / x


first_line = np.abs(-0.25 - FirstOrderDeriv(fun1, 2, x_line))
second_line = np.abs(-0.25 - SecondOrderDeriv(fun1, 2, x_line))

plt.plot(x_line, first_line, label="First Order Deriv Approx")
plt.plot(x_line, second_line, label="Second Order Deriv Approx")
plt.xlabel("h value")
plt.ylabel("Error Value")
plt.legend()
plt.title("Derivative Approximations")
plt.gca().invert_xaxis()
plt.show()
