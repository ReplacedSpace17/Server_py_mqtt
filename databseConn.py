
import datetime
from vars.db_config import get_db_connection

import time

MAX_INTENTOS = 3  # Número máximo de intentos de conexión


def verificar_conexion():
    intentos = 0
    while intentos < MAX_INTENTOS:
        try:
            # Establecer conexión con la base de datos MySQL
            connection = get_db_connection()

            # Verificar si la conexión fue exitosa
            if connection.is_connected():
                print("Conexión exitosa a la base de datos")
                return True
            else:
                print("Error al conectar a la base de datos")
                intentos += 1
                time.sleep(1)  # Esperar un segundo antes de intentar de nuevo

            # Cerrar conexión
            connection.close()
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            intentos += 1
            time.sleep(1)  # Esperar un segundo antes de intentar de nuevo
            
    print("No se pudo establecer conexión después de", MAX_INTENTOS, "intentos")
    return False


def guardar_en_mysql(topico,id, sensor, mensaje):
    # Verificar la conexión con la base de datos
    connection = get_db_connection()
    

    try:
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Consulta para crear la tabla si no existe
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {topico} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha DATETIME,
            id_dispositivo VARCHAR(255),
            sensor VARCHAR(255),
            valor VARCHAR(255)
        )
        """

        # Ejecutar la consulta para crear la tabla
        cursor.execute(create_table_query)

        # Obtener la fecha actual
        fecha_actual = datetime.datetime.now()
        # Hacer commit para guardar los cambios
        connection.commit()
        print("Tabla creada exitosamente")
        
        cursor = connection.cursor()

        # Consulta para insertar el mensaje en la tabla de la base de datos
        insert_query = f"INSERT INTO {topico} (fecha, id_dispositivo, sensor, valor) VALUES (%s, %s, %s, %s)"
        mensaje_data = (datetime.datetime.now(), id, sensor, mensaje)

        # Ejecutar la consulta para insertar el mensaje
        cursor.execute(insert_query, mensaje_data)

        # Hacer commit para guardar los cambios
        connection.commit()
        print("Mensaje guardado en la base de datos")

        # Cerrar cursor y conexión
        cursor.close()
        connection.close()
    except Exception as e:
        print("Error al guardar el mensaje en la base de datos:", e)
        connection.close()