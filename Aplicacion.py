from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import io
from PIL import Image
import pytesseract

app = FastAPI()

# Habilitar CORS para permitir solicitudes desde el frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aquí puedes especificar el dominio del frontend si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta para recibir la imagen
@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Leer la imagen enviada
        image = Image.open(io.BytesIO(await file.read()))
        
        # Procesar la imagen y extraer texto usando pytesseract
        text = pytesseract.image_to_string(image)
        
        # Devolver el texto extraído en formato JSON
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}

# Ejecutar la aplicación (si corres el archivo directamente)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
