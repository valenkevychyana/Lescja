class TemperatureConverter:
    _conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter._conversion_count += 1
        return (celsius * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter._conversion_count += 1
        return (fahrenheit - 32) * 5/9
    @staticmethod
    def get_conversion_count():
        return TemperatureConverter._conversion_count
    
temp_f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C to {temp_f}°F")
temp_c = TemperatureConverter.fahrenheit_to_celsius(77)
print(f"77°F to {temp_c:.2f}°C")
conversion_count = TemperatureConverter.get_conversion_count()
print(f"Liczba wykonanych konwersji: {conversion_count}")


