## **The vonHeijne method for SP detection** 
This repository contains the implementation of the **Von Heijne method** for signal peptide cleavage site prediction.
The method builds a **Position-Specific Weight Matrix (PSWM)** using experimentally validated protein sequences and compares them against background amino acid frequencies (SwissProt). Pseudocount +1 was used to avoid zero probabilities. 
For the method implementation, the following parameters were considered: 
- Aminoacids Window: [-13, +2] relative to the cleavage site
- Background distribution: SwissProt amino acid frequencies
- PSWM: built from positive examples (proteins with confirmed signal peptides)
- Goal: identify likely cleavage sites by comparing observed amino acid frequencies with the   background model
- 
## **PSWM implementation** 

The script *create_pswm.ipynb* was produced to build a Position-Specific Weight Matrix (PSWM) from a training dataset of proteins with annotated signal peptides in the *train_bench.tsv* file. 
The input DataFrame used must contain sequences and a SPEnd index for the cleavage site.
