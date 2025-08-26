import numpy as np
import matplotlib.pyplot as plt
import math
from DiffEQs.ODE import ExplicitTrapezoid

g = 9.8
l = 1


def pendfunc(t, y):
    const1 = y[1]
    const2 = -1 * (g / l) * math.sin(y[0])
    return np.array([const1, const2])


# Euler's Method is Cheeks with Pendulum Motion, way too inaccurate
# Midpoint Method and Explicit Trapezoid are pretty damn similar

solution_points = ExplicitTrapezoid(pendfunc, (0, np.array([0.1, 0])), 0.05, 100)
solution_points2 = ExplicitTrapezoid(pendfunc, (0, np.array([0, 0.1])), 0.05, 100)
solution_points3 = ExplicitTrapezoid(
    pendfunc, (0, np.array([math.pi / 2, 0])), 0.01, 500
)
solution_points4 = ExplicitTrapezoid(pendfunc, (0, np.array([3, 0])), 0.01, 500)

t_values = [point[0] for point in solution_points]
y_values = [point[1][0] for point in solution_points]

t_values2 = [point[0] for point in solution_points2]
y_values2 = [point[1][0] for point in solution_points2]

t_values3 = [point[0] for point in solution_points3]
y_values3 = [point[1][0] for point in solution_points3]

t_values4 = [point[0] for point in solution_points4]
y_values4 = [point[1][0] for point in solution_points4]

plt.figure(figsize=(10, 6))

plt.scatter(t_values, y_values, label=".1 radians, 0 velo", color="red", marker="o")
plt.scatter(t_values2, y_values2, label="0 radians, .1 velo", color="black", marker="x")
plt.scatter(
    t_values3, y_values3, label="pi/2 radians, 0 velo", color="blue", marker="+"
)
plt.scatter(t_values4, y_values4, label="3 radians, 0 velo", color="purple", marker="1")

plt.grid(True)
plt.title("Pendulum Motion")
plt.xlabel("Time")
plt.ylabel("Y-Position of the End of Pendulum")
plt.legend()
plt.show()
