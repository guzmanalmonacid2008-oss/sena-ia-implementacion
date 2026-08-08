import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

HISTORIAL = []

class PeticionClasificar(BaseModel):
    texto: str
    motor: str = "eco"

def clasificar_eco(texto: str) -> str:
    texto_lower = texto.lower()
    if "endpoint" in texto_lower or "salud" in texto_lower:
        return "feat"
    elif "readme" in texto_lower or "actualiza" in texto_lower:
        return "docs"
    elif "pruebas" in texto_lower or "unitarias" in texto_lower:
        return "test"
    return "fix"

@app.get("/health")
def health():
    return {"estado": "ok"}

@app.post("/clasificar")
def clasificar(peticion: PeticionClasificar):
    if peticion.motor != "eco":
        raise HTTPException(status_code=400, detail="Motor no soportado")
    
    inicio = time.time()
    tipo = clasificar_eco(peticion.texto)
    latencia = (time.time() - inicio) * 1000
    
    registro = {"texto": peticion.texto, "tipo": tipo, "motor": peticion.motor}
    HISTORIAL.append(registro)
    
    return {"tipo": tipo, "latencia_ms": latencia}

@app.get("/inferencias")
def obtener_inferencias(limite: int = 10):
    return HISTORIAL[-limite:]
