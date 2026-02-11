from langchain_text_splitters import RecursiveCharacterTextSplitter
from Embedding import getEmbedding
from pathlib import Path
from langchain_community.vectorstores import Chroma

filepath = Path(__file__).parent.parent / "cheat_sheet" / "LangchainInAi.pdf"

recursiveTextSplitters = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = recursiveTextSplitters.split_text(filepath)

embedding = getEmbedding()

vector = Chroma.from_documents(chunks, embedding=embedding)

docs = vector.similarity_search("LangChain")
print(' docs:', docs)

# Convert a vector store to a retriever
retriever = vector.as_retriever()
#  Retrieve documents
docs = retriever.invoke("Langchain")
print(' docs from retriever:', docs)