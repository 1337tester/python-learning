"""Returns the diff of the letter count of two inputted strings - if 0 -> words are anagrams(contain the same letters)"""
w1 = input()
w2 = input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total += abs(w1.count(letter)- w2.count(letter))
print(total)
