def repeater(value):
    x = 1
    while x<100:
        yield x, value
        x += 1

# for x, count in repeater('ahoj'):
#     print(x, " ", count)


print(dict(repeater('a')))

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

print(list(bounded_repeater('a', 5)))
