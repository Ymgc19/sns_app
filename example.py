import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


# ダミーデータを作成
data = {'カテゴリ': ['ねこ', 'B', 'ねこ', 'C', 'B', 'C', 'ねこ', 'C'],
        '値': [10, 20, 15, 25, 30, 10, 5, 40]}
df = pd.DataFrame(data)

# グループごとのデータ数を数える
grouped = df.groupby('カテゴリ').size()

# 結果を表示
print(type(grouped))

grouped_df = grouped.reset_index(name='カウント')
print(grouped_df)

fig, ax = plt.subplots()
ax.pie(grouped_df['カウント'], labels=grouped_df['カテゴリ'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # アスペクト比を等しくする（円に近づける）
plt.show()
