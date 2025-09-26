from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API El chavo"}

@app.get("/saludo")
def saludo(nombre: Optional[str] = Query(default="Juan")):
    return {"saludo": f"Hola, {nombre}!"}

@app.get("/suma")
def suma(a: int = Query(...), b: int = Query(...)):
    resultado = a + b
    return {"operacion": f"{a} + {b}", "resultado": resultado}

@app.get("/status")
def status():
    return {"status": "La API está corriendo correctamente", "puerto": 8050}
