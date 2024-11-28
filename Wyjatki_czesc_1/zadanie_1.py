def main():
    try:
        imie = input("Podaj swoje imię: ")
        wiek = int(input("Podaj swój wiek: "))
        if wiek < 0 or wiek > 130:
            raise ValueError("Wiek musi byc liczba z przedzialu od 0 do 130.")
        print(f"Witaj, {imie}! Twój wiek to {wiek}.")
    except ValueError as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()