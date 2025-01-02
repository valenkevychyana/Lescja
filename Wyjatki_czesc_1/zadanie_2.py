#1 wersja (nie obsługuje wyjątku wewnątrz funkcji)
def create_greeting(name, age):
    if age < 0 or age > 130:
        raise ValueError("Wiek musi byc od 0 do 130.")
    return f"Witaj, {name}! Twój wiek to {age}."
def main():
    try:
        name = input("Podaj swoje imię: ")
        age = int(input("Podaj swój wiek: "))
        greeting = create_greeting(name, age)
        print(greeting)
    except ValueError as e:
        print(f"Blad: {e}")
if __name__ == "__main__":
    main()

#2 wersja (obsługuje wyjątek wewnątrz funkcji)

def create_greeting(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Wiek musi byc od 0 do 130.")
        return f"Witaj, {name}! Twój wiek to {age}."
    except ValueError as e:
        print(f"Błąd: {e}")
def main():
    name = input("Podaj swoje imię: ")
    age = int(input("Podaj swój wiek: "))
    greeting = create_greeting(name, age)
    print(greeting)

if __name__ == "__main__":
    main()
