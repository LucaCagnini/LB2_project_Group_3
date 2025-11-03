# **SVM Optimization**

This repository contains the SVM optimization via Bayesian search and provides a performance analysis module to evaluate model quality and 
  interpret false positives (FP) and false negatives (FN). 

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

## ** Performance Analysis **

The script **model_evaluation.ipynb** contains the evaluation procedure that took in account different features fo differentiate our results: 


