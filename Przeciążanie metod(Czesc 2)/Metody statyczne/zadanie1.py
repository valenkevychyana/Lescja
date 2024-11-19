class Fraction:
    _instance_count = 0
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction._instance_count += 1

    @staticmethod
    def get_instance_count():
        return Fraction._instance_count

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = Fraction(5, 6)
print(Fraction.get_instance_count())