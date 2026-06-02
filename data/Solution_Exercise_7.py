import pandas as pd

iris = pd.read_csv("iris.csv")
with pd.ExcelWriter("iris2.xlsx") as writer:
    for variety_name, variety_df in iris.groupby("variety"):
        variety_df.to_excel(writer, sheet_name=variety_name)