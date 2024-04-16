import asyncio
import uvicorn
import databseConn
import mqqt_publish
from fastapi import FastAPI

app = FastAPI()

mensaje = None

async def suscribe_mqtt_messages():
    global mensaje
    while True:
        mensaje = await mqqt_publish.suscribe_message()
        print("Nuevo mensaje MQTT recibido:", mensaje)

@app.get("/")
def read_root():
    if mensaje:
        return {"mensaje": mensaje}
    else:
        return {"mensaje": "No hay mensajes disponibles"}

if __name__ == "__main__":
    print("-----------------Servidor iniciado----------------")
    databseConn.verificar_conexion()
    print("Esperando mensajes MQTT...")
    asyncio.run(suscribe_mqtt_messages())
    uvicorn.run(app)