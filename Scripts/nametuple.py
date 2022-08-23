from collections import namedtuple
Car = namedtuple('Car' , 'color mileage')
print(Car.color)

my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car[1])
print(tuple(my_car))
print(my_car)
print(my_car._asdict())
print(my_car._replace(color='blue'))
print(Car._make(['red', 999]))
