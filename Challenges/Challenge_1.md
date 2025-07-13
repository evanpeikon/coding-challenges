### Problem
You've just received RNA-seq count data and need to perform initial quality control before differential expression analysis. Given a count matrix named ```count_matrix```, create a function that calculates basic QC metrics for your data. 

### Requirements
Your function should take the ```count_matrix``` as an argument and return a dictionary with the following QC metrics:
- ```total_reads_per_sample```: Series with total read counts per sample
- ```genes_detected_per_sample```: Series with number of genes with >0 counts per sample
- ```samples_per_gene```: Series with number of samples where each gene is detected (>0)
- ```low_count_genes```: List of gene IDs with <10 total counts across all samples
- ```summary_stats```: Dict with overall metrics (total_genes, total_samples, median_counts_per_sample)

### Data     
Below you'll find a codeblock used to generate synthetic data for this problem:
```python
import pandas as pd
import numpy as np
np.random.seed(42)
n_genes, n_samples = 1000, 8
gene_ids = [f"GENE_{i:04d}" for i in range(n_genes)]
sample_ids = [f"Sample_{i+1}" for i in range(n_samples)]
counts = np.random.negative_binomial(n=5, p=0.3, size=(n_genes, n_samples))
counts[:50] = np.random.poisson(2, size=(50, n_samples))
counts[-50:] = np.random.negative_binomial(n=20, p=0.2, size=(50, n_samples))
count_matrix = pd.DataFrame(counts, index=gene_ids, columns=sample_ids)
```

### Sample Solution
```python
def rna_seq_qc(count_matrix):
  #Calculate total total_reads_per_sample
  total_reads_per_sample_list = []
  for i in range(0,len(count_matrix.columns)):
    total_reads = count_matrix.iloc[:,i].sum()
    total_reads_per_sample_list.append(total_reads)
  total_reads_per_sample = pd.Series(total_reads_per_sample_list, index=count_matrix.columns)

  # Find genes with <10 total counts across all samples
  genes_detected_per_sample_list = []
  for i in range(0,len(count_matrix.columns)):
    gene_tally = 0
    for x in range(0,len(count_matrix)):
      if count_matrix.iloc[x,i]>0:
        gene_tally += 1
    genes_detected_per_sample_list.append(gene_tally)
  genes_detected_per_sample = pd.Series(genes_detected_per_sample_list, index=count_matrix.columns)

  # Calculate samples per gene
  samples_per_gene_list = []
  for i in range(0,len(count_matrix)):
    sample_tally = 0
    for x in range(0,len(count_matrix.columns)):
      if count_matrix.iloc[i,x]>0:
        sample_tally +=1
    samples_per_gene_list.append(sample_tally)
  samples_per_gene = pd.Series(samples_per_gene_list, index=count_matrix.index)

  # find low count genes
  low_count_genes = []
  for i in range(0,len(count_matrix)):
    low_count_tally = 0
    for x in range(0,len(count_matrix.columns)):
      if count_matrix.iloc[i,x]<10:
        low_count_tally +=1
    if low_count_tally == len(count_matrix.columns):
      low_count_genes.append(count_matrix.index[i])

  # calculate summary stats
  total_genes = len(count_matrix)
  total_samples = len(count_matrix.columns)
  median_counts_per_sample = []
  for i in range(0,len(count_matrix.columns)):
    median_val = count_matrix.iloc[:,i].median()
    median_counts_per_sample.append(median_val)
  summary_stats = {'total_genes':total_genes, 'total_samples':total_samples, 'median_counts_per_sample':median_counts_per_sample}

  # Create QC dictionary and return dictionary
  qc_dictionary = {'total_reads_per_sample':total_reads_per_sample, 'genes_detected_per_sample':genes_detected_per_sample,
                   'samples_per_gene':samples_per_gene, 'low_count_genes':low_count_genes, 'summary_stats':summary_stats}
  return qc_dictionary

qc_metrics = rna_seq_qc(count_matrix)
print(qc_metrics)
```
```
{'total_reads_per_sample': Sample_1    14124
Sample_2    14611
Sample_3    14320
Sample_4    14590
Sample_5    14621
Sample_6    14658
Sample_7    14135
Sample_8    14473
dtype: int64, 'genes_detected_per_sample': Sample_1    995
Sample_2    989
Sample_3    994
Sample_4    994
Sample_5    991
Sample_6    986
Sample_7    991
Sample_8    990
dtype: int64, 'samples_per_gene': GENE_0000    7
GENE_0001    7
GENE_0002    7
GENE_0003    6
GENE_0004    8
            ..
GENE_0995    8
GENE_0996    8
GENE_0997    8
GENE_0998    8
GENE_0999    8
Length: 1000, dtype: int64, 'low_count_genes': ['GENE_0000', 'GENE_0001', 'GENE_0002', 'GENE_0003', 'GENE_0004', 'GENE_0005', 'GENE_0006', 'GENE_0007', 'GENE_0008', 'GENE_0009', 'GENE_0010', 'GENE_0011', 'GENE_0012', 'GENE_0013', 'GENE_0014', 'GENE_0015', 'GENE_0016', 'GENE_0017', 'GENE_0018', 'GENE_0019', 'GENE_0020', 'GENE_0021', 'GENE_0022', 'GENE_0023', 'GENE_0024', 'GENE_0025', 'GENE_0026', 'GENE_0027', 'GENE_0028', 'GENE_0029', 'GENE_0030', 'GENE_0031', 'GENE_0032', 'GENE_0033', 'GENE_0034', 'GENE_0035', 'GENE_0036', 'GENE_0037', 'GENE_0038', 'GENE_0039', 'GENE_0040', 'GENE_0041', 'GENE_0042', 'GENE_0043', 'GENE_0044', 'GENE_0045', 'GENE_0046', 'GENE_0047', 'GENE_0048', 'GENE_0049', 'GENE_0823'], 'summary_stats': {'total_genes': 1000, 'total_samples': 8, 'median_counts_per_sample': [10.5, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0]}}
```
