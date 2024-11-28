class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        if isinstance(other, Complex):
                return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented
    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented
    def __truediv__(self, other):
        if isinstance(other, Complex):
            if other.real == 0 and other.imag == 0:
                raise ZeroDivisionError("Cannot divide by zero complex number.")
            denom = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / denom
            imag_part = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real_part, imag_part)
        return NotImplemented
    def __repr__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"({self.real} {sign} {abs(self.imag)}i)"
    
z1 = Complex(3, 4)
z2 = Complex(1, -2)

print(f"z1: {z1}")   
print(f"z2: {z2}")
print(f"z1 + z2: {z1 + z2}")
print(f"z1 - z2: {z1 - z2}")
print(f"z1 * z2: {z1 * z2}")
print(f"z1 / z2: {z1 / z2}")