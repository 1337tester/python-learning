def dispatch_dict(operator, x, y):
    import pdb; set_trace()
    return {
        'add': lambda: x + y,
        'subt': lambda: x - y,
        'mult': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_dict('mult', 2, 8))
print(dispatch_dict('unknown', 2, 8))
