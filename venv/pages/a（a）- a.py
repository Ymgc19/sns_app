import datetime
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
st.table(df)
koumoku = ['名前', '読んだ日', 'タイトル', '著者名', '出版年', 'キーワード', '分野', '概要', '手法', '評価']
options = ['GIS', '経済', '農業', '環境', '階層', '教育', '家族', '政治', '思想', '心理', '統計', 'メディア', 'その他']
btn = st.button('EDIT')
if btn:
    edit_df = pd.read_csv(path1)
    selected_koumoku = st.selectbox('編集する項目', koumoku)
    kakutei = st.button('CONFIRM')
    if kakutei:
        st.write('選択する項目:', selected_koumoku)
        if selected_koumoku == '分野':
            henkou = st.multiselect('分野', options)
        elif selected_koumoku == '読んだ日':
            henkou = st.date_input('変更後', datetime.date.today())
        elif selected_koumoku == '評価':
            henkou = st.slider('論文の評価', min_value=0, max_value=100)
        else:
            henkou = st.text_input('変更後の内容を入力')
        edit_df.at[1, f'{selected_koumoku}'] = henkou
        edit_btn = st.button('SUBMIT')
        if edit_btn:
            edit_df.to_csv(path1)
            st.text('変更を受け取りました！')
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
