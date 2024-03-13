from langManager import procesar_licitaciones
from agent import Agent
from bdcontroller import obtener_estadisticas_mysql
def main():
    #procesar_licitaciones()
    obtener_estadisticas_mysql()
    list = ["PliegosTecnicos/A_SER-037561_2023 (5-C_24)/A_SER-037561_2023 (5-C_24)x0x05_pliego_de_prescripciones_tecnicas_particulares_censurado.pdf","PliegosTecnicos/A_SER-037561_2023 (5-C_24)/A_SER-037561_2023 (5-C_24)x1xdiligencia_correccion_error_pcap_dp_so_jco_grabacion_datos_ganaderia.pdf"]
    nombre = "A_SER-037561_2023 (5-C_24)"
   # agente = Agent(list,nombre)
    query ="información del objeto del contrato,lugar donde se prestarán los servicios, tecnologias,presupuesto,equipo de trabajo necesario,fecha máxima para la presentación de solicitudes," \
		"plazo desarrollo, pago, criterios valoracion, fecha apertura sobres, bolsa horas, garantia, metodologia desarrollo, documentacion adjudicacion"
    #docs = agente.retrieve_documents(query)
    #print(docs)

if __name__ == "__main__":
    main()