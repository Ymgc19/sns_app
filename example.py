import pandas as pd
import os

df = pd.read_csv("venv/datas/山口（2022）- コモンズの現代的課題とその解決.csv")

#print(df.at[0, "名前"])


#path = __file__
#path = str(os.path.splitext(os.path.basename(path))[0])
#print(path)


df["評価"][0] = 1234

print(df["評価"][0])

df.to_csv("venv/datas/a（a）- a.csv")

print(df.dtypes)