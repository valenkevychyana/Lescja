class Stadium:
    def __init__(self, nazwa_stadionu, data_otwarcia, kraj, miasto, liczba_miejsc_siedzących):
        self.nazwa_stadionu = nazwa_stadionu
        self.data_otwarcia = data_otwarcia
        self.kraj = kraj
        self.miasto = miasto
        self.liczba_miejsc_siedzących = liczba_miejsc_siedzących
    def getInfo(self):
        return(f"Nazwa Stadionu: {self.nazwa_stadionu}, Data otwarcia: {self.data_otwarcia}, Kraj: {self.kraj}, Miasto: {self.miasto}, Liczba miejsc siedzących: {self.liczba_miejsc_siedzących}")
    @classmethod
    def create_from_input(cls):
        nazwa_stadionu = input('Podaj nazwe stadionu: ')
        data_otwarcia = input('Podaj date otwarcia: ')
        kraj = input('Podaj kraj: ')
        miasto = input('Poday miasto: ')
        liczba_miejsc_siedzących = input('Podaj liczbe miejsc siedzących: ')
        return cls(nazwa_stadionu, data_otwarcia, kraj, miasto, liczba_miejsc_siedzących)
print(Stadium.create_from_input())