import subprocess
import Bio
import shlex

subprocess.run(shlex.split("mmseqs easy-cluster /home/um13/lab2_project/LB2_project_Group_3/Data_Collection/negative_dataset.fasta /home/um13/lab2_project/LB2_project_Group_3/Data_Collection/neg_cluster/neg tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1"), stdout=subprocess.DEVNULL)
subprocess.run(shlex.split("mmseqs easy-cluster /home/um13/lab2_project/LB2_project_Group_3/Data_Collection/positive_dataset.fasta /home/um13/lab2_project/LB2_project_Group_3/Data_Collection/pos_cluster/pos tmp --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1"), stdout=subprocess.DEVNULL)

