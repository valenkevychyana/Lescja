class Device:
    def __init__(self, name, brand, power):
        self.name = name
        self.brand = brand
        self.power = power
    def get_info(self):
        return f"Nazwa: {self.name}, marka: {self.brand}, moc: {self.power}W"

class CoffeeMachine(Device):
    def __init__(self, name, brand, power, coffee_type):
        super().__init__(name, brand, power)
        self.coffee_type = coffee_type
    def brew_coffee(self):
       print(f"Parze {self.coffee_type}") 
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, typ kawy: {self.coffee_type}"
    
class Blender(Device):
    def __init__(self, name, brand, power, speed_levels):
        super().__init__(name, brand, power)
        self.speed_levels = speed_levels
    def blend(self):
      print("Blenduję składniki")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, poziomy prędkości: {self.speed_levels}"
    
class MeatGrinder(Device):
    def __init__(self, name, brand, power, capacity):
        super().__init__(name, brand, power)
        self.capacity = capacity

    def grind(self):
      print("Mielę mięso")
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, pojemność: {self.capacity}kg"

coffee_machine = CoffeeMachine("Ekspres do kawy", "Philips", 1500, "espresso")
blender = Blender("Blender", "Bosch", 800, 5)
meat_grinder = MeatGrinder("Maszynka do mięsa", "Moulinex", 1200, 2)

coffee_machine.brew_coffee()
blender.blend()
meat_grinder.grind()

print(coffee_machine.get_info())
print(blender.get_info())
print(meat_grinder.get_info())