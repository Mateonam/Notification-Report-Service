from fastapi import FastAPI

# Inicializamos la aplicación
app = FastAPI(
    title="Report Generator API",
    description="Microservicio para generar reportes en PDF",
    version="1.0.0"
)

# Creamos nuestro primer "Endpoint" (Ruta de acceso)
@app.get("/")
def home():
    return {"mensaje": "El microservicio de reportes está funcionando al 100%"}