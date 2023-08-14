import pandas as pd

df = pd.read_csv("論文データ.csv")

df = df["読んだ日"]
data_gb = df.groupby('読んだ日').size()

print(data_gb)