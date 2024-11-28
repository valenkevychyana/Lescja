import math

class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
shapes = [
    Rectangle(4, 6),
    Circle(3), 
    RightTriangle(5, 12),
    Trapezoid(3, 7, 5) 
]
for shape in shapes:
     print(f"Pole powierzchni {shape.__class__.__name__}: {shape.area():.2f}")