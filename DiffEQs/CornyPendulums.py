import numpy as np
import matplotlib.pyplot as plt
import math
from DiffEQs.ODE import ExplicitTrapezoid

g=9.8
l=1
d = 1
A = 10

def dampedpendfunc(t,y): 
    const1 = y[1]
    const2 = -1* (g / l) * math.sin(y[0]) -1*d*y[1]
    return np.array([const1,const2])

def forceddampedpendfunc(t,y): 
    const1 = y[1]
    const2 = -1* (g / l) * math.sin(y[0]) -1*d*y[1] + A*math.sin(t)
    return np.array([const1,const2])


solution_points = ExplicitTrapezoid(dampedpendfunc, (0,np.array([math.pi/3,0])), .05, 100) 
solution_points2 = ExplicitTrapezoid(forceddampedpendfunc, (0,np.array([math.pi/3,.1])), .05, 100) 

t_values = [point[0] for point in solution_points]
y_values = [point[1][0] for point in solution_points]

t_values2 = [point[0] for point in solution_points2]
y_values2 = [point[1][0] for point in solution_points2]


plt.figure(figsize=(10, 6))

plt.scatter(t_values, y_values, label='60 degrees, 0 velo, damped, d = 1', color='red', marker='o')
plt.scatter(t_values2, y_values2, label='60 degrees, 0 velo, forceddamped, d = 1, A = 10', color='black', marker='x')

plt.grid(True)
plt.title('Pendulum Motion')
plt.xlabel('Time')
plt.ylabel('Y-Position of the End of Pendulum')
plt.legend() 
plt.show() 
