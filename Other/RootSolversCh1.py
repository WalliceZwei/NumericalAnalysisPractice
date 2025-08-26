
def BisectionMethod(fun,lower,upper,limit): 
    mid = (lower+upper)/2 
    val = fun(mid)
    while abs(val)>limit:
        if val>0:
            upper = mid
        else:
            lower = mid
        mid = (lower+upper)/2 
        val = fun(mid)
    return mid 

# I mean techncially it's just secant method, but it's impossible to take the derivatives of some functions
def NewtonsMethod(fun, input, limit):
    h = .00001
    val = fun(input)
    while abs(val) > limit: 
        deriv = (fun(input+h) - val) / h
        input -= (val/deriv)
        val = fun(input)
    return input

# A "real" Newton's Method would 