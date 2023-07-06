from fastapi import FastAPI
import uvicorn

from uce.ai.openuce import Document, process_inference

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/inference", status_code=200)
def inference(doc: Document):
    respuestas = process_inference(doc.item)
    return {
        'response': respuestas
    }

#uvicorn main:app --reload --port=1008

