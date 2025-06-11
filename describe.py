import pandas as pd 
import sys
def my_min(tab):
    min = tab[0]
    for i in tab:
        if i < min:
            min = i
    return min

def my_max(tab):
    max = tab[0]
    for i in tab:
        if i > max:
            max = i
    return max

def my_sum(tab):
    sum = 0
    for i in tab:
        sum += i
    return sum

def give_std(tab):
    moyenne = my_sum(tab)/ tab.size
    moyenne_ecart = 0
    for element in tab:
        moyenne_ecart += abs(element - moyenne) ** 2
    return (moyenne_ecart / (int(tab.size - 1)))**0.5

#describe attend plusieurs attributs Name feature Count Mean std min 25% 50% 75% Max
if __name__ == "__main__":
    try:
        if(len(sys.argv) != 2):
            raise ValueError("Not the right number of argument")
        df = pd.read_csv(sys.argv[1])
        for attribute in df.columns:
            if (df[attribute].dtype != type(object)):
                if(df[attribute].dropna().size):
                    print("Name:", df[attribute].name)
                    print('Count:',f"{df[attribute].dropna().size}")
                    print('Mean:',f"{my_sum(df[attribute].dropna())/ df[attribute].dropna().size:.6f}")
                    print('Std:', f"{give_std(df[attribute].dropna()):.6f}")
                    print('Min:',f"{my_min(df[attribute].dropna()):.6f}")
                    print('25%:',f"{sorted(df[attribute].dropna())[int(df[attribute].dropna().size / 4)]:.6f}")
                    print('50%:',f"{sorted(df[attribute].dropna())[int(df[attribute].dropna().size / 2)]:.6f}")
                    print('75%:',f"{sorted(df[attribute].dropna())[int(0.75 * (df[attribute].dropna().size - 1))]:.6f}")
                    print('Max:',f"{my_max(df[attribute].dropna()):.6f}")
                    print('Var:', f"{give_std(df[attribute].dropna())**2:.6f}")
                    print()
    except ValueError as e :
        print(e)
    except OSError as e :
        if e.errno == 2:
            print(e.args[1])