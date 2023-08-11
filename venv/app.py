import streamlit as st

st.title("論文共有用")
st.caption("東北大学の文学研究科所属のカエルがお送りします．")
st.subheader("自己紹介")
st.text("このサイトでは，読んだ論文の概要や感想などについて述べていきます．")

title = st.text_input('タイトル')

submit_btn = st.bottun("送信")
cancel_btn = st.bottun("キャンセル")

print(f'submit_btn: {submit_btn}')
print(f'cancel_btn: {cancel_btn}')