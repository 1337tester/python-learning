def arg_kwarg(default, *args, **kwargs):
    print(default)
    if args: print(args)
    if kwargs: print(kwargs)


arg_kwarg('aa')
print(80*'*')
arg_kwarg('aa', 1, 4, 5)
print(80*'*')
arg_kwarg('aa', 5, 6, 7, a=1, b='r')
