from lagrange_interpolation import LagrangeInterpolant
import matplotlib.pyplot as plt
import numpy as np
import math

def get_uniform_nodes(n: int):
    # get x and y from function:
    x_list = []
    y_list = []
    for i in range(n + 1):
        x_list.append((2*i)/n - 1)
        y_list.append(1/(1 + 25 * (x_list[i]**2)))
    return x_list, y_list

def get_chebyshev_nodes(n: int):
    x_list = []
    y_list = []
    for i in range(n + 1):
        x = (-1 + 1)/2 + ((1 - (-1))/2) * np.cos((2 * i + 1)/(2 * (n + 1)) * np.pi)
        x_list.append(x)
        y_list.append(1/(1 + 25 * (x_list[i]**2)))
    return x_list, y_list

def add_interpolant_to_plot(n: int, x_list: list, y_list: list):
    lagrange_interpolant = LagrangeInterpolant(x_list, y_list)
    x_axis = np.linspace(x_list[0], x_list[-1], 400)
    interpolant_values = []
    for x in np.nditer(x_axis):
        interpolant_values.append(lagrange_interpolant.evaluate(x))
    plt.plot(x_axis, interpolant_values, label="Interpolant for n = {0}".format(n))

def add_function_to_plot():
    x_axis = np.linspace(-1, 1, 400)
    y_list = []
    for x in np.nditer(x_axis):
        y_list.append(1/(1 + 25 * (x**2)))
    plt.plot(x_axis, y_list, label="True function f")
    
def generate_plots(chebyshev: bool):
    for n in [6, 10 , 14]:
        if chebyshev:
            x_list, y_list = get_chebyshev_nodes(n)
        else:
            x_list, y_list = get_uniform_nodes(n)
        add_interpolant_to_plot(n, x_list, y_list)
    add_function_to_plot()
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    phrase = "Chebyshev" if chebyshev else "uniform"
    plt.title("Lagrange interpolant for various n, in case of {0} nodes".format(phrase))
    plt.savefig("{0}_plot_for_q1.png".format(phrase))
    plt.figure()

def get_nodes_factor_for_x(x, nodes):
    factor = 1
    for i in range(len(nodes)):
        factor *= (x - nodes[i])
    return np.abs(factor)

def plot_nodes_factor(chebyshev):
    for n in [6, 10, 14]:
        if chebyshev:
            x_list, _ = get_chebyshev_nodes(n)
        else:
            x_list, _ = get_uniform_nodes(n)
        x_axis = np.linspace(x_list[0], x_list[-1], 400)
        factor_values = []
        for x in np.nditer(x_axis):
            factor_values.append(get_nodes_factor_for_x(x, x_list))
        plt.plot(x_axis, factor_values, label="Factor for n = {0}".format(n))
    plt.show()
    
def get_max_error_direct(n, chebyshev):
    if chebyshev:
        x_list, y_list = get_chebyshev_nodes(n)
    else:
        x_list, y_list = get_uniform_nodes(n)
    lagrange_interpolant = LagrangeInterpolant(x_list, y_list)
    x_vals_to_test = np.linspace(x_list[0], x_list[-1], 10**6)
    max = 0
    for x in np.nditer(x_vals_to_test):
        f_val = 1 / (1 + 25 * x**2)
        error = np.abs(lagrange_interpolant.evaluate(x) - f_val)
        if error > max:
            max = error
    return max
    


# generate plots:
#generate_plots(False)
#generate_plots(True)

# get uniform max error for various n:
print("uniform:")
print(get_max_error_direct(6, False))
print(get_max_error_direct(10, False))
print(get_max_error_direct(14, False))

print("chebyshev:")
print(get_max_error_direct(6, True))
print(get_max_error_direct(10, True))
print(get_max_error_direct(14, True))