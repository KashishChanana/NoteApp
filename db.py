import os
import time
from dotenv import find_dotenv, load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OpenAIEmbeddings

_ = load_dotenv(find_dotenv())

class PineconeDB():

    def __init__(self) -> None:
        self.index_name = "noteapp-index"
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.index = None
        self.vector_store = None

        pinecone = Pinecone(api_key=os.environ['PINECONE_API_KEY'])
        existing_indexes = [index_info["name"] for index_info in pinecone.list_indexes()]
        if self.index_name not in existing_indexes:
            pinecone.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )
            # wait for index to be initialized
            while not pinecone.describe_index(self.index_name).status['ready']:
                time.sleep(1)

        try:
            # connect to index
            self.index = pinecone.Index(self.index_name)
            time.sleep(1)
            # view index stats
            self.index.describe_index_stats()
            print("DB Instantiated.")

        except Exception as e:
            print(e)

    
    def upsert(self, documents:list):
        self.vector_store = PineconeVectorStore.from_documents(documents=documents, embedding=self.embeddings, index_name=self.index_name)
        print("Added to Vector Store.")


    def retrieve(self, question:str):
        self.vector_store = PineconeVectorStore(index_name=self.index_name, embedding=self.embeddings, pinecone_api_key=os.environ['PINECONE_API_KEY'])
        found_docs = self.vector_store.similarity_search(query=question)
        retrieved_content = ""
        for doc in found_docs:
            retrieved_content += doc.page_content
        return retrieved_content
        