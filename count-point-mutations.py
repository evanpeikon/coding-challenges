# Given two DNA strings of equal length (not exceeding 1 kbp), return the hamming distance dH(s,t).

string1 = 'GAGCCTACTAACGGGAT'
string2 ='CATCGTAATGACGGCCT'
hamming_distance = 0

for i in range(len(string1)):
  if string1[i]==string2[i]:
    hamming_distance +=0
  else:
    hamming_distance +=1
print(hamming_distance)
