class LagrangeInterpolant:
    def __init__(self, x_list: list, y_list: list):
        if len(x_list) < 2 or len(y_list) < 2:
            raise ValueError("Provide at least two points to fit")
        if len(x_list) != len(set(x_list)):
            raise ValueError("Please ensure that all x-coordinates are distinct.")

        self.x_list = x_list
        self.y_list = y_list
        self.degree = len(x_list) - 1

    def __L(self, x: float, i: int):
        if i > len(self.x_list) - 1:
            raise ValueError("Provide valid index.")
        
        numerator = 1
        for j in range(self.degree + 1):
            if j != i:
                numerator *= (x - self.x_list[j])
        
        denominator = 1
        for j in range(self.degree + 1):
            if j != i:
                denominator *= (self.x_list[i] - self.x_list[j])
        
        return (numerator/denominator)

    def evaluate(self, x: float):
        res = 0
        for i in range(self.degree + 1):
            res += self.__L(x, i) * self.y_list[i]
        return res
