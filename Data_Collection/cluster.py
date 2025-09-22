import subprocess
import Bio
import shlex

subprocess.run(shlex.split("mmseqs easy-cluster /home/um13/lab2_project/LB2_project_Group_3/Data_Collection/neg_cluster/negative_dataset.fasta neg_cluster tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1"))
subprocess.run(shlex.split("mmseqs easy-cluster /home/um13/lab2_project/LB2_project_Group_3/Data_Collection/pos_cluster/positive_dataset.fasta pos_cluster tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1"))

