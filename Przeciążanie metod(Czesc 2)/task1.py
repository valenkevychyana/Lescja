class Car:
    def __init__(self, model, rok_wydania, cena):
        self.model = model
        self.rok_wydania = rok_wydania
        self.cena = cena
    def __str__(self):
        return f"{self.model} {self.rok_wydania} roku, {self.cena} PLN"
    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return (self.model == other.model, self.rok_wydania == other.rok_wydania, self.cena == other.cena)
    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.rok_wydania < other.rok_wydania

car1 = Car("Toyota", 2015, 50000)
car2 = Car("Honda", 2018, 30000)

print(car1)
print(car1 == car2)
print(car1 < car2)
