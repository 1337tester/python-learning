from cmath import phase, sqrt

number = complex(input())
imag = number.imag
real = number.real

print(abs(sqrt(imag**2 + real**2)))
print(phase(number))