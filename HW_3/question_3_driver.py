from ode_solver import ODESolver
import matplotlib.pyplot as plt

# part a:
def derivative_function(t_n, y_n):
    return (5 * 10**-6) * (10**5 - y_n) * y_n

for delta_t in [1, 2, 4]:
    t_values, w_values = ODESolver.solve_initial_value_problem(derivative_function, delta_t, ODESolver.forward_euler, (0, 1000), round(100 / delta_t))
    plt.plot(t_values, w_values, label='$\Delta$ t = {0}'.format(delta_t))
plt.axhline(y=10**5, color = 'r', linestyle="--")

plt.legend()
plt.ylabel("Number of infectives")
plt.xlabel("Time (days)")
plt.show()
plt.savefig("infectives_vs_time.png")
plt.clf()

# part b:
def derivative_function_prime(t_n, y_n):
    return 5 * 10**-6 * 10**5 - 2 * 5 * 10**-6 * y_n

for delta_t in [1, 2, 4]:
    t_values, w_values = ODESolver.solve_initial_value_problem(derivative_function, delta_t, ODESolver.backward_euler, (0, 1000), round(100 / delta_t), derivative_function_prime)
    plt.plot(t_values, w_values, label='$\Delta$ t = {0}'.format(delta_t))
plt.axhline(y=10**5, color = 'r', linestyle="--")

plt.legend()
plt.ylabel("Number of infectives")
plt.xlabel("Time (days)")
plt.show()
plt.savefig("infectives_vs_time_backward.png")