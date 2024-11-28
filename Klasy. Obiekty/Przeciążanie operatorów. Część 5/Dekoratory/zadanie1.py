import time

def czas_wykonania(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        czas = end - start
        print(f"Czas wykonania: {czas:.6f} sekund")
        return wynik
    return wrapper
@czas_wykonania
def znajdz_liczby_pierwsze(limit):
    liczby_pierwsze = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            liczby_pierwsze.append(num)
    return liczby_pierwsze 

liczby = znajdz_liczby_pierwsze(1000)   
print(f"Liczby pierwsze od 0 do 1000: {liczby}")
