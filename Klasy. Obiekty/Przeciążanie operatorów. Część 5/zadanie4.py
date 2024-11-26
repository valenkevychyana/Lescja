class Apartament:
    def __init__(self, powierzchnia, cena):
        if powierzchnia < 0 or cena < 0:
            raise ValueError("Powierzchnia i cena nie mogą być ujemne.")
        self.powierzchnia = powierzchnia
        self.cena = cena
    def __eq__(self, other):
        if isinstance(other, Apartament):
            return self.powierzchnia == other.powierzchnia
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, Apartament):
            return self.powierzchnia != other.powierzchnia
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Apartament):
            return self.cena > other.cena
        return NotImplemented
    def __repr__(self): 
        return f"Apartament(powierzchnia={self.powierzchnia}m², cena={self.cena}zł)"
    
ap1 = Apartament(50, 300000)
ap2 = Apartament(60, 350000)
ap3 = Apartament(50, 280000)
print(ap1 == ap2)
print(ap1 == ap3)
print(ap1 != ap2)
print(ap1 != ap3) 
print(ap1 > ap2)
print(ap2 > ap1)
