"""
14 - Make a function that receives a distance in Km and the amount of gas liters used by a car.
Calculate the consumpiton Km/l and write a message acording the table below:
  CONSUMPTION             (Km/l)           MESSAGE
   less than                8           Sell the car!
    between               8 e 14          Economic!
  bigger than               12         Very economic!
"""


# Car consumption function.
def car_consumption(distance, liters):
    if (type(distance) is float or type(distance) is int) and (type(liters) is float or type(liters) is int):
        consumption = distance/liters
        if consumption < 8:
            return 'Sell the car!'
        elif 8 <= consumption <= 12:
            return 'Economic!'
        else:
            return 'Very economic!'
    return 'Both parameters should be numeric values.'


# Testing the function.
print(car_consumption(12, 'd'))      # OUTPUT: Both parameters should be numeric values.
print(car_consumption('d', 12))      # OUTPUT: Both parameters should be numeric values.
print(car_consumption(12, 12))       # OUTPUT: Sell the car!
print(car_consumption(12, 12.5))     # OUTPUT: Sell the car!
print(car_consumption("oioi", 'd'))  # OUTPUT: Both parameters should be numeric values.
print(car_consumption(3.75, 12.3))   # OUTPUT: Sell the car!
print(car_consumption(12, 1))        # OUTPUT: Economic!
print(car_consumption(30, 2))        # OUTPUT: Very economic!
