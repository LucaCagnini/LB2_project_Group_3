## Feature Extraction and selection

This repository provides the **feature extration and selection workflow** used in this project, integrating:
- **Feature extraction** from amino acid sequences  
- **5-fold cross-validation** for model evaluation  
- **Feature selection** using Random Forest Gini importance  
- **SVM training** optimized via grid search on validation performance  

---

###  1. Feature Definition & Dataset Preparation

1. The dataset (`train_bench.tsv`) is divided into **5 cross-validation folds** (`Set = 1–5`).
2. For each iteration:
   - **Training set:** 3 folds  
   - **Validation set:** next fold  
   - **Testing set:** current fold  
3. Custom biochemical and positional features are computed using:
   - `get_pswm()` → builds Position-Specific Weight Matrices (PSWM)  
   - `get_all_features()` → extracts sequence-level physicochemical descriptors, chosen among a series of features of our proteins
     considering a wide range of elements. 
4. Each split is saved as `.npz` files containing:
   - `matrix` → feature matrix (samples × features)
   - `target` → binary target vector (1 = Positive, 0 = Negative)

---
###  2. Feature Selection & Model Training

This phase combines **Random Forest feature ranking** with **SVM optimization**.

#### Step 1 — Feature Ranking
- A `RandomForestClassifier` (1000 trees) ranks features by **Gini importance**.
- Top-ranked features are incrementally tested to find the most informative subset.

#### Step 2 — SVM Grid Search
- SVM with **RBF kernel** is optimized on a grid:
  - `C ∈ {0.1, 1.0, 10.0, 100.0}`
  - `γ ∈ {"scale", 0.01, 0.1, 1.0}`
- Model performance is evaluated using **Matthews Correlation Coefficient (MCC)**.

#### Step 3 — Feature Subset Evaluation
- The number of top features (`k`) is varied to maximize validation MCC.  
- The best `k` features are then used for the final testing phase.

---

### 3. Performance Summary

| Fold | Best k | Validation MCC | Test MCC |
|------|--------:|----------------:|----------:|
| 1 | 27 | 0.868 | 0.825 |
| 2 | 28 | 0.877 | 0.862 |
| 3 | 13 | 0.839 | 0.854 |
| 4 | 11 | 0.857 | 0.798 |
| 5 | 35 | 0.845 | 0.883 |

**Average Test MCC:** ≈ **0.84–0.88**

---
