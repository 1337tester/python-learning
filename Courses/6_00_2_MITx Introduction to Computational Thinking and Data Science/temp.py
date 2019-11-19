#a = 1_000_000_000_000_000
#print(a)

file1 = open('fuzz.txt', 'x')

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in a:
    for letteer in a:
        for letteeer in a:
            item = letter + letteer + letteeer
            file1.write(item + '\n')