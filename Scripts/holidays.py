# Happy Holidays!
# with height = 5:
#     *
#    ***
#   *****
#  *******
# *********
#     |
# Dependency: Python 3.3
 
height = 10
stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
print((' ' * height) + '|')