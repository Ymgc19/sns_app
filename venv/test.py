import streamlit as st
import pandas as pd

# データを保存するための空のDataFrameを作成
data = pd.DataFrame(columns=["名前", "年齢"])

# Streamlitアプリ
st.title("情報登録アプリ")

# 左側のカラム
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("名前を入力してください")

with col2:
    age = st.number_input("年齢を入力してください", min_value=0, max_value=150, value=0, step=1)

if st.button("登録"):
    data = data.append({"名前": name, "年齢": age}, ignore_index=True)

# 登録された情報を表形式で表示
st.write("登録された情報:")
st.dataframe(data)
