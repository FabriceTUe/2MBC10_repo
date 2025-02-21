import numpy as np
import matplotlib.pyplot as plt
from floating_point_system import FloatingPointSystem

class Plotter:
    def __init__():
        super()

    @staticmethod
    def get_rel_error(x_hat, x):
        return np.divide(np.abs(x_hat - x), np.abs(x))
    
    @staticmethod
    def get_abs_error(x_hat, x):
        return np.abs(x_hat - x)

    @staticmethod
    def plot(fl_sys: FloatingPointSystem, range: np.ndarray):
        # Plot 1:
        N = 400
        x_axis = np.linspace(range[0], range[1], 400)
        vec_fl_ch = np.vectorize(fl_sys.fl_ch)
        vec_fl_rn = np.vectorize(fl_sys.fl_rn)
        fl_ch = vec_fl_ch(x_axis)
        fl_rn = vec_fl_rn(x_axis)
        plt.figure(figsize=(10,5))
        plt.plot(x_axis, fl_ch, color='b', linestyle='dotted')
        plt.plot(x_axis, fl_rn, color='r')
        plt.xlabel("x")
        plt.ylabel("Floating-point approximation of x")
        plt.title("Requested graph for F({0}, {1}, {2}, {3})".format(fl_sys.beta, fl_sys.p, fl_sys.L, fl_sys.U))
        plt.legend(["Chopping", "Rounding to nearest"], loc="upper left")
        plt.show()

        rel_error_ch = Plotter.get_rel_error(fl_ch, x_axis)
        abs_error_ch = Plotter.get_abs_error(fl_ch, x_axis)
        rel_error_rn = Plotter.get_rel_error(fl_rn, x_axis)
        abs_error_rn = Plotter.get_abs_error(fl_rn, x_axis)

Plotter.plot(FloatingPointSystem(2, 2, -1, 1), [-1, 1])