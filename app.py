from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os




from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from ingest import create_vectorstore

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.set_page_config(page_title="Website Chatbot", layout="centered")
st.title("🌐 Website Chatbot")

url = st.text_input("Enter Website URL")

if st.button("Index Website"):
    if url:
        with st.spinner("Indexing website..."):
            create_vectorstore(url)
        st.success("Website indexed successfully!")
    else:
        st.error("Please enter a URL")

if os.path.exists("vectorstore"):

    from langchain_openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    retriever = db.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""
Answer ONLY from the context below.
If answer not present, say:
"The answer is not available on the provided website."

Context:
{context}

Question:
{question}
""")

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)



    question = st.text_input("Ask a question")

    if question:
        answer = chain.invoke(question)
        st.write(answer)


