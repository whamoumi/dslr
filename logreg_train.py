import pandas as pd 
import numpy as np 
import sys 
import errno


def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

if __name__ == "__main__":

    try:
        if(len(sys.argv) != 2):
            raise ValueError("Not the right number of argument")
        df = pd.read_csv(sys.argv[1])

        feature_column_names = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
        # normalisation des données
        df.fillna(0, inplace=True)
        for column in df.columns[feature_column_names]:
            column_mean = df[column].mean()
            column_std = df[column].std()
            df[column] = (df[column] - column_mean) / column_std
        K = 4 # nombre de classificateur a trouver

        # entrainement pour le classificateur Gryffindor    
        
        df['Erreur'] = 0.0
        
        alpha = 0.01
        
        m = len(df)

        data = {}
        for classificateur in range(0, K):
            df['Etiquettes'] = 0
            if (classificateur == 0):
                df['Etiquettes'] = (df["Hogwarts House"] == "Gryffindor").astype(int)
            elif (classificateur == 1):
                df['Etiquettes'] = (df["Hogwarts House"] == "Ravenclaw").astype(int)
            elif (classificateur == 2):
                df['Etiquettes'] = (df["Hogwarts House"] == "Slytherin").astype(int)
            elif (classificateur == 3):
                df['Etiquettes'] = (df["Hogwarts House"] == "Hufflepuff").astype(int)
            
            weight = np.random.rand(13) * 0.01    
            X = df[feature_column_names].values
            Y_true = df["Etiquettes"].values

            biais = 0.01
            
            for epoch in range(1000): 

                z_score = np.dot(X, weight) + biais
                y_predicted_proba = sigmoid(z_score)
                errors = y_predicted_proba - Y_true


                gradient_weights = np.dot(X.T, errors) / m
                gradient_bias = np.mean(errors)

                weight = weight - (alpha * gradient_weights)
                biais = biais - (alpha * gradient_bias)
                 
            data["weight" + str(classificateur)] = weight
            data["biais" + str(classificateur)] = biais
        dataweigth = pd.DataFrame(data)
        dataweigth.to_csv("weight.csv", index=False)
    except ValueError as e :
        print(e)
    except OSError as e :
        if e.errno == 2:
            print(e.args[1])

        

    
