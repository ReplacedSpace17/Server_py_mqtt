
from fastapi import FastAPI
import mqqt_publish
app = FastAPI()


mensaje = mqqt_publish.publish_message(str("Hol"))
mensaje1 = mqqt_publish.suscribe_message()
@app.get("/")
def read_root():
    return mensaje1

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)