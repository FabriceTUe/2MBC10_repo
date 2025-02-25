import numpy as np

def f(i):
    return (1500/i) * ((1 + i)**240 - 1) - 750000

def bisect(g, a, b, tol):
    while ((b-a) > tol):
        m = a + (b-a)/2
        if np.sign(g(a)) == np.sign(g(m)):
            a = m
        else:
            b = m
    return m

#ans = bisect(f, 0.0005, 0.05, 10**-16)
#print(ans)
#print(f(ans))
#print(f(0.0055507819))