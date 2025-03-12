import numpy as np

class Integrator:
    @staticmethod
    def simpson(f, x_0, x_1):
        x_m = (x_0 + x_1) / 2
        factor_1 = (x_1 - x_0) / 6
        factor_2 = f(x_0) + 4 * f(x_m) + f(x_1)
        return factor_1 * factor_2

    @staticmethod
    def integrate_composite(f, x_0, x_1, quadrature_rule, granularity, open = False):
        if not open:
            points = np.linspace(x_0, x_1, granularity + 1)
        else:
            raise NotImplementedError()
        I = 0
        for i in range(points.shape[0] - 1):
            I += quadrature_rule(f, points[i], points[i + 1])
        return I