import numpy as np
import matplotlib.pyplot as plt

# define f:
def f(x):
    return np.sin(x)

def get_data_for_n(n, epsilon):
    h = 10**(n)
    if 1 + h > np.pi/2:
        M = f(1 + h)
    else:
        M = 1
    truncation_err = (M * h) / 2
    round_off_err = (2 * epsilon) / h
    approximation = (f(1 + h) - f(1)) / h
    tot_err = np.abs(approximation - np.cos(1))
    return truncation_err, round_off_err, tot_err

def plot(min_n, max_n, epsilon):
    n_values = []
    truncation_errs = []
    round_off_errs = []
    tot_errs = []
    n_values = np.linspace(min_n, max_n, 400)
    for n in n_values:
        trun, round_off, tot = get_data_for_n(n, epsilon)
        truncation_errs.append(trun)
        round_off_errs.append(round_off)
        tot_errs.append(tot)
    plt.plot(n_values, truncation_errs, label="Truncation error")
    plt.plot(n_values, round_off_errs, label="Roundoff error")
    plt.plot(n_values, tot_errs, label="Total error")
    plt.yscale('log')
    plt.legend()
    plt.xlabel("n")
    plt.ylabel("error")

    plt.savefig("diff_plot.png")

plot(-15, 0, 10**-16)