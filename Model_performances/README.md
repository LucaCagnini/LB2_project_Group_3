# **SVM Optimization**

SVM optimization was developed  via Bayesian search and provides a performance analysis module to evaluate model quality and interpret false positives (FP) and false negatives (FN). 

---

## **Bayesian search optimization**
The script **hyperparameter_tuning.ipynb** contains the implementation of the Bayesian search using an RBF SVM using BayesSearchCV. It reports best hyperparameters and MCC scores. Bayesian optimization uses past evaluations to predict where the best hyperparameters probably are, wasting  less time testing bad configurations. 

### **Results**
The table below shows the results of the hyperparameter tuining procedure. The MCC obtained suggest a better performance of the SVM method in respect to the classical approach of the VonHeije method. 

  
| Hyperparameter | Value | Description |
|----------------|-------|-------------|
| `svm__C` | **0.6758** | Regularization parameter controlling the trade-off between margin size and classification error |
| `svm__gamma` | **0.0350** | RBF kernel coefficient defining the influence of single training examples |
| `svm__kernel` | **rbf** | Kernel type used by the SVM (Radial Basis Function) |
| **Best MCC (validation)** | **0.8569** | Matthews Correlation Coefficient obtained during cross-validation |

---

## **Performance Analysis**

The script **model_evaluation.ipynb** contains the evaluation procedure that took in account different features fo differentiate our results.
During the model evaluation phase, several in-depth analyses were conducted to better understand the model’s behavior and error patterns, focusing on False Negatives (FN) and False Positives (FP).
These analyses aim to identify biological or compositional reasons behind the misclassifications and assess the robustness of the feature set.

---

## **False Negative (FN) Analysis**

- **Taxonomy distribution:**
Pie charts comparing the taxonomy of FN, FP, and total predictions.
→ In particular, we expect to observe many FP among plant sequences due to the presence of transit peptides.

- **Amino acid frequency distribution:**
Histogram comparing the amino acid composition of FN versus True Positives (TP).

- **Signal peptide composition:**
Comparison between the amino acid composition of signal peptides in TP versus FN sequences.

- **Signal peptide length distribution:** 
Length comparison of signal peptides between TP and FN groups.

- **Hydrophobicity distribution:**
Comparison of average hydrophobicity between TP and FN sequences.

- **Feature-wise distributions:**
In general, distributions were generated for all the most informative features to detect systematic differences between FN and TP samples.

---

## **False Positive (FP) Analysis**

- **FPR on transmembrane proteins:**
Calculation of the false positive rate (FPR) specifically for transmembrane domain proteins.

- **FPR with Von Heijne features:**
Same FPR calculation applied to models including the Von Heijne feature set, to evaluate its impact on transmembrane-related misclassifications.


