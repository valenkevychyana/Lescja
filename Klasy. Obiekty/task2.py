class Book:
    def __init__(self, tytul, rok_wydania, wydawca, gatunek, autor, cena):
        self.tytul = tytul
        self.rok_wydania = rok_wydania 
        self.wydawca = wydawca
        self.gatunek = gatunek
        self.autor = autor
        self.cena = cena
    def getInfo(self):
        return (f"Tytul: {self.tytul}, Rok wydania: {self.rok_wydania}, Wydawca: {self.wydawca}, Gatunek: {self.gatunek}, Auor: {self.autor}, Cena: {self.cena}")
    @classmethod
    def create_from_input(cls):
        tytul = input('Tytul: ')
        rok_wydania = input('Rok wydania: ') 
        wydawca = input('Wydawca: ')
        gatunek = input('Gatunek: ')
        autor = input('Autor: ')
        cena = input('Cena: ')
        return cls(tytul, rok_wydania, wydawca, gatunek, autor, cena)
print(Book.create_from_input())
