from integration import Integrator
import numpy as np

# 3.1:
sigma = 5 # as an example. The result is independent of sigma.
def f(x):
    factor_1 = 1 / (sigma * np.sqrt(2 * np.pi))
    factor_2 = np.exp((-1/2) * ((x / sigma)**2))
    return factor_1 * factor_2

#a
print(Integrator.integrate_composite(f, -sigma, sigma, Integrator.right_rectangle_rule, 10**7))
#b
print(Integrator.integrate_composite(f, -2 * sigma, 2 * sigma, Integrator.right_rectangle_rule, 10**7))
#c
print(Integrator.integrate_composite(f, -3 * sigma, 3 * sigma, Integrator.right_rectangle_rule, 10**7))

# 3.2:
def g(x):
    y = 9 * (np.sin(x))**2 + 4 * (np.cos(x))**2
    return np.sqrt(y)

print(Integrator.integrate_composite(g, 0, 2 * np.pi, Integrator.right_rectangle_rule, 10**8))