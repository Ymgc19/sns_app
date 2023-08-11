import streamlit as st

st.title("論文共有")
st.text("東北大学　文学研究科　計算人文社会学　山口侑平")
st.subheader("ここで論文の情報を入力をします")

title = st.text_input('タイトル')

# ボタン
submit_btn = st.button("送信")
cancel_btn = st.button("キャンセル")

print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')