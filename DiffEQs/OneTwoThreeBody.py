import numpy as np
import matplotlib.pyplot as plt
import math
from DiffEQs.ODE import ExplicitTrapezoid

G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24  # Earth's mass (kg)


def onebodyfunc(t, y):
    const0 = (-1 * G * M) / ((y[2] ** 2 + y[0] ** 2) ** 1.5)
    const1 = y[1]
    const2 = const0 * y[0]
    const3 = y[3]
    const4 = const0 * y[2]
    return np.array([const1, const2, const3, const4])


R = 7e6  # Orbital radius (m), slightly above Earth's radius
v_circular = np.sqrt(G * M / R)  # Circular orbit velocity (~7.8 km/s)
y0 = np.array([R, 0, 0, v_circular])

solution_points = ExplicitTrapezoid(onebodyfunc, (0, y0), 1, 10000)

x_values = [point[1][0] for point in solution_points]
y_values = [point[1][2] for point in solution_points]

plt.figure(figsize=(10, 6))

plt.scatter(x_values, y_values, label="", color="red", marker="o")

plt.grid(True)
plt.title("One Body Motion")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Do Two and Three Body Later???
