
from dotenv import load_dotenv
load_dotenv()


from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = '사과' 

# print(response.content)

import streamlit as st

st.title("디지털 정보창")
st.title(chat_model.model)

subject  = st.text_input("알고 싶은 거 입력해 주세요")

if st.button("궁금증 해결해 줘!", type="secondary", icon="🔥"):
    with st.spinner("Wait for it..."):
    # with st.spinner("Wait for it...", show_time=True):
        response = chat_model.invoke(subject + "에 대해 설명해줘")
        st.success("완료")
        st.write(response.content)    