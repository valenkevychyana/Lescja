class Book:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania 
    def __str__(self):
        return f"{self.tytul}, {self.autor}, {self.rok_wydania} roku"
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.tytul == other.tytul, self.autor == other.autor, self.rok_wydania == other.rok_wydania)
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.rok_wydania < other.rok_wydania
    
obj1 = Book("Memory", "George Orwell", "1949")
obj2 = Book("Introduction", "Margarett", "1859")

print(obj1)
print(obj1 == obj2)
print(obj1 < obj2)