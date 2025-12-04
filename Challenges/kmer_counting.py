def count_kmers(sequence, k=3, merge_reverse_complement=False):
  if k<=len(sequence):
    if merge_reverse_complement==False:
      kmers= {}
      for i in range(0,len(sequence)-k+1):
        if sequence[i:i+k] in kmers:
          kmers[sequence[i:i+k]]+=1
        else: 
          kmers[sequence[i:i+k]]=1

      sorted_kmers = sorted(kmers.items(), key=lambda item: item[1], reverse=True)
      return sorted_kmers
    
    # If merge_reverse_complement==True
    else:
      kmers= {}
      for i in range(0,len(sequence)-k+1):
        rc = reverse_complement(sequence[i:i+k])
        canonical = min(sequence[i:i+k], rc)
        if canonical in kmers:
          kmers[canonical]+=1
        else:
          kmers[canonical]=1

      sorted_kmers = sorted(kmers.items(), key=lambda item: item[1], reverse=True)
      return sorted_kmers

  else:
    print('Error: k-mer length cannot be longer than sequence.')

def reverse_complement(seq):
    nucleotide_comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    compliment = ''
    
    for i in range(0,len(seq)):
      compliment+= nucleotide_comp[seq[i]]
    
    reverse_compliment =''
    for i in range(1,len(compliment)+1):
      reverse_compliment+=compliment[-i]

    return reverse_compliment





print(count_kmers('ATGCAT', k=3, merge_reverse_complement=True))
