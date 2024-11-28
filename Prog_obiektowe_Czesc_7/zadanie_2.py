import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania: {end_time - start_time:.4f} sekund")
        return result
    return wrapper
@timer
def get_primes_in_range(start, end):
    return [n for n in range(max(2, start), end + 1) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]

start_range = 10
end_range = 50
prime_numbers = get_primes_in_range(start_range, end_range)
print(f"Liczby pierwsze z zakresu od {start_range} do {end_range}:", prime_numbers)