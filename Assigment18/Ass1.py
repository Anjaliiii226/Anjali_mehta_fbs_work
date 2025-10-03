class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"ComplexNumber object created: {self}")
    def __del__(self):
        print(f"ComplexNumber object destroyed: {self}")

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Operand must be ComplexNumber")
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("Operand must be ComplexNumber")
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
