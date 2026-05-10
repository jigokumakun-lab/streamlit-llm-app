from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("【提出課題】LLM機能を搭載したWebアプリを開発しよう")
st.write("#### 操作方法")
st.write("質問したい先生を選択し、入力フォームに質問を入力し「実行」ボタンを押してください")


selected_item = st.radio(
    "質問したい先生を選択してください。",
    ["国語の先生", "数学の先生", "英語の先生", "社会の先生","理科の先生"]
)

st.divider()

if selected_item == "数学の先生":
    input_message = st.text_input(label="質問をしてください")
    text_count = len(input_message)

else:
    input_message = st.text_input(label="質問をしてください")
    text_count = len(input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "数学の先生":

        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")