import numpy as np

class FloatingPointSystem():
    def __init__(self, beta, p, L, U):
        self.beta = beta
        self.p = p
        self.L = L
        self.U = U

    def __get_exponent(self, x):
        i = self.L
        while self.beta**i < abs(x) and i < self.U:
            i = i + 1
        return i
    
    def __compute_fl(self, m, e):
        fl = 0
        for i in range(self.p):
            fl += m[i] * self.beta**(e - i)
        return fl

    def __get_mantissa_ch(self, x, e):
        M = np.zeros(self.p, dtype=int)
        i = 0
        x = abs(x)

        while x > 0 and i < self.p:
            M[i] = M[i] + 1
            x -= self.beta**e
            if x - self.beta**e < 0:
                e -= 1
                i += 1
        return M

    def fl_ch(self, x: float):
        E = self.__get_exponent(x)
        M = self.__get_mantissa_ch(x, E)
        return np.sign(x) * self.__compute_fl(M, E)
    
    def __add_val_to_mantissa(self, M, v, pos):
        if M[pos] + v < self.beta:
            M[pos] += v
            return M
        elif pos == 0:
            return ValueError("Overflow")
        else:
            M[pos] = v % self.beta
            return self.__add_val_to_mantissa(self, M, v // self.beta, pos - 1)
    
    def __get_mantissa_rn(self, x, e):
        M_low = self.__get_mantissa_ch(x, e)
        M_high = np.copy(M_low)
        M_high = self.__add_val_to_mantissa(M_high, self.p - 1, 1)

        fl_low = self.__compute_fl(M_low, e)
        fl_high = self.__compute_fl(M_high, e)
        
        if abs(x - fl_low) > abs(x - fl_high):
            return M_high
        else:
            return M_low
        
    def fl_rn(self, x:float):
        E = self.__get_exponent(x)
        M = self.__get_mantissa_rn(x, E)
        return np.sign(x) * self.__compute_fl(M, E)
    
    def __get_m_numbers_for_exponent(self, E, pos):
        m_numbers = []
        if E < self.L - self.p + 1 or pos > self.p:
            return [0]
        else:
            for i in range(1, self.beta):
                 m_numbers.extend([i * self.beta**(E) + x for x in self.__get_m_numbers_for_exponent(E-1, pos + 1)])
            if pos > 1:
                m_numbers.extend(self.__get_m_numbers_for_exponent(E-1, pos + 1))
            return m_numbers

    def get_machine_numbers(self):
        m_numbers = []
        for E in range(self.L, self.U + 1):
            m_numbers.extend(self.__get_m_numbers_for_exponent(E, 1))
        m_numbers = set(m_numbers)
        return m_numbers

        
