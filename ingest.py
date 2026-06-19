import os
from langchain_community.document_loaders import DirectoryLoader , TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


print("Loading company documents...")
loader = DirectoryLoader("knowledge_base", glob="*.txt",loader_cls=TextLoader)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
print(f"split document into {len(chunks)} individual text chunks.")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Converting text chunks to vectors and saving to ChromaDB...")
persist_directory = "./chroma_db"

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=persist_directory
)

print("success! Your vector database is saved and ready at './chroma_db'")