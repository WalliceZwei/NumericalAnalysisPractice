import numpy as np
import matplotlib.pyplot as plt
import math
from DiffEQs.ODE import ExplicitTrapezoid
from scipy.optimize import root_scalar
from Other.RootSolversCh1 import NewtonsMethod, BisectionMethod
# First, rewrite the second order into a system of first orders

def func(t,y): 
    const1 = y[1]
    const2 = 4*y[0]
    return np.array([const1,const2])

x_line = np.linspace(0,1,500)
cons1 = (3-math.exp(-2)) / (math.exp(2)-math.exp(-2))
cons2 = (math.exp(2)-3) / (math.exp(2)-math.exp(-2))
y_line = cons1*np.exp(2*x_line) + cons2*np.exp(-2*x_line)

# Implement the root solvers later

# note that input is (scalar, np.array([ya, sa])) where sa is the guess for the slope

def ShootingMethod(fun,starttime, ya, endtime, yb,h):
    timeelapsed = endtime - starttime
    def partial(slopeinput):
        return ExplicitTrapezoid(fun, (starttime, np.array([ya, slopeinput])), h, math.ceil(timeelapsed/h)+1)[-1][1][0] - yb

    conditions = NewtonsMethod(partial,1,.00001)
    print(conditions)
    return ExplicitTrapezoid(fun, (starttime, np.array([ya, conditions])), h, math.ceil(timeelapsed/h)+1)
    
solution_points = ShootingMethod(func,0,1,1,3,.05)

t_values = [point[0] for point in solution_points]
y_values = [point[1][0] for point in solution_points]

plt.figure(figsize=(10, 6))

plt.scatter(t_values, y_values, label='ShootingMethod', color='red', marker='o')
plt.plot(x_line, y_line, color = "green", label = "Actual Solution")

plt.grid(True)
plt.title('BVP')
plt.xlabel('Time')
plt.ylabel('Y')
plt.legend() 
plt.show() 
