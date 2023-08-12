import streamlit as st
import datetime
import pandas as pd

st.title("論文共有")
st.text("東北大学　文学研究科　計算人文社会学　山口侑平")

col1, col2 = st.columns(2)

with col1:
    st.subheader("論文情報の追加")
    data = pd.DataFrame(columns=["読んだ日", "タイトル", "著者名", "キーワード", "分野", "概要", "手法", "評価"])

    with st.form(key = "論文情報の入力"):
        date = st.date_input("読んだ日", datetime.date(2023, 8, 12))
        title = st.text_input('タイトル')
        author = st.text_input('著者名')
        keywords = st.text_input('キーワード')
        options = ["GIS", "経済", "農業", "環境", "階層", "教育", "家族", "政治", "思想", "心理", "統計", "メディア", "その他"]
        field = st.multiselect('分野（複数選択可）', options)
        summary = st.text_input('概要')
        method = st.text_input('用いられた手法')
        recommend = st.slider("論文の評価", min_value=0, max_value=100)



    # ボタン
        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")
        if submit_btn:
            st.text("論文情報を登録しました")
            data = data.append({"読んだ日": date, "タイトル": title, "著者名": author, "キーワード": keywords, "分野": field, "概要": summary, "手法": method, "評価": recommend}, ignore_index=True)

with col2:
    st.table(data)