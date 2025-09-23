## Data Preparation: Building Training and Benchmarking Datasets

Once the preliminary data are collected, the dataset needs to be divided into two distinct subsets:

- **Training set**  
  Used to train the models, optimize hyperparameters, and perform cross-validation experiments.

- **Benchmarking set**  
  Also known as the *holdout dataset*, it is reserved for testing the generalization performance of the models.

---

## Redundancy Reduction

Before splitting the data, it is essential to create a **non-redundant dataset**.  
This involves:

- Controlling **sequence identity** and **alignment coverage**  
- Performing redundancy reduction using clustering tools with **MMSeqs2**  
- Selecting **one representative sequence per cluster** 

Once redundancy has been addressed, the split can safely be performed randomly.

## MMseq2

For the clusterisation procedure the MMseqs2 software (version) was used. MMseqs2 is an open-source software use to cluster large databases of sequences. input file were: negative_dataset.fasta and positive_dataset.fasta. For each run two output files were created. For the negative set: 
- [neg_cluster.tsv](./neg_cluster/neg_cluster.tsv): TSV containing two colums ( ID of each sequence in th input file, ID of the representative sequence indetifying the cluster). 
- [neg_rep_seq.fasta](./neg_cluster/neg_rep_seq.tsv): .fasta file containing all the representative sequences, one for each found cluster.
- [neg_all_seq.fasta](./neg_cluster/neg_all_seq.tsv): .fasta file with all the sequences used. 
  The same output files ( [positive_cluster.tsv](./pos_cluster/pos_cluster.tsv), [positive_rep_seq.fasta](./pos_cluster/pos_rep_seq.tsv), [neg_all_seq.fasta](./pos_cluster/pos_all_seq.tsv ) was obtained using as input *positive_dataset.fasta*. 

---

### Benchmarking Set: Motivation

Cross-validation alone is not sufficient to guarantee an unbiased estimate of generalization performance:

- Hyperparameter tuning through cross-validation and grid search may still introduce **overfitting**.  
- A holdout dataset provides a stronger guarantee of the *never-seen-before* condition.  
- The model tested on the benchmarking set is the one intended for **production** use.  
- During cross-validation, models are trained on slightly different subsets of the training dataset, which may bias results.

Creating a proper holdout dataset is **not trivial** and requires specific criteria to avoid biased results: in protein bioinformatics, **sequence similarity** must be carefully considered.This applies both to **cross-validation splits** and to the **selection of a reliable holdout set**.


