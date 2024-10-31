class Samochod:
    def __init__(self, model, rok_wydania, producent, pojemnosc_silnika, kolor, cena):
        self.model = model
        self.rok_wydania = rok_wydania
        self.producent = producent
        self.pojemnosc_silnika = pojemnosc_silnika
        self.kolor = kolor
        self.cena = cena
    def getInfo(self):
        return (f"Model: {self.model}, Rok wydania: {self.rok_wydania}, Producent: {self.producent}, Pojemność silnika: {self.pojemnosc_silnika}, Kolor: {self.kolor}, Cena: {self.cena} PLN")
    @classmethod
    def create_from_input(cls):
        model = input('Podaj model:')
        rok_wydania = input('Rok wydania:')
        producent = input('Producent:')
        pojemnosc_silnika = input('Pojemnosc silnika:')
        kolor = input('Kolor:')
        cena = input('Cena:')
        return cls(model, rok_wydania, producent, pojemnosc_silnika, kolor, cena)
print(Samochod.create_from_input())