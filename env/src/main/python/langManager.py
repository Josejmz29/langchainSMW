
import os
from agent import Agent
from pdf import es_pdf_valido
from bdcontroller import insertar_en_mysql

def obtener_paths_pdfs_ejecutar(directorio, limit=0):
    paths_pdfs = []
    n=0
    # Recorre el directorio de manera recursiva
    for directorio_actual, _, archivos in os.walk(directorio):
        if limit > 0 and n >= limit:
            break
        
                
        paths_pdfs = []
        # Filtra los archivos que son PDF       
        subdirectorio_nombre = directorio_actual.split(os.path.sep)[-1]
        subdirectorio_nombre_modificado = subdirectorio_nombre.replace('_', '/')
        if not os.path.exists(os.path.join("/workspaces/langchain3.9/env/src/main/python/persist", subdirectorio_nombre)):
            

            for archivo in archivos:
                if archivo.lower().endswith('.pdf'):
                    path_completo = os.path.join(directorio_actual, archivo)
                    if es_pdf_valido(path_completo):
                        paths_pdfs.append(path_completo)


            # Obtiene los paths completos de los PDF y los agrega a la lista       
            agent = Agent(paths_pdfs,subdirectorio_nombre)
            ejecutar_agente(agent)
        else:
            print(f"Agente ya ejecutado {subdirectorio_nombre}")
        n+=1
        print(f"Procesados {n} directorios")
        
    

def ejecutar_agente(agent: Agent):
    query ="información del objeto del contrato,lugar donde se prestarán los servicios, tecnologias,presupuesto,equipo de trabajo necesario,fecha máxima para la presentación de solicitudes," \
		"plazo desarrollo, pago, criterios valoracion, fecha apertura sobres, bolsa horas, garantia, metodologia desarrollo, documentacion adjudicacion"
            
    if(agent.paths != []):       
        print(f"Vector store creado para {agent.nombre}")    
        response= agent.generate_licitacion_response(query)
        print(response)
        insertar_en_mysql(response, agent.nombre)
            
    else:
        print(f"No hay archivos PDF en {agent.nombre}")

    
    return agent

def procesar_licitaciones(limit=0):
    directorio_raiz = "/workspaces/langchain3.9/PliegosTecnicos"   
    obtener_paths_pdfs_ejecutar(directorio_raiz, limit=limit)


    
    
    