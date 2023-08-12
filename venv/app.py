import streamlit as st
import datetime
import pandas as pd
from PIL import Image
import glob

st.set_page_config(
    page_title="Full Screen App",
    layout="wide", 
    initial_sidebar_state="auto" 
)


st.title("論文共有")
st.text("東北大学　文学研究科　計算人文社会学　YMGC")


col1, col2 = st.columns(2)

#表を作成するためのデータフレーム
data = pd.DataFrame(columns=["読んだ日", "タイトル", "著者名", "出版年", "キーワード", "分野", "概要", "手法", "評価"])


with col1:    
    st.subheader("論文情報の追加")

    with st.form(key = "論文情報の入力"):
        date = st.date_input("読んだ日", datetime.date(2023, 8, 12))
        title = st.text_input('タイトル')
        author = st.text_input('著者名')
        year = st.text_input('出版年')
        keywords = st.text_input('キーワード')
        options = ["GIS", "経済", "農業", "環境", "階層", "教育", "家族", "政治", "思想", "心理", "統計", "メディア", "その他"]
        field = st.multiselect('分野（複数選択可）', options)
        summary = st.text_input('概要')
        method = st.text_input('用いられた手法')
        recommend = st.slider("論文の評価", min_value=0, max_value=100)



    # ボタン
        submit_btn = st.form_submit_button("登録")
        cancel_btn = st.form_submit_button("キャンセル")
        if submit_btn:
            # 書き込んだ情報に合わせてPythonファイルを作成
            #データフレーム作成
            df = pd.DataFrame({
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
            #ファイル作成
            filename = f"venv/pages/{author}（{year}）.py"
            with open(filename, "w") as file:
                file.write("import streamlit as st")
                # ここでファイルを読み込むやつを作成
                path = 'venv/datas/f"{author}（{year}".csv'
                file.write(df = path)
                file.write("st.table(df)")
            




with col2:
    st.subheader("読んだ論文の情報")
    #データテーブルの表示
    data = pd.read_csv("論文データ.csv")
    data_except_summary = data[["読んだ日", "タイトル", "著者名", "キーワード", "評価"]]
    st.table(data_except_summary)

    #読んだ日付によってヒストグラム的なものを作成
