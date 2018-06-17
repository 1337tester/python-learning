import functools
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

print(greet())
print(greet.__name__, greet.__doc__)
print(40*'-')

def uppercase2(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase2
def greet2():
    """Return a friendly greeting."""
    return 'Hello!'

print(greet2())
print(greet2.__name__, greet2.__doc__)
