import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np  

if __name__ == "__main__":
    df = pd.read_csv("./dataset_train.csv")
    for attribute in df.columns:
        if (df[attribute].dtype != type(object)):
            dataset = df[attribute].dropna()
            plt.hist(dataset, bins=df[attribute].dropna().size)
            plt.title(df[attribute].name) 
            plt.show()

#Which Hogwarts course has a homogeneous score distribution between all four houses? Care of Magical creature on peut aussi le checker avec l'ecart type 