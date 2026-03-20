import wget
import os

# from langchain_core.document_loaders import
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chat_models import init_chat_model
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_chroma import Chroma

filename = "companyPolicies.txt"
llm = init_chat_model("openai:gpt-5", temperature=0.5)


# Pre-processing
def load_document():
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JDbUb_L3egv_eOkouY71A.txt"

    # download document uisng wget
    wget.download(url, out=filename)
    print("file downloaded")

    # open the file
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)


# splitting documents into cunks
def split_into_chunks():
    loader = TextLoader(filename)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    print(len(texts))
    return texts


# Embedding and saving - embedding means converting document into vectors and saving into vector store
def embedding_saving():
    os.environ["PWD"] = os.getcwd()

    embedding = HuggingFaceEmbeddings()
    docsearch = Chroma.from_documents(
        split_into_chunks(), embedding, persist_directory="./chroma_db"
    )  # store the embedding in docsearch using Chromadb
    print("document ingested")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=False,
    )
    query = "Can you summarize the document for me"
    rsp = qa.invoke({"query": query})
    print(rsp.get("result"))


# load_document()
embedding_saving()
