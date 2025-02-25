import numpy as np

def fixed_point_iteration(f, x_0, N, tol = 0):
    n = 0
    while np.abs(f(x_0) - x_0) > tol and n < N:
        x_0 = f(x_0)
        n += 1
    return x_0, n