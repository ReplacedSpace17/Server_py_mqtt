import paho.mqtt.publish as publish
import databseConn

def publish_message(message):
    publish.single("lap/mensaje", message, hostname="192.168.1.101", port=1883)
    print("Mensaje enviado")
    return "Mensaje enviado"


# async def  suscribe_message():
#     import paho.mqtt.subscribe as subscribe
#     #Recibe el mensaje del broker MQTT
#     msg = subscribe.simple("lap/mensaje", hostname="192.168.1.101", port=1883)
    
#     #print(str(msg.payload))
#     #Convierte el mensaje a cadena de texto
#     cadena_texto = msg.payload.decode('utf-8').strip("'b")
    
#     #Guarda el mensaje en la base de datos
#     databseConn.guardar_en_mysql(cadena_texto)
#     #print(cadena_texto)
#     return cadena_texto

async def suscribe_message():
    import paho.mqtt.subscribe as subscribe
    msg = subscribe.simple("lap/mensaje", hostname="192.168.1.101", port=1883)
    payload = msg.payload.decode('utf-8').strip("'b")  # Convertir el payload a cadena de texto
    id_dispositivo, mensaje = payload.split(":")
    print("Id    ",id_dispositivo)# Separar el ID del dispositivo y el mensaje
    print("Mensaje    ",mensaje)
    print(type(mensaje))
    databseConn.guardar_en_mysql(str(mensaje))  # Llamar a la función para guardar en la base de datos
    return id_dispositivo, mensaje

