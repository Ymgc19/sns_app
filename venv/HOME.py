import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
# plt.use('Agg')  # バックエンドをAggに設定
import japanize_matplotlib

st.set_page_config(
    page_title="Full Screen App",
    layout="wide", 
    initial_sidebar_state="auto",
    page_icon=":paintbrush:"
)


custom_colors = ["aquamarine", "mediumpurple", "yellow", "orange", "firebrick", "forestgreen",
                 "hotpink", "white", "greenyellow", "deeppink", "cyan"]

# ちょっとした画像を出す
image = Image.open("pics/万行の田園風景.jpeg")
st.image(image)

st.title("DISCUTTER")
st.text("読んだ論文を共有して議論しよう！")


col1, col2 = st.columns(2)

#表を作成するためのデータフレーム
data = pd.DataFrame(columns=["読んだ日", "タイトル", "著者名", "出版年", "キーワード", "分野", "概要", "手法", "評価"])


with col1:    
    st.subheader("論文情報を入力（全項目必須入力）")

    with st.form(key = "LET'S PLANT"):
        name = st.text_input("名前")
        date = st.date_input("読んだ日", datetime.date.today())
        title = st.text_input('タイトル')
        author = st.text_input('著者名')
        year = st.text_input('出版年')
        keywords = st.text_input('キーワード')
        # 複数登録しても一個のデータフレームにまとまるようにしたい
        options = ["GIS", "経済", "農業", "環境", "階層", "教育", "家族", "政治", "思想", "心理", "統計", "メディア", "その他"]
        field = st.multiselect('分野', options)
        summary = st.text_input('概要')
        method = st.text_input('用いられた手法')
        recommend = st.slider("論文の評価", min_value=0, max_value=100)



    # ボタン
        submit_btn = st.form_submit_button("SUBMIT")
#        cancel_btn = st.form_submit_button("キャンセル")
        if submit_btn:
            data = pd.read_csv("論文データ.csv")
            data = data.append({"名前": name, "読んだ日": date, "タイトル": title, "著者名": author, "出版年": year, "キーワード": keywords,
                                "分野": field, "概要": summary, "手法": method, "評価": recommend},
                                ignore_index=True)
            data.to_csv("論文データ.csv", index=False)

            #書き込んだ情報に合わせてPythonファイルを作成
            #データフレーム作成
            df = pd.DataFrame({
                "名前": name,
                "読んだ日": date,
                "タイトル": title,
                "著者名": author,
                "出版年": year,
                "キーワード": keywords,
                "分野": field,
                "概要": summary,
                "手法": method,
                "評価": recommend
            })
            df.to_csv(f"venv/datas/{author}（{year}）.csv")


            #コメント用ファイル作成
            column_names = ['名前', 'コメント']
            emp_data = {col: [] for col in column_names}
            empty_df = pd.DataFrame(emp_data)
            empty_df.to_csv(f"venv/comments/com_{author}（{year}）- {title}.csv")


            #ファイル作成
            filename = f"venv/pages/{author}（{year}）.py"
            filename2 = f"venv/comments/{author}（{year}）.csv"
            with open(filename, "w") as file:
                file.write("import streamlit as st\n")
                file.write("import pandas as pd\n")
                file.write("import os\n")
                file.write("from PIL import Image\n")
                # 画面を分けるために画像挿入
                file.write("kitchen = Image.open('pics/台所.jpeg')\n")
                file.write("st.image(kitchen)\n")
                file.write('path = __file__\n')
                file.write("path = str(os.path.splitext(os.path.basename(path))[0])\n")
                file.write("cast1 = 'venv/datas/'\n")
                file.write("cast2 = '.csv'\n")
                file.write("cast3 = 'venv/comments/com_'\n")
                file.write("path1 = cast1 + path + cast2\n")
                file.write("path2 = cast3 + path + cast2\n")
                # 論文データの詳細表示
                file.write("st.subheader('論文の詳細情報')\n")
                file.write("df = pd.read_csv(path1)\n")
                file.write("df = df.drop(df.columns[0], axis=1)\n")
                file.write("df = df.T\n")
                file.write("df = df.drop(df.index[0])\n")
                file.write("st.table(df)\n") #概要以外のデータを表示させる




                # 論文に関する質問フォーム（名前入力）
                # 他の人が星を与える
                file.write("st.subheader('論文に関する議論')\n")
                file.write("st.text('最新のコメントを読み込むにはブラウザをリロードしてください')\n")
                file.write("cdf = pd.read_csv(path2)\n")
                # コメントのcsvから最後の2列だけを取り出す．
                file.write("cdf = cdf.iloc[:, -2:]\n")
                file.write("st.table(cdf)\n")
                # 入力フォーム
                file.write("with st.form(key = '論文情報の入力'):\n")
                file.write("    name = st.text_input('名前')\n")
                file.write("    comment = st.text_input('コメント')\n")    
                file.write("    submit_btn = st.form_submit_button('送信')\n")
                file.write("    if submit_btn:\n")
                file.write("        st.write('コメントを送信しました！')\n")
                file.write("        to_add = pd.read_csv(path2)\n")
                file.write("        to_add = to_add.append({'名前': name, 'コメント': comment}, ignore_index = True)\n")
                file.write("        to_add.to_csv(path2)\n")


st.text("論文情報を変更したい場合は，著者名と出版年を同じにして再度情報を登録してください．")

with col2:
    st.subheader("最近投稿された論文情報")
    #データテーブルの表示
    data = pd.read_csv("論文データ.csv")
    data_fixed = data[["名前", "読んだ日", "[{'タイトル'}](https://www.google.com)", "著者名", "評価"]]
    # データが10行以上になったら，直近の10個だけを表示させたい．
    if len(data_fixed) >= 6:
        st.table(data_fixed.tail(5))
    else:
        st.table(data_fixed)

# 投稿者の割合円グラフ
    st.subheader("論文投稿者内訳")
    data_gb = data.groupby('名前').size()
    grouped_df = data_gb.reset_index(name='count') # データフレーム化
    grouped_df = grouped_df.sort_values(by='count', ascending=False)
    fig, ax = plt.subplots()
    ax.pie(grouped_df['count'], labels=grouped_df['名前'], autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.axis('equal')  # アスペクト比を等しくする（円に近づける）
    st.pyplot(fig)    # Streamlit上でグラフを表示

# 分野割合の内訳
# リストを分解して，出現回数で円グラフを作りたい
    st.subheader("分野内訳")
    data_gb = data.groupby('分野').size()
    grouped_df = data_gb.reset_index(name='count') # データフレーム化
    grouped_df = grouped_df.sort_values(by='count', ascending=False)
    fig, ax = plt.subplots()
    ax.pie(grouped_df['count'], labels=grouped_df['分野'], autopct='%1.1f%%', startangle=90, colors=custom_colors)
    ax.axis('equal')  # アスペクト比を等しくする（円に近づける）
    st.pyplot(fig)    # Streamlit上でグラフを表示


