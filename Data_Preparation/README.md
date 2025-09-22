## Building Training and Benchmarking Datasets

Once the preliminary data are collected, the dataset needs to be divided into two distinct subsets:

- **Training set**  
  Used to train the models, optimize hyperparameters, and perform cross-validation experiments.

- **Benchmarking set**  
  Also known as the *holdout dataset*, it is reserved for testing the generalization performance of the models.

---

### Redundancy Reduction

Before splitting the data, it is essential to create a **non-redundant dataset**.  
This involves:

- Controlling **sequence identity** and **alignment coverage**  
- Performing redundancy reduction using clustering tools such as **MMSeqs2**  
- Selecting **one representative sequence per cluster**

Once redundancy has been addressed, the split can safely be performed randomly.

---

### Benchmarking Set: Motivation

Cross-validation alone is not sufficient to guarantee an unbiased estimate of generalization performance:

- Hyperparameter tuning through cross-validation and grid search may still introduce **overfitting**.  
- A holdout dataset provides a stronger guarantee of the *never-seen-before* condition.  
- The model tested on the benchmarking set is the one intended for **production** use.  
- During cross-validation, models are trained on slightly different subsets of the training dataset, which may bias results.

Creating a proper holdout dataset is **not trivial** and requires specific criteria to avoid biased results: in protein bioinformatics, **sequence similarity** must be carefully considered.This applies both to **cross-validation splits** and to the **selection of a reliable holdout set**.

