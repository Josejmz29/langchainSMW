# Documentación del archivo vectorstore.py

## Descripción General

El archivo `vectorstore.py` ubicado en `env/src/main/python/vectorstore.py` es un módulo fundamental del proyecto LangChain SMW que se encarga de crear y gestionar una base de datos vectorial utilizando Chroma para almacenar embeddings de documentos PDF.

## Componentes y Funcionalidad

### Importaciones

```python
import os
import getpass
import shutil
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from pdf import get_text_pdf
```

**Propósito de cada importación:**

- `os`, `getpass`, `shutil`: Utilidades del sistema para manejo de archivos y directorios
- `load_dotenv`: Carga variables de entorno desde archivo .env
- `TextLoader`: Cargador de documentos de texto de LangChain (importado pero no utilizado en el código actual)
- `OpenAIEmbeddings`: Generador de embeddings usando la API de OpenAI
- `CharacterTextSplitter`: Divisor de texto para fragmentar documentos largos
- `Chroma`: Sistema de base de datos vectorial para almacenar embeddings
- `get_text_pdf`: Función personalizada del módulo pdf.py para extraer texto de archivos PDF

### Función Principal: `create_bd(chroma_path, pdf_paths)`

Esta es la única función pública del módulo y se encarga de crear una base de datos vectorial Chroma a partir de una lista de archivos PDF.

#### Parámetros:
- `chroma_path` (str): Ruta donde se almacenará la base de datos Chroma
- `pdf_paths` (list): Lista de rutas a archivos PDF que se procesarán

#### Funcionamiento paso a paso:

1. **Carga de variables de entorno**: Utiliza `load_dotenv()` para cargar configuraciones
2. **Verificación de existencia**: Comprueba si ya existe una base de datos en la ruta especificada
3. **Procesamiento de PDFs**: 
   - Itera sobre cada archivo PDF en `pdf_paths`
   - Extrae el texto usando `get_text_pdf()` del módulo pdf.py
   - Filtra PDFs válidos (que contengan texto)
4. **División de texto**: Utiliza `CharacterTextSplitter` con:
   - `chunk_size=1000`: Fragmentos de máximo 1000 caracteres
   - `chunk_overlap=0`: Sin solapamiento entre fragmentos
5. **Creación de embeddings**: Usa `OpenAIEmbeddings()` para generar representaciones vectoriales
6. **Almacenamiento**: Crea la base de datos Chroma con los documentos procesados
7. **Persistencia**: Guarda la base de datos en el directorio especificado

#### Valores de retorno:
- `db`: Instancia de la base de datos Chroma si se crea exitosamente
- `None`: Si la base de datos ya existe o no se encuentran PDFs válidos

## Flujo de Trabajo

```
PDFs → Extracción de texto → División en fragmentos → Generación de embeddings → Almacenamiento en Chroma
```

## Dependencias Externas

- **OpenAI API**: Requiere clave de API para generar embeddings
- **Chroma**: Base de datos vectorial para almacenamiento persistente
- **LangChain**: Framework para aplicaciones de IA con modelos de lenguaje

## Casos de Uso

Este módulo es típicamente utilizado para:
- Crear bases de conocimiento a partir de documentos PDF
- Preparar datos para sistemas de búsqueda semántica
- Alimentar sistemas de Retrieval-Augmented Generation (RAG)
- Indexar documentos para consultas de similitud vectorial

## Limitaciones y Consideraciones

- Solo procesa archivos PDF
- Requiere conexión a internet para generar embeddings con OpenAI
- No maneja actualizaciones de la base de datos existente
- El tamaño de fragmento (1000 caracteres) es fijo
- No incluye manejo de errores robusto para fallos de red o API