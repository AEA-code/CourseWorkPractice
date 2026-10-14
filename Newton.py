from math import exp
def Newton(f,dfdx,x0,max_it,tol=1e-3):
    f0=f(x0)
    iter = 0
    while abs(f0) > tol and iter < max_it:
        x1 = x0 -f0/dfdx(x0)
        x0 = x1
        f0 = f(x0)
        iter +=1

    converge = iter < max_it
    return x0,converge, iter
f = lambda x: x**2-4*x-exp(-x) 
dfdx = lambda x: 2*x-4-exp(-x)

root, converge, iter = Newton(f,dfdx,0,20)

if converge:
    print('Newton method converge')
    print('Root:', root)
    print('Iteration:', iter)
else:
    print('Newton method does not converge')