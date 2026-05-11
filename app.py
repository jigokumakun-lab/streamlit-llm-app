import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain import LLMChain
from langchain.agents import load_tools

import os

try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.5,
    openai_api_key=api_key
)

math_tools = load_tools(["llm-math"], llm=llm)

def result_chain(param, system_template):   

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", "{input}")
    ])

    chain = LLMChain(prompt=prompt, llm=llm)

    result = chain.run(param)
    return result


def get_japanese_answer(param):
    system_template = """
    あなたは国語の教師です。
    国語についての質問に対し、解答を提供します。
    """

    result = result_chain(param, system_template)
    return result

def get_english_answer(param):
    system_template = """
    あなたは英語の教師です。
    英語についての質問に対し、解答を提供します。
    """

    result = result_chain(param, system_template)
    return result

def get_social_answer(param):
    system_template = """
    あなたは社会の教師です。
    社会についての質問に対し、解答を提供します。
    """

    result = result_chain(param, system_template)
    return result

def get_science_answer(param):
    system_template = """
    あなたは理科の教師です。
    理科についての質問に対し、解答を提供します。
    """

    result = result_chain(param, system_template)
    return result



st.title("【提出課題】LLM機能を搭載したWebアプリを開発しよう")
st.write("#### 操作方法")
st.write("質問したい先生を選択し、入力フォームに質問を入力し「実行」ボタンを押してください")


selected_item = st.radio(
    "質問したい先生を選択してください。",
    ["国語の先生", "数学の先生", "英語の先生", "社会の先生","理科の先生"]
)

st.divider()

input_message = st.text_input(label="担当教科の質問をしてください")

if st.button("実行"):
    st.divider()

    if not input_message:
        st.error("質問を入力してください。")
    else:
        try:
            if selected_item == "国語の先生":
                result = get_japanese_answer(input_message)
            elif selected_item == "数学の先生":
                result = math_tools[0].run(input_message)
            elif selected_item == "英語の先生":
                result = get_english_answer(input_message)
            elif selected_item == "社会の先生":
                result = get_social_answer(input_message)
            elif selected_item == "理科の先生":
                result = get_science_answer(input_message)

            st.write(result)

        except Exception:
            st.error("エラーが発生しました。質問内容や選択した先生を確認してください。")

