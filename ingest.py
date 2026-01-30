from dotenv import load_dotenv
load_dotenv()

import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import os

def load_website(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return text


def create_vectorstore(url):
    text = load_website(url)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(text)

    embeddings = OpenAIEmbeddings()


    vectorstore = FAISS.from_texts(chunks, embeddings)

    os.makedirs("vectorstore", exist_ok=True)
    vectorstore.save_local("vectorstore")

    return True
