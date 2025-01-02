numbers = [3,1,4,1,5,9]
numbers.sort()
print(numbers)

names = ["Alice", "Charlie", "Bob"]
names.sort(key = len)
print(names)

#sorted
numbers = [3,1,4,1,5,9]
sorted_numbers = sorted(numbers, reverse = True)
print(sorted_numbers)

#filter
numbers = [1,2,33,4,5,6]
def is_even(n):
    return n % 2 == 0
even_numbers = filter(is_even, numbers)
print(even_numbers)

odd_numbers = filter(lambda n: n % 2 != 0, numbers)
print(list(odd_numbers))

#map
numbers = [1,2,3,4]

#Funkcja która mnoży liczby przez 2
def double(n):
    return n * 2

double_numbers = map(double, numbers)
print(list(double_numbers))

squared_numbers = map(lambda n: n ** 2, numbers)
print(list(squared_numbers))

#reduce

numbers = [1,2,3,4]

def add(x,y):
    return x + y

total = reduce(add, numbers)
print(total)

product = reduce(lambda x,y: x*y, numbers)
print(product)
