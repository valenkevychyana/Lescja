def main():
    numbers = []
    while True:
        try:
            num = float(input("Wprowadź liczbę dodatnią (aby zakończyć, napisz 'end'): "))
            if num < 0:
                raise ValueError("Liczba nie może być ujemna!")
            numbers.append(num)
        except ValueError as e:
            print(f"Помилка: {e}")
            break
    if numbers:
        total_sum = sum(numbers)
        print(f"Suma wszystkich liczb: {total_sum}")
    else:
        print("Lista numerów jest pusta.")

if __name__ == "__main__":
    main()