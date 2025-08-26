import numpy as np
import matplotlib.pyplot as plt
from DiffEQs.ODE import Euler
from DiffEQs.ODE import ExplicitTrapezoid
from DiffEQs.ODE import Midpoint, RK4


# Make sure to make the multi-ode function correct
def func(t, y):
    const1 = y[1] ** 2 - 2 * y[0]
    const2 = y[0] - y[1] - 1 * (t * y[1] * y[1])
    return np.array([const1, const2])


m = 1
dampcoeff = 2
springconst = 10


def mechvibfunc(t, y):
    const1 = y[1]
    const2 = -1 * (dampcoeff * y[1] + springconst * y[0]) / m
    return np.array([const1, const2])


solution_points = Midpoint(mechvibfunc, (0, np.array([1, 1])), 0.1, 25)
solution_points2 = RK4(mechvibfunc, (0, np.array([1, 1])), 0.1, 25)
solution_points3 = Euler(mechvibfunc, (0, np.array([1, 1])), 0.05, 50)

t_values = [point[0] for point in solution_points]
y_values = [point[1][0] for point in solution_points]

t_values2 = [point[0] for point in solution_points2]
y_values2 = [point[1][0] for point in solution_points2]

t_values3 = [point[0] for point in solution_points3]
y_values3 = [point[1][0] for point in solution_points3]

plt.figure(figsize=(10, 6))

# x_line = np.linspace(0,2.5,700)
# y_line = x_line * np.exp(-2*x_line)

x_line = np.linspace(0, 2.5, 700)
y_line = (np.cos(3 * x_line) + (2 / 3) * np.sin(3 * x_line)) * (np.exp(-1 * x_line))


plt.plot(x_line, y_line, label="Free Damped Spring Solution")
plt.scatter(t_values, y_values, label="Multi-Euler Approx", color="red", marker="o")
plt.scatter(
    t_values2, y_values2, label="Multi-Trapezoid Approx", color="black", marker="x"
)
plt.scatter(
    t_values3, y_values3, label="Multi-Midpoint Approx", color="blue", marker="+"
)
plt.grid(True)  # Add a grid for better readability

plt.legend()
plt.show()
