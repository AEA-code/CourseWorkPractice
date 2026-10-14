def bisection(f,a,b,tol=1e-3, max_iter =100):
    # check if a and b have opposite signs
    if f(a)*f(b) > 0:# if not print a message
        print(f'No root or more than one root in {a},{b}')
        return None
    #find the midpoint
    for _ in range(max_iter):
        m = (a+b)/2
        fm = f(m)

        if abs(fm) < tol or (b - a) / 2 < tol:
            return m
        if f(a) * fm < 0:
            b = m
        else:
            a = m
    return (a + b)/2
def f(x):
    return x**2 - 2

root = bisection(f, 0, 4)
print(root)