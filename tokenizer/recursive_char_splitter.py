from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text:str, chunk_size=None, chunk_overlap=None):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap=50)
    splits = text_splitter.split_documents(text)
    return splits