import os
import getpass
import shutil
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from pdf import get_text_pdf
def create_bd(chroma_path, pdf_paths):
    load_dotenv()
    # CHROMA_PATH = "env/src/main/python/persist"
    
    if os.path.exists(chroma_path):
        print("VectorStore Chroma ya existe en", chroma_path)
        return None

    pdf_list = [] 
    for pdf_path in pdf_paths:
        # Obtiene el texto del PDF
        
        pdf_text = get_text_pdf(pdf_path)
        if pdf_text != []:
            pdf_list.append(pdf_text)
                  
        # Divide el texto en documentos
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    all_documents = []
    
    for pdf_text in pdf_list:
        documents = text_splitter.split_documents(pdf_text)
        all_documents.extend(documents)

    if all_documents:
        db = Chroma.from_documents(all_documents, OpenAIEmbeddings(), persist_directory=chroma_path)
        # Agrega los documentos al vector store Chroma con embeddings de OpenAI  
        # Persiste el vector store Chroma
        db.persist()
        print("VectorStore Chroma creado en", chroma_path, "con", len(pdf_paths), "archivos PDF")
        return db
    else:
        print("No se encontraron archivos PDF válidos")
        return None


