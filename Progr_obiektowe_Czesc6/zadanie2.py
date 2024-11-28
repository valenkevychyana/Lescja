import math

class Shape:
    def area(self):
        raise NotImplementedError
    def __int__(self):
        return int(self.area())
    def __str__(self):
         return "Figura geometryczna o nieznanej specyfikacji."
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return (f"Prostokąt o szerokości {self.width} i wysokości {self.height}")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return (f"Okrąg o promieniu {self.radius}")
class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __str__(self):
        return (f"Trójkąt prostokątny o podstawie {self.base} i wysokości {self.height}")
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
    def __str__(self):
        return (f"Trapez o podstawach {self.base1}, {self.base2} i wysokości {self.height}")
shapes = [
    Rectangle(4, 6),
    Circle(3),
    RightTriangle(5, 12),
    Trapezoid(3, 7, 5)
]
for shape in shapes:
    print(str(shape))
    print(f"Pole: {shape.area():.2f}")
    print(f"Pole (jako int): {int(shape)}\n")