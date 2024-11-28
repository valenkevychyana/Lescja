import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania {end_time - start_time:.4f} sekund")
        return result
    return wrapper
    
@timer
def get_primes_up_to_1000():
    return [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
prime_numbers = get_primes_up_to_1000()
print("Прості числа:", prime_numbers)