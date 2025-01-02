#Użytkownik wpisuje liczbę. Określ ile cyfr ma ta liczba, znajdż ich sumę i średnią. Określ ile zer ma ta liczba. Zaimplementuj dialog z użytkownikiem poprzez menu 
def analiza_liczby(liczba):
    liczba_str = str(abs(liczba)) 
    cyfry = [int(c) for c in liczba_str]
    suma_cyfr = sum(cyfry)
    srednia = suma_cyfr / len(cyfry)
    liczba_zer = liczba_str.count('0')
    return len(cyfry), suma_cyfr, srednia, liczba_zer
while True:
    print("\n--- Menu ---")
    print("1. Wpisz liczbę i przeanalizuj")
    print("2. Wyjście")
    wybor = input("Wybierz opcję (1 lub 2): ")
    if wybor == "1":
        liczba = int(input("Podaj liczbę całkowitą: "))
        liczba_cyfr, suma_cyfr, srednia, liczba_zer = analiza_liczby(liczba)
        print(f"\nAnaliza liczby {liczba}:")
        print(f"Liczba cyfr: {liczba_cyfr}")
        print(f"Suma cyfr: {suma_cyfr}")
        print(f"Średnia cyfr: {srednia:.2f}")
        print(f"Liczba zer: {liczba_zer}")
    elif wybor == "2":
        print("Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

#Zadanie 2
#Napisz program wyświetlający szachownicę o zadanym rozmiarze komórek. Na przykład trzy, 
rozmiar = int(input("Podaj rozmiar komórek szachownicy: "))
wiersze = 8
kolumny = 8
for i in range(wiersze):
    for j in range(rozmiar):
        for k in range(kolumny):
            if (i + k) % 2 == 0:
                print("&" * rozmiar, end="")
            else:
                print(" " * rozmiar, end="")
        print()