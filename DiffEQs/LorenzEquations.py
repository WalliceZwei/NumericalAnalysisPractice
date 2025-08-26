import numpy as np
import matplotlib.pyplot as plt
import math
from DiffEQs.ODE import ExplicitTrapezoid
from DiffEQs.ODE import RK4

s = 10
r = 28
b = 8 / 3


def lorenzfunc(t, v):
    x, y, z = v
    const1 = -1 * s * x + s * y
    const2 = -1 * x * z + r * x - y
    const3 = x * y - b * z
    return np.array([const1, const2, const3])


solution_points = ExplicitTrapezoid(lorenzfunc, (0, np.array([4, 4, 5])), 0.001, 50000)
solution_points2 = RK4(lorenzfunc, (0, np.array([4, 4, 5])), 0.001, 50000)


t_values = [point[1][0] for point in solution_points]
y_values = [point[1][2] for point in solution_points]

t_values2 = [point[1][0] for point in solution_points2]
y_values2 = [point[1][2] for point in solution_points2]

plt.figure(figsize=(10, 6))

plt.plot(t_values, y_values, label="Trapezoid Lorenz", color="red")
plt.plot(t_values2, y_values2, label="RK4 Lorenz", color="black")


plt.grid(True)
plt.title("Butterfly Effect")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.show()
