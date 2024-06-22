# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

s = 'GATATATGCATATACTT'
t = 'ATAT'

position = []
for i in range(len(s)):
  if t in s[i:i+4]:
    position.append(i)
print(position)
