class Samolot:
    def __init__(self, typ, max_pax, current_pax=0):
        if max_pax < 0 or current_pax < 0:
            raise ValueError("Liczba pasażerów nie może być ujemna.")
        if current_pax > max_pax:
            raise ValueError("Aktualna liczba pasażerów nie może przekraczać maksymalnej pojemności.")
        self.typ = typ
        self.max_pax = max_pax
        self.current_pax = current_pax
    def __eq__(self, other):
        if isinstance(other, Samolot):
            return self.typ == other.typ
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Samolot):
            return self.max_pax > other.max_pax  
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Samolot):
            return self.max_pax >= other.max_pax
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Samolot):
            return self.max_pax < other.max_pax
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Samolot):
            return self.max_pax <= other.max_pax
        return NotImplemented
    def __add__(self, liczba_pax):
        if isinstance(liczba_pax, int):
            new_pax = self.current_pax + liczba_pax
            if new_pax > self.max_pax:
                raise ValueError("Przekroczono maksymalną liczbę pasażerów!")
            return Samolot(self.typ, self.max_pax, new_pax)
        return NotImplemented
    def __sub__(self, liczba_pax):
        if isinstance(liczba_pax, int):
            new_pax = self.current_pax - liczba_pax
            if new_pax < 0:
               raise ValueError("Liczba pasażerów nie może być ujemna!")
            return Samolot(self.typ, self.max_pax, new_pax)
        return NotImplemented
    def __iadd__(self, liczba_pax):
        if isinstance(liczba_pax, int):
            self.current_pax += liczba_pax
            if self.current_pax > self.max_pax:
                raise ValueError("Przekroczono maksymalną liczbę pasażerów!")
            return self
        return NotImplemented
    def __isub__(self, liczba_pax):
        if isinstance(liczba_pax, int):
            self.current_pax -= liczba_pax
            if self.current_pax < 0:
                raise ValueError("Liczba pasażerów nie może być ujemna!")
            return self
        return NotImplemented
    def __repr__(self):
        return f"Samolot(typ='{self.typ}', max_pax={self.max_pax}, current_pax={self.current_pax})"

samolot1 = Samolot("Boeing 747", 400, 200)
samolot2 = Samolot("Airbus A320", 180, 100)
print(samolot1 == samolot2)
print(samolot1 > samolot2)
print(samolot1 <= samolot2)
samolot3 = samolot1 + 50
print(samolot3)
samolot4 = samolot3 - 100
print(samolot4)
samolot1 += 100
print(samolot1)
samolot1 -= 50
print(samolot1)

               

            