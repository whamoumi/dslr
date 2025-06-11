import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np  

if __name__ == "__main__":
    df = pd.read_csv("./dataset_train.csv")
    name = []
    for attribute in df.columns:
        if (df[attribute].dtype != type(object)):
            name.append(df[attribute].name)
    name = name[1:]
    i = 0
    while (i < len(name)):
        j = i + 1
        while (j < len(name)):
            plt.scatter(df[name[i]], df[name[j]], color = "blue")
            plt.xlabel(name[i])
            plt.ylabel(name[j])
            plt.title("Scatter plot of " + name[i] + " vs " + name[j])
            plt.show()
            j +=1
        i += 1
# What are the two features that are similar ? Astronomy and Defense Against the dark arts
            
