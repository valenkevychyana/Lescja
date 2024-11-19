class Ship:
    def __init__(self, name, country, displacement):
        self.name = name
        self.country = country
        self.displacement = displacement
    def get_info(self):
        return f"Nazwa: {self.name}, kraj: {self.country}, wyporność: {self.displacement} ton"
    def sail(self):
        print(f"{self.name} wypływa w morze.")

class Frigate(Ship):
    def __init__(self, name, country, displacement, armament):
        super().__init__(name, country, displacement)
        self.armament = armament
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, uzbrojenie: {self.armament}"  
    def patrol(self):
        print(f"{self.name} patroluje wybrzeże, wyposażona w {self.armament}.")

class Destroyer(Ship):
    def __init__(self, name, country, displacement, torpedoes):
        super().__init__(name, country, displacement)
        self.torpedoes = torpedoes
    def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, torpedy: {self.torpedoes}"
    def attack(self):
        print(f"{self.name} atakuje wroga z użyciem {self.torpedoes} torped.")

class Cruiser(Ship):
    def __init__(self, name, country, displacement, missile_range):
        super().__init__(name, country, displacement)
        self.missile_range = missile_range
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, zasięg pocisków: {self.missile_range} km"
    def launch_missile(self):
        print(f"{self.name} wystrzeliwuje pocisk o zasięgu do {self.missile_range} km.")

frigate = Frigate()
destroyer = Destroyer()
cruiser = Cruiser()


frigate.patrol()
frigate.sail()
destroyer.attack()
destroyer.sail()
cruiser.launch_missile()
cruiser.sail()

print(frigate.get_info())
print(destroyer.get_info())
print(cruiser.get_info())