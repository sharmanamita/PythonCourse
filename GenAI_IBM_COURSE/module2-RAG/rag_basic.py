import wget

# from langchain_core.document_loaders import
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import chroma

filename = "companyPolicies.txt"


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
    embedding = HuggingFaceEmbeddings()
    docsearch = chroma.from_documents(
        split_into_chunks(), embedding
    )  # store the embedding in docsearch using Chromadb
    print("document ingested")


load_document()
split_into_chunks()
