import pandas as pd

# read only the first column
col1 = pd.read_csv("neg_cluster.tsv", sep="\t", header=None, usecols=[0], dtype=str, names=["id"])
col1["id"] = col1["id"].str.strip()  # remove spaces and newline characters

# unique values of the first column (to take the rapresentative ids only one time)
unique_ids = col1["id"].drop_duplicates()

# save to a new file
#print(unique_ids.to_list())

col2=pd.read_csv("negative_dataset.tsv", sep="\t", header=True)
pd.query
    print('yes') # remove spaces and newline characters
