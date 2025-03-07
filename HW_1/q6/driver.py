from bisection import bisect_iterations
from fixed_point import fixed_point_iteration
from newton_method import newton_method
import numpy as np

def f(x):
    return x**2 - 2

def f_prime(x):
    return 2*x

def g(x):
    return (x/2) + (1/x)

def print_res(n):
    print("### {0} ###".format(n))
    val_b = bisect_iterations(f, 0.5, 5, n)
    val_f = fixed_point_iteration(g, 5, n)
    val_n = newton_method(5, f, f_prime, n)
    print("(root) b, f, n: {0}, {1}, {2}".format(val_b, val_f[0], val_n))
    print("(abs_err) b, f, n: {0}, {1}, {2}".format(np.abs(val_b - np.sqrt(2)), np.abs(val_f[0] - np.sqrt(2)), np.abs(val_n - np.sqrt(2))))


#print(fixed_point_iteration(g, 5, 10**12, 10**-3))
#print_res(1)
#print_res(2)
#print_res(3)
#print_res(4)
#print_res(5)
#print_res(6)
#print_res(7)
#print_res(8)
#print_res(9)
#print_res(10)
print(fixed_point_iteration(g, 0.01, 100))