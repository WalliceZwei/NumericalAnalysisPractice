import numpy as np

initvec = np.array([1,2])

# def euclideandist(nparr):
#     return nparr[0]**2 + nparr[1]**2

def MultiNewton(functionarr, vector, tolerance):

    jacobarr = np.zeros((len(functionarr),len(functionarr)))
    derivconst = .0001
    oldvectorpoint = np.array([functionarr[i](vector) for i in range(len(functionarr))])
    
    while np.linalg.norm(oldvectorpoint) > tolerance:
        input = np.copy(vector)
        for x in range(len(functionarr)):
            const = functionarr[x](input)
            for y in range(len(functionarr)):
                input_perturbed = np.copy(input)
                input_perturbed[y] += derivconst
                jacobarr[y,x]=(functionarr[x](input_perturbed) - const) / derivconst
        oldvectorpoint = np.array([functionarr[i](vector) for i in range(len(functionarr))])
        vector -=  np.linalg.inv(jacobarr) @ oldvectorpoint
        
    return vector
       
def function1(nparr):
    return nparr[1]-(nparr[0]**3)
def function2(nparr):
    return nparr[0]**2 + nparr[1]**2 - 1

print(MultiNewton([function1, function2], np.array([1.,2.]), .001))
        
