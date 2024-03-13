# prompts.py
from langchain.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate

description_prompt = PromptTemplate.from_template(
    "Dime algo sobre el {topic}")




prompt =  """Quiero que me generes una ficha de la licitación en formato JSON. Esta ficha contendrá información detallada sobre varios aspectos de la licitación, organizada en un formato estructurado. Para cada punto que te indico a continuación, incluye el título como clave y la información relevante como valor. La respuesta debe seguir el formato JSON especificado a continuación, con cada sección claramente delimitada y todos los datos relevantes incluidos de forma concisa. Asegúrate de que la respuesta en formato JSON contenga las siguientes claves y valores correspondientes a cada punto: "+
            "\\\"resumenObjetoContrato\\\": información del objeto del contrato.\\\"lugarPrestacionServicios\\\": lugar donde se prestarán los servicios.\\\"tecnologiasFrontEnd\\\": listado de tecnologías para el desarrollo del FrontEnd.\\\"tecnologiasBackEnd\\\": listado de tecnologías para el desarrollo del Backend.\\\"tecnologiasOtros\\\": listado de tecnologías para soluciones no clasificables en FrontEnd o BackEnd.\\\"equipoTrabajo\\\": detalles del equipo de trabajo necesario, incluyendo formación y experiencia mínima.\\\"fechaMaximaPresentacion\\\": fecha máxima para la presentación de solicitudes.\\\"presupuestoMaximo\\\": presupuesto máximo disponible.\\\"plazoDesarrollo\\\": plazo estimado para el desarrollo del proyecto.\\\"formaPago\\\": detalles sobre la forma de pago.\\\"fechaAperturaSobres\\\": fecha de apertura de los sobres.\\\"criteriosValoracion\\\": criterios para la valoración de ofertas, incluyendo los puntos otorgados.\\\"bolsaHoras\\\": indica si es necesario incluir una bolsa de horas.\\\"garantiaMantenimiento\\\": garantía y mantenimiento requeridos.\\\"metodologiaDesarrollo\\\": si se exige seguir alguna metodología de desarrollo específica.\\\"documentacionAdjudicacion\\\": documentación requerida para optar a la adjudicación, con un resumen de cada documento. El formato JSON debe seguir este esquema general (los valores aquí son solo ejemplos; debes reemplazarlos con la información específica solicitada)" + "json Copy code { \\\"resumenObjetoContrato\\\": \\\"Descripción del objeto del contrato.\\\",  \\\"lugarPrestacionServicios\\\": \\\"Ciudad, País.\\\", \\\"tecnologiasFrontEnd\\\": [\\\"Tecnología1\\\", \\\"Tecnología2\\\"],  \\\"tecnologiasBackEnd\\\": [\\\"Tecnología3\\\", \\\"Tecnología4\\\"], \\\"tecnologiasOtros\\\": [\\\"Tecnología5\\\", \\\"Tecnología6\\\"], \\\"equipoTrabajo\\\": {   \\\"rol1\\\": {  \\\"resumenCriterio\\\": \\\"Descripción del rol\\\",  \\\"formacion\\\": \\\"formacion necesaria para desempeñar este rol\\\", "
                +" \\\"experiencia\\\": \\\"experiencia necesaria para desempeñar este rol\\\",}, \\\"rol2\\\": {  \\\"resumenCriterio\\\": \\\"Descripción del rol\\\",  \\\"formacion\\\": \\\"formacion necesaria para desempeñar este rol\\\",  \\\"experiencia\\\": \\\"experiencia necesaria para desempeñar este rol\\\",},\\\"rol3\\\": {  \\\"resumenCriterio\\\": \\\"Descripción del rol\\\",  \\\"formacion\\\": \\\"formacion necesaria para desempeñar este rol\\\",  \\\"experiencia\\\": \\\"experiencia necesaria para desempeñar este rol\\\",}, },  \\\"fechaMaximaPresentacion\\\": \\\"DD/MM/AAAA\\\",  \\\"presupuestoMaximo\\\": \\\"Cantidad máxima.\\\",  \\\"plazoDesarrollo\\\": \\\"X meses/días.\\\",  \\\"formaPago\\\": \\\"Descripción de la forma de pago.\\\",  \\\"fechaAperturaSobres\\\": \\\"DD/MM/AAAA\\\", \\\"criteriosValoracion\\\": {\\\"criterio1\\\": {  \\\"resumenCriterio\\\": \\\"resumen del criterio\\\",  \\\"puntos\\\": \\\"Descripción y puntos.\\\"},\\\"criterio2\\\": { \\\"resumenCriterio\\\": \\\"resumen del criterio\\\",  \\\"puntos\\\": \\\"Descripción y puntos.\\\"}, }, \\\"bolsaHoras\\\": \\\"Sí/No, con detalles si aplica.\\\",\\\"garantiaMantenimiento\\\": \\\"Descripción de garantía y mantenimiento.\\\",  \\\"metodologiaDesarrollo\\\": \\\"Nombre de la metodología, si aplica.\\\", \\\"documentacionAdjudicacion\\\": { \\\"documento1\\\": \\\"Resumen del contenido.\\\",\\\"documento2\\\": \\\"Resumen del contenido.\\\"}}     Por favor, sigue este formato detalladamente para generar la ficha de la licitación. La precisión y claridad son esenciales para que la información sea útil y pueda ser almacenada correctamente en la base de datos."""

template = """
         Responda la siguiente pregunta basándose únicamente en el contexto proporcionado.:

<context>
{context}
</context>

Question: {prompt}
"""
licitacion_prompt = PromptTemplate.from_template(prompt)
prompt_template = ChatPromptTemplate.from_template(template)
