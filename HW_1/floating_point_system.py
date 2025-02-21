import numpy as np
from decimal import Decimal

class FloatingPointSystem():
    def __init__(self, beta, p, L, U):
        self.beta = beta
        self.p = p
        self.L = L
        self.U = U

    def __get_exponent(self, x):
        i = self.L
        while self.beta**i < abs(x):
            i = i + 1
        return i

    def __number_to_base(self, x):
        if x == 0:
            return [0]
        digits = []
        while x:
            digits.append(int(x % self.beta))
            x //= self.beta
        return digits[::-1]

    def __dec_number_to_digits(self, x):
        v = format(x, "e")
        if '+' in v:
            power = v.split('+')[1]
            power = int(power)
        else:
            power = v.split('-')[1]
            power = int(power) -1
        x = float(v.split('e')[0])
        x = int(x * (10**power))
        return x

    def __get_mantissa(self, x):
        x = self.__dec_number_to_digits(x)
        print(x)

        str_rep = self.__number_to_base(x)
        print(str_rep)

        digits = []
        for i in range(min(self.p, len(str_rep))):
            d = str_rep[i]
            digits.append(int(d))
        for i in range(len(str_rep), self.p):
            digits.append(int(0))
        return np.array(digits)

    def fl_ch(self, x):
        mantissa = self.__get_mantissa(x)
        E = self.__get_exponent(x)
