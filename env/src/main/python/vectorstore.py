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
    """
    Crea una base de datos vectorial Chroma a partir de archivos PDF.
    
    Args:
        chroma_path (str): Ruta donde se almacenará la base de datos Chroma
        pdf_paths (list): Lista de rutas a archivos PDF para procesar
        
    Returns:
        db (Chroma): Instancia de la base de datos Chroma si se crea exitosamente
        None: Si la base de datos ya existe o no hay PDFs válidos
    """
    # Carga las variables de entorno (incluyendo la API key de OpenAI)
    load_dotenv()
    # CHROMA_PATH = "env/src/main/python/persist"
    
    # Verifica si ya existe una base de datos Chroma en la ruta especificada
    if os.path.exists(chroma_path):
        print("VectorStore Chroma ya existe en", chroma_path)
        return None

    # Lista para almacenar el texto extraído de los PDFs válidos
    pdf_list = [] 
    for pdf_path in pdf_paths:
        # Obtiene el texto del PDF usando la función del módulo pdf.py
        pdf_text = get_text_pdf(pdf_path)
        if pdf_text != []:  # Solo agrega PDFs que contengan texto
            pdf_list.append(pdf_text)
                  
    # Configura el divisor de texto para fragmentar documentos largos
    # chunk_size=1000: fragmentos de máximo 1000 caracteres
    # chunk_overlap=0: sin solapamiento entre fragmentos
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    # Lista para almacenar todos los documentos fragmentados
    all_documents = []
    
    # Procesa cada PDF válido y lo divide en fragmentos
    for pdf_text in pdf_list:
        documents = text_splitter.split_documents(pdf_text)
        all_documents.extend(documents)

    # Si hay documentos válidos, crea la base de datos vectorial
    if all_documents:
        # Crea la base de datos Chroma con embeddings de OpenAI
        db = Chroma.from_documents(all_documents, OpenAIEmbeddings(), persist_directory=chroma_path)
        # Agrega los documentos al vector store Chroma con embeddings de OpenAI  
        # Persiste el vector store Chroma en el directorio especificado
        db.persist()
        print("VectorStore Chroma creado en", chroma_path, "con", len(pdf_paths), "archivos PDF")
        return db
    else:
        print("No se encontraron archivos PDF válidos")
        return None


