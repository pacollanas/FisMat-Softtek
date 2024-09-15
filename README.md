# FisMat-Softtek

Integrantes: Sebastián Zaragoza Díaz, Cedrick Patricio Treviño Ortiz, Daniel Eugenio González Limas, Francisco Javier Llanas Domínguez.

# Propuesta: Automatización de cuentas por pagar en la industria de la construcción.
Este proyecto tiene como objetivo desarrollar una solución automatizada que combine inteligencia artificial generativa (IA GenIA) y visión por computadora para optimizar el proceso de cuentas por pagar en la industria de la construcción. A través de la extracción automática de texto a partir de facturas escaneadas y su posterior clasificación y análisis, la herramienta ofrecerá a las empresas constructoras una forma de gestionar y optimizar su flujo de caja, mejorando la toma de decisiones financieras y reduciendo el tiempo necesario para la gestión de pagos.

# Herramientas utilizadas.
Se hizo uso de la inteligencia artifical proporcionada por Softtek, Frida AI, además de la librería de Python "Pytesseract", la cual es una herramienta de reconocimiento óptico de caracteres (OCR, por sus siglas en inglés) que utiliza la tecnología de inteligencia artificial para convertir imágenes de texto en texto editable. También se utilizó FastAPI, que actúa como una interfaz entre la aplicación de visión por computadora (pytesseract) y los usuarios o sistemas externos. La API recibiría facturas en formato de imagen (escaneadas), procesaría esas imágenes utilizando pytesseract y devolvería el texto extraído hacia una Generative AI para que esta nos pueda arrojar una solución y/o recomendación para automatizar las cuentas a pagar.

![image](https://github.com/user-attachments/assets/c2d685cb-abb8-48d1-8c46-5bd0fafc7963)
![image](https://github.com/user-attachments/assets/2ff2a230-585a-4668-b40e-23cf82a0f97a)
![image](https://github.com/user-attachments/assets/5382765b-7304-427b-8c2c-de715de9e65b)


# Caso de uso específico.
Como objetivo, la IA debe procesar automáticamente las facturas enviadas por los proveedores de materiales, servicios y contratistas, identificando categorías clave como montos pagados, fechas de vencimiento, identificación del proveedor y detalles del proyecto de construcción. Además, debe generar recomendaciones sobre la optimización de pagos, gestión del flujo de caja y posibles mejoras en las relaciones con proveedores basándose en la información extraída.

# Pasos a seguir.
Para poder obtener el texto de la imagen:
1. Clonar el repositorio de manera local al usuario que desee revisar el contenido. (No omitir archivos ya que muchos son dependientes de los otros).
2. Abrir el archivo _. Cuando se esté corriendo, hará uso de el archivo _.
3. 
Para conectar el texto obtenido con...
