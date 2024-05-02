import asyncio
import aiomqtt,os, sys
from typing import List
from pydantic import BaseModel
import databseConn

# Definir el modelo Pydantic para el JSON esperado
class TopicItem(BaseModel):
    topico: str

async def subscribe_topics(topics: List[TopicItem]):
    async with aiomqtt.Client("192.168.102.109", port=1883) as client:
        for topic_item in topics:
            await client.subscribe(topic_item.topico)
            print(f"Suscrito al tópico: {topic_item.topico}")

        async for message in client.messages:
            print(f"Mensaje recibido en el tópico {message.topic}: {message.payload.decode()}")
            #guardar_en_mysql(message.payload.decode())
            payload = message.payload.decode('utf-8').strip("'b")  # Convertir el payload a cadena de texto
            id_dispositivo,sensor, mensaje = payload.split(":")
            print("Id    ",id_dispositivo)# Separar el ID del dispositivo y el mensaje
            print("Mensaje    ",mensaje)
            print("Sensor    ",sensor)
            print(type(message.topic))
            print(message.topic)
            databseConn.guardar_en_mysql(message.topic,id_dispositivo,sensor,mensaje)
        return {"message": "Subscripciones exitosas"}

if sys.platform.lower() == "win32" or os.name.lower() == "nt":
    from asyncio import set_event_loop_policy, WindowsSelectorEventLoopPolicy
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    
    