import numpy as np

class ODESolver():
    @staticmethod
    def newtons_method(f, f_prime, x_k, tol):
        while np.abs(f(x_k)) > tol:
            x_k = x_k - f(x_k) / f_prime(x_k)
        return x_k

    @staticmethod
    def bisection_method(f, a, b, tol):
        while b-a > tol or np.abs(f(m)) > 0:
            m = a + (b-a)/2
            if np.sign(f(a)) == np.sign(f(m)):
                a = m
            else:
                b = m
        print(f(m))
        return m


    @staticmethod
    def forward_euler(derivative_function, delta_t, t_n, w_n, derivative_function_prime):
        return w_n + delta_t * derivative_function(t_n, w_n)

    def backward_euler(derivative_function, delta_t, t_n, w_n, derivative_function_prime):
        if delta_t < 3:
            f = lambda x: -x + w_n + delta_t * derivative_function(t_n + delta_t, x)
            f_prime = lambda x: -1 + delta_t * derivative_function_prime(t_n + delta_t, x)
            print(w_n)
            return ODESolver.newtons_method(f, f_prime, w_n, 10-8)
        else:
            k = 5 * 10-6
            m = 105
            a = delta_t * k
            b = -1
            c = -(w_n + delta_t * k * m)
            numerator = -b + np.sqrt(b2 - 4 * a * c)
            denominator = 2 * a
            return numerator/denominator


    @staticmethod
    def solve_initial_value_problem(derivative_function, delta_t, time_integration_method, initial_value, n_steps, derivative_function_prime = None):
        w_values = []
        t_values = []
        w_values.append(initial_value[1])
        t_values.append(initial_value[0])

        t_i = initial_value[0]
        w_i = initial_value[1]
        for i in range(n_steps):
            t_i += delta_t
            w_i = time_integration_method(derivative_function, delta_t, t_i, w_i, derivative_function_prime)
            w_values.append(w_i)
            t_values.append(t_i)

        return t_values, w_values