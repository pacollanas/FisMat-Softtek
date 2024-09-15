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
        extracted_text = pytesseract.image_to_string(image)
        
        def analisis_texto(text):
            from openai import OpenAI
            client = OpenAI(
                api_key="-",
                base_url="https://fridaplatform.com/v1"
            )
            response = client.chat.completions.create(
            model="tgi",
                messages=[
                {"role": "system", "content": "You are an AI financial advisor specialized in the construction industry. Your task is to automate the analysis of accounts payable by classifying the following data and generating actionable financial recommendations."},
                {"role": "user", "content": f"Generate a detailed financial report analyzing the following data. Include insights on the financial health and provide actionable recommendations for improving financial management based on the extracted information:\n\n{text}"},
            ],max_tokens=500, stream=False
            )
            return response.choices[0].message.content
        
        # Formato en Markdown
        formatted_text = f"## Texto extraído de la imagen\n\n{extracted_text}\n\n"
        formatted_text += f"## Análisis del texto:\n\n{analisis_texto(extracted_text)}"

        # Devolver el texto formateado en Markdown
        return {"text": formatted_text}
    except Exception as e:
        return {"error": str(e)}

# Ejecutar la aplicación (si corres el archivo directamente)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
