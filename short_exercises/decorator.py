import functools
def uppercase(func):
    def wrapper():
        # original_result = func()
        # modified_result = original_result.upper()
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
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
    """Return a second friendly greeting."""
    return 'Howdy!'

print(greet2())
print(greet2.__name__, greet2.__doc__)
