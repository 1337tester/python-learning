def capitalize(string):
    # a = [x for x in string.split()]
    # a[0] = a[0].capitalize()
    # a[-1] = a[-1].capitalize()
    # return ' '.join(a)

#try finish this somehow
    # return ' '.join([x.capitalize() for x in string.split()])
    return string.title()

#test
print(capitalize('a1y2aa ahoj moja ereh fgd4'))
print(capitalize(' ahoj moja  '))
print(capitalize(' ahoj moja a '))
print(capitalize(' ahoj moja a 8'))
print(capitalize('q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'))
