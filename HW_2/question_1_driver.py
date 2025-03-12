from lagrange_interpolation import LagrangeInterpolant
import matplotlib.pyplot as plt
import numpy as np

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


# actually execute the code:
generate_plots(False)
generate_plots(True)