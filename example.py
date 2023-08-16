import pandas as pd

df = pd.read_csv("論文データ.csv")

print(df.at[0, "名前"])