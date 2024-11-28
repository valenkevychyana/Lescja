
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return NotImplemented
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented
    def __sub__(self, value):
        if isinstance(value, (int, float)):
            new_radius = self.radius - value
            if new_radius < 0:
                raise ValueError("Radius cannot be negative.")
            return Circle(new_radius)
        return NotImplemented
    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            if self.radius < 0:
                raise ValueError("Radius cannot be negative.")
            return self
        return NotImplemented
    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            if self.radius < 0:
                raise ValueError("Radius cannot be negative.")
            return self
        return NotImplemented
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
circle1 = Circle(7)
circle2 = Circle(10)

print(circle1 == circle2)
print(circle1 < circle2)
print(circle1 + 3) 

