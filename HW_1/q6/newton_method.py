def newton_method(x_0, f, f_prime, n):
    for i in range(n):
        x_0 = x_0 - (f(x_0)/f_prime(x_0))
    return x_0
