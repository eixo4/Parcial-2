from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="API de Vacunación Sarampión Panamá",
    description="API de solo lectura para consultar datos históricos del indicador SH.IMM.MEAS.",
    version="1.0.0"
)

# Modularización: incluimos las rutas definidas en el otro archivo
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    # Se habilita reload para facilitar el desarrollo en PyCharm
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)