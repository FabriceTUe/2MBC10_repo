import numpy as np

class FloatingPointSystem():
    def __init__(self, beta, p, L, U):
        self.beta = beta
        self.p = p
        self.L = L
        self.U = U

    def __get_exponent(self, x):
        i = self.L
        while self.beta**(i + 1) < abs(x) and i < self.U:
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

        # ensure first digit is at least 1
        M[0] = 1
        x -= self.beta**e

        while x > 0 and i < self.p:
            if x - self.beta**e >= 0 and M[i] < self.beta - 1:
                M[i] = M[i] + 1
                x -= self.beta**e
            else:
                e -= 1
                i += 1
        return M

    def fl_ch(self, x: float):
        E = self.__get_exponent(x)
        M = self.__get_mantissa_ch(x, E)
        return self.__compute_fl(M, E)
    
    def fl_rn(self, x):
        e = self.__get_exponent(x)
        M_low = self.__get_mantissa_ch(x, e)
        fl_low = self.__compute_fl(M_low, e)
        m_numbers = self.get_machine_numbers()
        higher_m_numbers = [n for n in m_numbers if n > fl_low]
        if len(higher_m_numbers) == 0:
            fl_high = fl_low
        else:
            fl_high = min(higher_m_numbers)

        if abs(x - fl_low) > abs(x - fl_high):
            return fl_high
        else:
            return fl_low
    
    def __get_m_numbers_for_exponent(self, E, pos):
        '''Run with initial values E and 0.''' 
        m_numbers = []
        if E < self.L - self.p + 1 or pos > self.p - 1:
            return [0]
        else:
            for i in range(1, self.beta):
                 m_numbers.extend([i * self.beta**(E) + x for x in self.__get_m_numbers_for_exponent(E-1, pos + 1)])
            if pos > 0:
                m_numbers.extend(self.__get_m_numbers_for_exponent(E-1, pos + 1))
            return m_numbers

    def get_machine_numbers(self):
        m_numbers = []
        for E in range(self.L, self.U + 1):
            m_numbers.extend(self.__get_m_numbers_for_exponent(E, 0))
        m_numbers = set(m_numbers)
        return m_numbers
    
    def get_min(self):
        return self.beta**self.L

    def get_max(self):
        M = np.ones(self.p) * (self.beta - 1)
        return self.__compute_fl(M, self.U)

        
