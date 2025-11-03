# **SVM Optimization**

This repository contains the SVM optimization via Bayesian search and provides a performance analysis module to evaluate model quality and 
  interpret false positives (FP) and false negatives (FN). 

  ** Bayesian search optimization**
  The script **hyperparameter_tuning.ipynb** contains the implementation of the Bayesian search using an RBF SVM using BayesSearchCV. It reports best hyperparameters and MCC scores. Bayesian optimization uses past evaluations to predict where the best hyperparameters probably are, wasting  less time testing bad configurations. 

  **Results**
