from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# LLMの初期化
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

def get_llm_response(user_input: str, expert_type: str) -> str:
    """
    LLMに質問を送信して回答を取得する関数
    
    Args:
        user_input (str): ユーザーからの質問テキスト
        expert_type (str): 専門家の種類（「エンジニア」または「UIデザイナー」）
    
    Returns:
        str: LLMからの回答テキスト
    """
    # 選択に応じたシステムメッセージを設定
    if expert_type == "エンジニア":
        system_message = "あなたは経験豊富なソフトウェアエンジニアです。技術的な質問に対して、専門的かつ実践的なアドバイスを提供してください。"
    else:
        system_message = "あなたは経験豊富なUIデザイナーです。ユーザーインターフェースやユーザーエクスペリエンスに関する質問に対して、専門的かつ実践的なアドバイスを提供してください。"
    
    # メッセージを作成
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input),
    ]
    
    # LLMから回答を取得
    result = llm.invoke(messages)
    
    return result.content

st.title("LLM機能を搭載したWebアプリ")

st.write("このWebアプリは、LLM（大規模言語モデル）の機能を活用したシンプルなツールです。")
st.write("専門家の種類を選択して、質問を入力してください。")

# 専門家の種類を選択
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ["エンジニア", "UIデザイナー"]
)

# ユーザー入力
user_input = st.text_input("質問を入力してください:")

if st.button("送信"):
    if user_input:
        # 関数を呼び出してLLMから回答を取得
        response = get_llm_response(user_input, expert_type)
        
        # Streamlitで表示
        st.divider()
        st.write("**回答:**")
        st.write(response)
    else:
        st.error("質問を入力してください。")

