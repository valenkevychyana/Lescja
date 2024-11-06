class Stadium:
    def __init__(self, nazwa_stadionu, data_otwarcia, liczba_miejsc_siedzacych):
        self.nazwa_stadionu = nazwa_stadionu
        self.data_otwarcia = data_otwarcia
        self.liczba_miejsc_siedzacych = liczba_miejsc_siedzacych
    def __str__(self):
        return f"{self.nazwa_stadionu}, {self.data_otwarcia}, {self.liczba_miejsc_siedzacych}"
    def __eq__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return (self.nazwa_stadionu == other.nazwa_stadionu, self.data_otwarcia == other.data_otwarcia, self.liczba_miejsc_siedzacych == other.liczba_miejsc_siedzacych)
    
obj1 = Stadium("Camp", "10 czerwca", "3000")
obj2 = Stadium("Olimp", "13 lipca", "2000")

print(obj1)
print(obj1 == obj2)
