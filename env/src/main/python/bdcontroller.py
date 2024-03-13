import os
import json
import mysql.connector
def guardar_en_json(directorio, mensaje_json, nombre_archivo="mensaje.json"):
    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # Unir el directorio y el nombre del archivo
    ruta_completa = os.path.join(directorio, nombre_archivo)

    # Guardar el mensaje JSON en el archivo
    with open(ruta_completa, 'w') as archivo:
        json.dump(mensaje_json, archivo, indent=2)

    print(f"Mensaje guardado en: {ruta_completa}")




def insertar_en_mysql(mensaje_json, numero_expediente):
    try:
        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host="bd.smartwaystudio.com",
            user="licitaciones_smw",
            password="^w8b@8y*ACydQvr0EBfOf#EuSb",
            database="licitaciones"
        )

        # Crear un cursor
        cursor = conexion.cursor()

       
        numero_expediente_modificado = numero_expediente.replace("_", "/")

        try:
            cursor.execute("""
            UPDATE licitaciones 
            SET responsePrompt = %s 
            WHERE numeroExpediente = %s
        """, (mensaje_json, numero_expediente_modificado))
            # Confirmar la transacción
            conexion.commit()
        except mysql.connector.Error as insert_error:
            # Si ocurre un error, intentar con el número de expediente original
            cursor.execute("""
            UPDATE licitaciones 
            SET responsePrompt = %s 
            WHERE numeroExpediente = %s
        """, (mensaje_json, numero_expediente_modificado))
            # Confirmar la transacción
            conexion.commit()

        print("Mensaje insertado en la base de datos MySQL")

    except mysql.connector.Error as error:
        print(f"Error al insertar en MySQL: {error}")

    finally:
        # Cerrar el cursor y la conexión
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conexion' in locals() and conexion is not None:
            conexion.close()

def obtener_estadisticas_mysql():
    try:
        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host="bd.smartwaystudio.com",
            user="licitaciones_smw",
            password="^w8b@8y*ACydQvr0EBfOf#EuSb",
            database="licitaciones"
        )

        # Crear un cursor
        cursor = conexion.cursor()

        # Obtener las estadísticas de la base de datos
        cursor.execute("""
        SELECT COUNT(*) FROM licitaciones
    """)
        total_licitaciones = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM licitaciones WHERE responsePrompt IS NOT NULL
    """)
        licitaciones_con_respuesta = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM licitaciones WHERE responsePrompt IS NULL
    """)
        licitaciones_sin_respuesta = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM licitaciones WHERE responsePrompt IS NOT NULL AND responsePrompt != ""
    """)
        licitaciones_con_respuesta_valida = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM licitaciones WHERE responsePrompt IS NOT NULL AND responsePrompt = ""
    """)
        licitaciones_con_respuesta_vacia = cursor.fetchone()[0]

        cursor.execute("""
        SELECT COUNT(*) FROM prompdata 
    """)
        prompts_parseados = cursor.fetchone()[0]

        print(f"Total de licitaciones: {total_licitaciones}")
        print(f"Licitaciones con respuesta: {licitaciones_con_respuesta}")
        print(f"Licitaciones sin respuesta: {licitaciones_sin_respuesta}")
        
        carpetas_persist = sum([len(dirs) for _, dirs, _ in os.walk('/workspaces/langchain3.9/env/src/main/python/persist')])
        carpetas_document = sum([len(dirs) for _, dirs, _ in os.walk('/workspaces/langchain3.9/PliegosTecnicos')])
        print(f"Total de carpetas con documento: {carpetas_document}")
        print(f"Total de carpetas en persist: {carpetas_persist/2}")
        print(f"Propmts parseados:{prompts_parseados}")
        

    except mysql.connector.Error as error:
        print(f"Error al obtener estadísticas de MySQL: {error}")

    finally:
        # Cerrar el cursor y la conexión
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conexion' in locals() and conexion is not None:
            conexion.close()
