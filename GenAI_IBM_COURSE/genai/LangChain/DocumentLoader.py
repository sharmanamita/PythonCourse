
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
# import os
# os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

SCRIPT_DIR = Path(__file__).parent
file_path = f"{SCRIPT_DIR.parent.parent}\\cheat_sheet\\LangchainInAi.pdf"

# pdfloader - loads PDF documents

pdf_loader = PyPDFLoader(file_path=file_path)
# print(pdf_loader.load())

loader = WebBaseLoader("https://python.langchain.com/v0.2/docs/introduction/")
web_data = loader.load()
