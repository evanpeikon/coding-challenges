## Challenge 2 - Basic Sequence Feature Extraction
### Background
Before we can predict function from protein sequences, we need to extract meaningful features. Your task is to write a function that takes a protein sequence and extracts basic physicochemical features that could be predictive of function.

### Requirements
Your function should calculate at least these features:
- Sequence length
- Amino acid composition (fraction of each of the amino acids in the sequence)
- Hydrophobicity (average hydrophobicity of the sequence)
- Charge (net charge at physiological pH)
- Molecular weight (approximate)

Additional success criteria:
- Handle edge cases (empty sequences, invalid amino acids)
- Return consistent feature dictionary structure

### Data
For this problem you'll be provided with a dictionary of amino acid properties and a list of test sequences:
```python
# Amino acid properties
amino_acid_properties = {
    'A': {'name': 'Alanine', 'hydrophobicity': 1.8, 'charge': 0, 'molecular_weight': 89.1},
    'R': {'name': 'Arginine', 'hydrophobicity': -4.5, 'charge': 1, 'molecular_weight': 174.2},
    'N': {'name': 'Asparagine', 'hydrophobicity': -3.5, 'charge': 0, 'molecular_weight': 132.1},
    'D': {'name': 'Aspartic acid', 'hydrophobicity': -3.5, 'charge': -1, 'molecular_weight': 133.1},
    'C': {'name': 'Cysteine', 'hydrophobicity': 2.5, 'charge': 0, 'molecular_weight': 121.2},
    'Q': {'name': 'Glutamine', 'hydrophobicity': -3.5, 'charge': 0, 'molecular_weight': 146.2},
    'E': {'name': 'Glutamic acid', 'hydrophobicity': -3.5, 'charge': -1, 'molecular_weight': 147.1},
    'G': {'name': 'Glycine', 'hydrophobicity': -0.4, 'charge': 0, 'molecular_weight': 75.1},
    'H': {'name': 'Histidine', 'hydrophobicity': -3.2, 'charge': 0.1, 'molecular_weight': 155.2},
    'I': {'name': 'Isoleucine', 'hydrophobicity': 4.5, 'charge': 0, 'molecular_weight': 131.2},
    'L': {'name': 'Leucine', 'hydrophobicity': 3.8, 'charge': 0, 'molecular_weight': 131.2},
    'K': {'name': 'Lysine', 'hydrophobicity': -3.9, 'charge': 1, 'molecular_weight': 146.2},
    'M': {'name': 'Methionine', 'hydrophobicity': 1.9, 'charge': 0, 'molecular_weight': 149.2},
    'F': {'name': 'Phenylalanine', 'hydrophobicity': 2.8, 'charge': 0, 'molecular_weight': 165.2},
    'P': {'name': 'Proline', 'hydrophobicity': -1.6, 'charge': 0, 'molecular_weight': 115.1},
    'S': {'name': 'Serine', 'hydrophobicity': -0.8, 'charge': 0, 'molecular_weight': 105.1},
    'T': {'name': 'Threonine', 'hydrophobicity': -0.7, 'charge': 0, 'molecular_weight': 119.1},
    'W': {'name': 'Tryptophan', 'hydrophobicity': -0.9, 'charge': 0, 'molecular_weight': 204.2},
    'Y': {'name': 'Tyrosine', 'hydrophobicity': -1.3, 'charge': 0, 'molecular_weight': 181.2},
    'V': {'name': 'Valine', 'hydrophobicity': 4.2, 'charge': 0, 'molecular_weight': 117.1}}

# Test protein sequences
test_sequences = ["MKWVTFISLLFLFSSAYS", "MKTAYIAKQRQISFVKSHFRVGDGTQDNLS", "MGHRHKFGKGKDSGFKHALVMKGAP", "ARNDCQEGHILKMFPSTWYV"]
```

### Example Solution
```python
def extract_feature_sequences(seq): 
  # Logic for edge case handling 
  valid_AA = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
  Conditions = [0,0] # Condition must be 0,0 for downstream code to run
  if len(seq)==0:
    Conditions[0]+=1
  for i in range(0,len(seq)):
    if seq[i] in valid_AA:
      pass
    else:
      Conditions[1]+=1

  if Conditions[0]==0 and Conditions[1]==0: 
    # Calculate amino acid composition of sequence 
    AA_composition = {}
    for i in range(0,len(seq)):
      if seq[i] in AA_composition:
        AA_composition[seq[i]]+=1
      else:
        AA_composition[seq[i]]=1
        
    for i in AA_composition.keys():
      AA_composition[i]= round((AA_composition[i]/len(seq)),2)
    
    # Calculate hydrophobicity of sequence
    hydrophobicity = 0
    for i in range(0,len(seq)):
      hydrophobicity+= amino_acid_properties[seq[i]]['hydrophobicity']

    # Calculate net charge of sequence
    net_charge = 0
    for i in range(0,len(seq)):
      net_charge+=amino_acid_properties[seq[i]]['charge']

    # Calculate molecular weight of sequence
    molecular_weight = 0
    for i in range(0,len(seq)):
      molecular_weight+=amino_acid_properties[seq[i]]['molecular_weight']
  
    # Compile features in dictionary and return feature_dict 
    feature_dict = {'Sequence Length':len(seq), 'Amino Acid Composition':AA_composition, 'Average Hydrophobicity':round((hydrophobicity/len(seq)),2), 
                    'Net Charge':round(net_charge,2), 'Molecular Weight':round(molecular_weight,2)}
    return feature_dict
  
  elif Conditions[0]>0 and Conditions[1]==0:
    return print('Error: Empty Sequence')

  elif Conditions[0]==0 and Conditions[1]>0:
    return print('Error: Invalid Amino Acid In Sequence')

# Test function
test_sequences = ["MKWVTFISLLFLFSSAYS", "MKTAYIAKQRQISFVKSHFRVGDGTQDNLS", "MGHRHKFGKGKDSGFKHALVMKGAP", "ARNDCQEGHILKMFPSTWYV"]

for i in test_sequences:
  print(extract_feature_sequences(i))
```
