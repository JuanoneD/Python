
import pandas as pd

def main():
    # # Exer 1
    # df = pd.read_csv("03\Output\BostonHousing.csv",sep=",")
    # print(df.loc[:13,["crim","medv"]])
    df = pd.read_csv("03\Output\Cars93_miss.csv",sep = ",")
    print(df.columns)
    df = df[df["Passengers"]==5]
    df = df.sort_values(by=["MPG.city","Price","Rev.per.mile"],ascending=[False,True,True])
    print(df.loc[:,["Manufacturer","Make","Price","MPG.city","Type","Passengers"]].head(10))

if __name__ == "__main__":
    main()