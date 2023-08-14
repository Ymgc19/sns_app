import streamlit as st
import pandas as pd
import os
from PIL import Image
kitchen = Image.open('pics/台所.jpeg')
st.image(kitchen)
path = __file__
path = str(os.path.splitext(os.path.basename(path))[0])
cast1 = 'venv/datas/'
cast2 = '.csv'
cast3 = 'venv/comments/com_'
path1 = cast1 + path + cast2
path2 = cast3 + path + cast2
st.subheader('論文の詳細情報')
df = pd.read_csv(path1)
df = df.drop(df.columns[0], axis=1)
df = df.T
df = df.drop(df.index[0])
st.table(df)
st.subheader('論文に関する議論')
st.text('最新のコメントを読み込むにはブラウザをリロードしてください')
cdf = pd.read_csv(path2)
cdf = cdf.iloc[:, -2:]
st.table(cdf)
with st.form(key = '論文情報の入力'):
    name = st.text_input('名前')
    comment = st.text_input('コメント')
    submit_btn = st.form_submit_button('送信')
    if submit_btn:
        st.write('コメントを送信しました！')
        to_add = pd.read_csv(path2)
        to_add = to_add.append({'名前': name, 'コメント': comment}, ignore_index = True)
        to_add.to_csv(path2)
