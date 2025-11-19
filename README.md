
# **A Cross-Model Comparison of Secretiory Signal Peptide Prediction Techiques: Von Hijne, SVM, NN**

## **Laboratory of Bioinformatics 2, A.Y. 2025/2026**

Cagnini Luca,  Centenaro Marco,  Cuscunà Marco,  Mariano Marina,  Timelli Giacomo
Bioinformatics, FABIT, Alma Mater Studiorum – University of Bologna, Italy

---

## **Abstract**
This repository contains files and codes of the project for the **Laboratory of Bioinformatics 2 course**. The aim of the project was to analyze and compare three different **computational approaches** for the prediction of **Signal peptides (SPs)**. 
Signal peptides (SPs) are short, essential sequences that guide proteins to their
correct cellular locations, significantly influencing protein functionality and various cellular processes.
While numerous computational methods exist for SP prediction, machine learning techniques,
particularly **Support Vector Machines (SVM)** and **Neural Networks**, have shown substantial
improvements over traditional methods like the **Von Heijne algorithm**. 
**Results:** The aim of the study is to confirm this hypothesis developing a correct workflow that higlights significant improvement on protein predictions of the firs two methods previously mentioned over the latter.  

---
# Table of Contents

1. [Data Collection](#data-collection)  
2. [Data_Preparation](#data-preparation)  
3. [Data_analysis](#data-analysis)  
4. [Von Heijne](#von-heijne)  
5. [SVM:Feature Selection](#svm:feature-selection)  
6. [SVM:Performance evaluation](#performance-evaluation)  
7. [Deep_Learning](#deep-learning)
8.  [Discussion](#discussion)
---

# Data Collection

Repository: [Data_collection](./Data_Collection)

The first step of the analysis was to retrieve relevant datasets of protein sequences from UniProtKB. Two proteins datasets were created, a positive one containing the signal peptide, and a negative one with all the others. This approach included two step:
- Web interface approach: advance query search using web interface. 
- API approach: APi call to the UniProtKB/swiss-Prot database.


 ## Results 

Results were saved in two .tsv files: [positive_dataset.tsv], (Data_Collection/positive_dataset.tsv) [negative_dataset.tsv](/Data_collection/negative_dataset.tsv). 

 | Positive Set | Negative Set | Negative with HD | 
|--------------|--------------|------------------|
|  2932        |    20615     |      1384        |

---

# Data Preparation
Repository: [Data_Preparation](./Data_Preparation)

This step included the preprocessing pipeline datasets for cross-validation and benchmarking, including:
- training and benchmark set creation: splitting positive and negative datasets into two subsets
- redundancy reduction: performend using the MMseqs2 clustering tool

## Results 

Results of our analysis were saved on the file [train_bench.tsv](./Data_Preparation/train_bench.tsv). 

|       Dataset          |        Negatives        |     Positives      |  
|-------------------------|-------------------------|-------------------|
|  Training Sets (total)  |          7147           |       874         |  
| Benchmark Set           |          1787           |       219         |
| Total                   |          8934           |       1093        |


---

# Data Analysis
Repository: [Data-analysis](./Data_Analysis)

An exploratory statistical analysis of the datasets was essential to asses adequacy of the datasets for our porpouse, aimed to confirm dataset quality. 
- Detect dataset **biases** (length, amino acid composition, taxonomy).
- Assess whether sequence properties are **informative features** for classification tasks.
- Evaluate differences between **training** and **benchmarking** datasets.
- gain an insight about data quality across datasets (benchmark/training).

## Results
Resulting plot were saved on three folders:
- [SequenceLogo](/Data_Analysis/SequenceLogo) Contains sequence logo visualizations representing conserved regions and amino acid preferences across datasets.
- [Sequence_lengths_comparison](/Data_Analysis/Sequence_lengths_comparison) Includes analyses and plots comparing sequence length distributions between datasets.
- [Taxonomy_classification](/Data_Analysis/Taxonomy_classification) Provides taxonomic classification summaries, exploring the distribution of sequences across taxonomic groups. 

---

# Von Heijne
Repository: [von_Heijne](./vonHeijne)

Von Heijne’s algorithm was developed by Gunnar von Heijne in the 1980s–1990s, often used in combination with experimental data to analyze protein targeting. Implementation involved the creation of a PSWM (position specific weight metric combined with a 5-fold cross validation method, using appropirate measures for testing our analysis. 

## Results 
After cross-validation method, a mean value of each metric was calculated and it is shown below. 

 | Metric      | Mean ± Std  |
|------------|-------------|
| MCC        | 0.663 ± 0.016 |
| Precision  | 0.934 ± 0.003 |
| Accuracy   | 0.691 ± 0.014 |
| Sensitivity| 0.711 ± 0.029 |

---

# SVM: Feature Selection 
Repository: [Feature_Selection](./Feature_Selection)

The SVM (support Vector Machine) algorithm was trained using a Feature extraction adn selection procedure, taking into account several characteristics of the proteins dataset. It was implemented using Random Forest and SVM training optimized by 5 fold cross validation. 
Results show strong and consistent predictive performance, with average MCC scores between 0.84 and 0.88 across all folds.

## SVM: Performance Summary

| Fold | Best k | Validation MCC | Test MCC |
|------|--------:|----------------:|----------:|
| 1 | 27 | 0.868 | 0.825 |
| 2 | 28 | 0.877 | 0.862 |
| 3 | 13 | 0.839 | 0.854 |
| 4 | 11 | 0.857 | 0.798 |
| 5 | 35 | 0.845 | 0.883 |

**Average Test MCC:** ≈ **0.84–0.88**

# Performance Evaluation
[Performance_evaluation](./performance_SVM)

Performance evaluation procedure consisted into a hyperparameter tuning procedure for the SVM algorithm. Classical performance measures (ex, MCC) were employed. In addition, a strict analysis of the False Positive and False Negative results was developed, in order to aknowledge possible patterns in the error detection of the model. 

## Performance Summary 

 | Metod     |   MCC  |
|------------|--------|
| VonHeijne  | 0.688  |
| SVM        | 0.808  |
# Discussion
Discuss and report results

# Contacts
- Giacomo Timelli - giacomo.timelli@studio.unibo.it
- Luca Cagnini - luca.cagnini@studio.unibo.it
- Marco Centenaro - marco.centenaro@studio.unibo.it
- Marco Cuscunà - marco.cuscuna@studio.unibo.it
- Marina Mariano - marina.mariano@studio.unibo.it

