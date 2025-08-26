import numpy as np
import matplotlib.pyplot as plt
import math 


def CompositeTrapezoidal(fun, start, end, num):
    answer = 0
    height = (end-start)/num
    for x in range(num+1):
        if x == 0 or x == num: 
            answer += ((fun(start+(x*height))))
        else:
            answer += (2*((fun(start+(x*height)))))
    answer *= (height/2)
    # (height*(fun(start+(x*height)) + fun(start+((x+1)*height)))/2) is explicit
    return answer

def CompositeMidpoint(fun, start, end, num):
    answer = 0
    height = (end-start)/num
    for x in range(num):
        answer += (fun(start+((x+1/2)*height)))
    answer *= (height)
    return answer

def CompositeSimpsonsRule(fun, start, end, num):
    answer = 0
    height = (end-start)/num
    for x in range(num):
        answer+= ((fun(start+(x*height)) + 4* fun(start+((x+1/2)*height)) + fun(start+((x+1)*height))) * (height/6))
    return answer

def CompositeThreeEighthsSimpsonsRule(fun, start, end, num):
    answer = 0
    height = (end-start)/num
    for x in range(num):
        answer+= ((fun(start+(x*height)) + 3* fun(start+((x+1/3)*height))+ 3* fun(start+((x+2/3)*height)) + fun(start+((x+1)*height))) * (height/8))
    return answer

# Obviously you can convert this into a more optimized form later

def func(x):
    return x**2

print(CompositeMidpoint(func, 0, 1, 100))
print(CompositeTrapezoidal(func, 0, 1, 100))
print(CompositeSimpsonsRule(func, 0, 1, 100))
print(CompositeThreeEighthsSimpsonsRule(func, 0, 1, 100))
    
    