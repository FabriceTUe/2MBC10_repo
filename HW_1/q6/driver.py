from bisection import bisect
from fixed_point import fixed_point_iteration
from newton_method import newton_method

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def g(x):
    return (x/2) + (1/x)

print(fixed_point_iteration(g, 5, 10**12, 10**-3))