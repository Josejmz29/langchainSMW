from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from prompts import  licitacion_prompt
from pdf import get_text_pdf
from langchain.prompts import ChatPromptTemplate

# loads the .env file
load_dotenv()

query_prompt = """
    Responde a las instrucciones indicadas sobre el siguiente texto.:

    {text}

    Indicaciones: {question}

"""
text = get_text_pdf("documents/02_02_2024 SERx0xDOC202402061537044+INFORME+DE+NECESIDAD+CONTR+MANTENIMIENTO+PAG+WEB+2024.pdf")

context_text = "\n\n--\n\n".join([text.page_content for text in text])
#print(context_text)
prompt_template = ChatPromptTemplate.from_template(query_prompt)
prompt = prompt_template.format(text=context_text, question=licitacion_prompt.template)
llm = ChatOpenAI(model_name="gpt-4-turbo-preview")



output = llm.predict(prompt)
print(output)

