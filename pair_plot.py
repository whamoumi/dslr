import pandas as pd 
from matplotlib import pyplot as plt  
import seaborn as sns

if __name__ == "__main__":
    df = pd.read_csv("./dataset_train.csv")
    sns.pairplot(df[df.columns[6:]])  # 'species' colore selon la classe
    plt.show()