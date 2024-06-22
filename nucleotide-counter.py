#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in

dna_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def nucleotide_counter(dna_seq):
  base_count = {'A':0, 'T':0, 'C':0, 'G':0}
  for i in range(len(dna_seq)):
    base_count[dna_seq[i]]+=1
  return base_count
print(nucleotide_counter(dna_string))
