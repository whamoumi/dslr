import pandas as pd 
import numpy as np 
import sys

def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

if __name__ == "__main__":
    try:
        if(len(sys.argv) != 3):
            raise ValueError("Not the right number of argument")
        df = pd.read_csv(sys.argv[1])
        weightfile = pd.read_csv(sys.argv[2])
        data = {"index": [], "Hogwarts House" : []}
        df.fillna(0, inplace=True)
        feature_column_names = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']
        for column in df.columns[feature_column_names]:
            column_mean = df[column].mean()
            column_std = df[column].std()
            df[column] = (df[column] - column_mean) / column_std

        weight0 = np.array(weightfile["weight0"].to_list())
        weight1 = np.array(weightfile["weight1"].to_list())
        weight2 = np.array(weightfile["weight2"].to_list())
        weight3 = np.array(weightfile["weight0"].to_list())

        biais0 = weightfile["biais0"][0]
        biais1 = weightfile["biais1"][0]
        biais2 = weightfile["biais2"][0]
        biais3 = weightfile["biais3"][0]

        for index, row in df.iterrows():
            Gryffindor = sigmoid(np.dot(weight0,row[feature_column_names].values) + float(biais0))
            Ravenclaw = sigmoid(np.dot(weight1,row[feature_column_names].values) + float(biais1))
            Slytherin = sigmoid(np.dot(weight2,row[feature_column_names].values) + float(biais2))
            Hufflepuff = sigmoid(np.dot(weight3,row[feature_column_names].values) + float(biais3))
            column_position = df.columns.get_loc("Hogwarts House")
            if ( Gryffindor > Ravenclaw and Gryffindor > Slytherin and Gryffindor > Hufflepuff):
                data["index"].append(index)
                data["Hogwarts House"].append("Gryffindor")
            elif ( Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff):
                data["index"].append(index)
                data["Hogwarts House"].append("Ravenclaw")
            elif ( Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff):
                data["index"].append(index)
                data["Hogwarts House"].append("Slytherin")
            elif ( Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin):
                data["index"].append(index)
                data["Hogwarts House"].append("Hufflepuff")
        df_poudlard = pd.DataFrame(data)
        df_poudlard.to_csv("house.csv", index=False)
    except ValueError as e :
        print(e)
    except OSError as e :
        if e.errno == 2:
            print(e.args[1])

        


        
