import streamlit as st
import pandas as pd
import os
path = __file__
path = str(os.path.splitext(os.path.basename(path))[0])
cast1 = 'venv/datas/'
cast2 = '.csv'
path = cast1 + path + cast2
df = pd.read_csv(path)
df = df.drop(df.columns[0], axis=1)
st.table(df)
comments = []
st.subheader('論文に関する議論')
for _ in range(len(comments)):
    st.write(comments[_])
comment = st.text_input('コメント')
if st.button('送信'):
    comments.append(str(comment))