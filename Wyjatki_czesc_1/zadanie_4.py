# 1 wersja

def calculate_sum(numbers):
    if any(num < 0 for num in numbers):
        raise ValueError("Na liście jest liczba ujemna!")
    return sum(numbers)
def main():
    numbers = []
    while True:
        try:
           num = float(input("Wpisz liczbę dodatnią (wprowadź liczbę ujemną, aby uzupełnić): "))
           if num < 0:
            break
           numbers.append(num)
        except ValueError as e:
            print(f"Blad: {e}")
        
    try:
        total_sum = calculate_sum(numbers)
        print(f"Suma liczb: {total_sum}")
    except ValueError as e:
        print(f"ПBlad: {e}")
if __name__ == "__main__":
    main()

# 2 wersja

def calculate_sum(numbers):
    try:
        if any(num < 0 for num in numbers):
            raise ValueError("Na liście znajduje się liczba ujemna!")
        return sum(numbers)
    except ValueError as e:
        print(f"Blad: {e}")

def main():
    numbers = [] 
    while True:
        try:
            num = float(input("Wpisz liczbę dodatnią (wprowadź liczbę ujemną, aby uzupełnić): "))
            if num < 0:
                break
            numbers.append(num)
        except ValueError as e:
            print(f"Помилка: {e}")

    total_sum = calculate_sum(numbers)
    print(total_sum)
if __name__ == "__main__":
    main()

    

    