import sys, os
from typing import List
from fastapi import FastAPI, HTTPException
import databseConn

from mqtt_suscriber import TopicItem, subscribe_topics


app = FastAPI()

subscription_active = False

@app.post("/subscribe/")
async def handle_subscription(topics: List[TopicItem]):
    global subscription_active
    subscription_active = True
    result = await subscribe_topics(topics)
    return result


@app.get("/active")
async def active():
    global subscription_active
    if  subscription_active==False:
        raise HTTPException(status_code=400, detail="Subscription not yet activated. Please POST to /subscribe first.")
    else:
        return {"message": "This is the /active endpoint."}

@app.get("/ping")
def ping():
    print("Ping")
    return {"message": "Servidor en línea"}

    
if __name__ == "__main__":
    import uvicorn
    print("-----------------Servidor iniciado----------------")
    # Verificar la conexión a la base de datos y a internet
    #databseConn.verificar_conexion()
    #databseConn.verificar_conexion_internet()
    print("Esperando mensajes MQTT...")
    uvicorn.run("app:__main__", host= "0.0.0.0", port=8000, reload=True)
