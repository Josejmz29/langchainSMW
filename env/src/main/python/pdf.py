from langchain_community.document_loaders import PyPDFLoader
import os
from pypdf import PdfReader


def get_text_pdf(path):
    loader = PyPDFLoader(path)
    try:
        pages = loader.load_and_split()
        return pages
    except Exception as e:
        print(f"Error al abrir el archivo {path}: {e}")
        return []
    

def es_pdf_valido(path):
    try:
        with open(path, 'rb') as file:
            PdfReader(file)
        return True
    except Exception as e:
        #print(f"Error al abrir el archivo {path}: {e}")
        return False
