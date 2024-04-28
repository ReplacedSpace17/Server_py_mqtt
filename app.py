import sys, os
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import databseConn

from mqtt_suscriber import TopicItem, subscribe_topics


app = FastAPI()

@app.post("/subscribe/")
async def handle_subscription(topics: List[TopicItem]):
    result = await subscribe_topics(topics)
    return result


    
if __name__ == "__main__":
    import uvicorn
    print("-----------------Servidor iniciado----------------")
    databseConn.verificar_conexion()
    print("Esperando mensajes MQTT...")
    uvicorn.run(app)
