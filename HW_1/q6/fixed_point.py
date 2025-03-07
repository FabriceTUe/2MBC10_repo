import numpy as np

def fixed_point_iteration(f, x_0, N):
    n = 0
    while n < N:
        x_0 = f(x_0)
        n += 1
    return x_0, n