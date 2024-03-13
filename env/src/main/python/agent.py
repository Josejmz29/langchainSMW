from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from vectorstore import create_bd
from prompts import prompt, prompt_template, licitacion_prompt

class Agent:
    def __init__(self, paths, nombre):
        self.paths = paths
        self.chroma_path = f"env/src/main/python/persist/{nombre}"
        self.nombre = nombre
        load_dotenv()

    def create_vector_store(self):
        return create_bd(self.chroma_path, self.paths)

    def retrieve_documents(self, query, k=3):
        
        db = Chroma(persist_directory=self.chroma_path, embedding_function=OpenAIEmbeddings())
        docs = db.similarity_search_with_relevance_scores(query, k=k)
        
        return docs

    def generate_response(self, docs):
        if len(docs) == 0 or docs[0][1] < 0.7:
            return "No se encontraron documentos"
        
        context_text = "\n\n--\n\n".join([doc.page_content for doc, _score in docs])
        formatted_prompt = prompt_template.format(prompt=prompt, context=context_text)
        
        model = ChatOpenAI(model_name="gpt-4-turbo-preview")
        response = model.predict(formatted_prompt)
        return response
    
    def generate_licitacion_response(self, query):
        self.create_vector_store()
        docs = self.retrieve_documents(query)
        print(docs)
        return self.generate_response(docs)