from json import tool
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.tools import Tool
from langchain_community.vectorstores import Chroma
from langchain import LLMChain
from langchain.agents import create_openai_functions_agent
from langchain.tools.retriever import create_retriever_tool
from prompts import  prompt, prompt_template, licitacion_prompt
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_openai_tools_agent, initialize_agent, AgentType


load_dotenv()
#create_bd("env/src/main/python/persist", "documents/02_02_2024 SERx0xDOC202402061537044+INFORME+DE+NECESIDAD+CONTR+MANTENIMIENTO+PAG+WEB+2024.pdf")

#db = Chroma(persist_directory="env/src/main/python/persist", embedding_function=OpenAIEmbeddings())
def search_tool():
    db = Chroma(persist_directory="env/src/main/python/persist", embedding_function=OpenAIEmbeddings())
    query = "información del objeto del contrato,lugar donde se prestarán los servicios, tecnologias,presupuesto,equipo de trabajo necesario,fecha máxima para la presentación de solicitudes," \
		"plazo desarrollo, pago, criterios valoracion, fecha apertura sobres, bolsa horas, garantia, metodologia desarrollo, documentacion adjudicacion"

    docs = db.similarity_search_with_relevance_scores(query, k=3)
    if(len(docs) == 0 or docs[0][1]<0.7):
        print("No se encontraron documentos")
        return
    context_text = "\n\n--\n\n".join([doc.page_content for doc, _score in docs])
    print(context_text)
    return context_text



text_search_tool = Tool.from_function(func=search_tool,
    name="SearchTool",
    description="Busca informacion relevante sobre la licitacion")

prompt_tool = "Da la informacion de la licitacion sobre el siguiente texto {search_text}"
prompt_template=PromptTemplate.from_template(prompt_tool)
model = ChatOpenAI(model_name="gpt-4-turbo-preview")

llm_chain = LLMChain(
    llm=model,
    prompt=prompt_template
)

summarize_tool = Tool.from_function(
    func=llm_chain.run,
    name="Summarizer",
    description="Devuelve la informacion de la licitacion en formato JSON"
)

tools = [text_search_tool, summarize_tool]

agent = initialize_agent(
    tools=tools,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    llm=model,
    verbose=True
)

print(agent.run(prompt))
