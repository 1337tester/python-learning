__author__ = 'zii'


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print(keywords)
    """keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])"""

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")


print("-" * 40)

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

def fook(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    foo(x, *new_args, **kwargs)


foo('fff', 1, 2, 3, key1 = 'aa', key = 3.4)
fook('fff', 1, 2, 3, key1 = 'aa', name = 3.4)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

car = AlwaysBlueCar('green', 48392)

print(car.color, car.mileage)
