# Challenge 3:  Protein Sequence Similarity Matrix

## Background 
Implement a function that calculates pairwise similarity scores between protein sequences using a simplified scoring system.

## Tasks
Write a function calculate_similarity_matrix(sequences, match_score=2, mismatch_score=-1, gap_penalty=-2) that:
- Takes a list of protein sequences and scoring parameters
- Returns a symmetric similarity matrix (as a 2D list or numpy array) and a list of comparisons with their associated scores
- Uses a simple alignment scoring: match/mismatch for aligned positions, gap penalty for length differences
- For sequences of different lengths, align from the start and treat extra characters as gaps

### Challenge aspects:
- Efficient nested iteration
- Matrix operations
- Edge case handling (empty sequences, different lengths)
- Clean, readable code structure

## Data:
For this problem you'll be provided with a list of sequences which you'll need to correctly predict scores for
```python
sequences = ["ARND", "ARMD", "AKND", ""]
'''
Expected scores per comparison:
- ARND vs ARMD: 3 matches, 1 mismatch = 3*2 + 1*(-1) = 5
- ARND vs AKND: 3 matches, 1 mismatch = 3*2 + 1*(-1) = 5  
- ARMD vs AKND: 2 matches, 2 mismatches = 2*2 + 2*(-1) = 2
'''
```

## Sample Solution:
```python
import numpy as np

def calculate_similarity_matrix(sequences, match_score=2, mismatch_score=-1, gap_penality=-2):
  filtered_seqs = list(filter(None, sequences)) # Remove empty strings from list of sequences
  scores = [] # Store scores for comparisons 
  comparison = [] # Store comparisons

  # Iterate through index sequences list, exluding last item. 
  for x in range(0,len(filtered_seqs)-1):
    # Iterate through the index of sequences starting from x+1 to avoid self comparison. 
    for y in range(x+1, len(filtered_seqs)):
      comparison.append(f'{filtered_seqs[x]} vs. {filtered_seqs[y]}') 

      # For sequences of same length 
      if len(filtered_seqs[x])==len(filtered_seqs[y]):
        count=0
        for i in range(0,len(filtered_seqs[x])):
          if filtered_seqs[x][i]==filtered_seqs[y][i]:
            count+=match_score
          if filtered_seqs[x][i]!=filtered_seqs[y][i]:
            count+=mismatch_score
        scores.append(count)

      # For sequences of different length 
      if len(filtered_seqs[x])!=len(filtered_seqs[y]):
        count = 0
        if len(filtered_seqs[x])>len(filtered_seqs[y]):
          for i in range(0,len(filtered_seqs[x]) - (len(filtered_seqs[x])-len(filtered_seqs[y]))):
            if filtered_seqs[x][i]==filtered_seqs[y][i]:
              count+=match_score
            if filtered_seqs[x][i]!=filtered_seqs[y][i]:
              count+=mismatch_score
          count+=(len(filtered_seqs[x])-len(filtered_seqs[y]))*gap_penality #Apply gap penality 
          scores.append(count)
        if len(filtered_seqs[x])<len(filtered_seqs[y]):
          for i in range(0,len(filtered_seqs[x])):
            if filtered_seqs[x][i]==filtered_seqs[y][i]:
              count+=match_score
            if filtered_seqs[x][i]!=filtered_seqs[y][i]:
              count+=mismatch_score
          count+= (len(filtered_seqs[y])-len(filtered_seqs[x]))*gap_penality #Apply gap penalty
          scores.append(count)

  for i in range(0,len(comparison)):
    print(f'{comparison[i]}: {scores[i]}')

  return scores
      
result = calculate_similarity_matrix(test_sequences)
print(result)
```
