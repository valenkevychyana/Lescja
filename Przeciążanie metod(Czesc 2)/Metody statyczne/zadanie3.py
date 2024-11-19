class MetricImperialConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084
    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084
    @staticmethod
    def centimeters_to_inches(centimeters):
        return centimeters / 2.54
    @staticmethod
    def inches_to_centimeters(inches):
        return inches * 2.54
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371
    @staticmethod
    def miles_to_kilometers(miles):
        return miles / 0.621371
    
length_in_feet = MetricImperialConverter.meters_to_feet(10)
print(f"10 metrów to {length_in_feet:.2f} stóp.")
length_in_meters = MetricImperialConverter.feet_to_meters(32.8)
print(f"32.8 stóp to {length_in_meters:.2f} metrów.")
length_in_inches = MetricImperialConverter.centimeters_to_inches(50)
print(f"50 cm to {length_in_inches:.2f} cali.")
length_in_centimeters = MetricImperialConverter.inches_to_centimeters(20)
print(f"20 cali to {length_in_centimeters:.2f} cm.")
distance_in_miles = MetricImperialConverter.kilometers_to_miles(5)
print(f"5 kilometrów to {distance_in_miles:.2f} mil.")
distance_in_kilometers = MetricImperialConverter.miles_to_kilometers(3.1)
print(f"3.1 mil to {distance_in_kilometers:.2f} kilometrów.")