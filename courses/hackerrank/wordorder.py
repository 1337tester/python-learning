"""
Input Format
The first line contains the integer, .
The next  lines each contain a word.

Output Format
Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""
import collections

n = int(input())
slovnik = collections.OrderedDict()
for i in range(n):
    slovo = input()
    if slovo not in slovnik:
        slovnik[slovo] = 1
    else:
        slovnik[slovo] += 1

print(len(slovnik.keys()))
print(" ".join(str(e) for e in slovnik.values()))
