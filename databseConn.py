import datetime

from vars.db_config import get_db_connection



def verificar_conexion():
    try:
        # Establecer conexión con la base de datos MySQL
        connection = get_db_connection()

        # Verificar si la conexión fue exitosa
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        else:
            print("Error al conectar a la base de datos")
            return False

        # Cerrar conexión
        connection.close()
        return True
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return False
    
    
def guardar_en_mysql(mensaje):
    # Establecer conexión con la base de datos MySQL
    connection = get_db_connection()
    
    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Consulta para crear la tabla si no existe
    create_table_query = """
    CREATE TABLE IF NOT EXISTS mensajes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha DATETIME,
        valor VARCHAR(255)
    )
    """

    # Ejecutar la consulta para crear la tabla
    cursor.execute(create_table_query)

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()

    # Consulta para insertar el mensaje en la tabla de la base de datos
    insert_query = "INSERT INTO mensajes (fecha, valor) VALUES (%s, %s)"
    mensaje_data = (fecha_actual, mensaje)

    # Ejecutar la consulta para insertar el mensaje
    cursor.execute(insert_query, mensaje_data)

    # Hacer commit para guardar los cambios
    connection.commit()
    print("Mensaje guardado en la base de datos")

    # Cerrar cursor y conexión
    cursor.close()
    connection.close()