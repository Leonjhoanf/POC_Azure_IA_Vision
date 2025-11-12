import os
from flask import Flask, render_template, request, jsonify
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import traceback 

# Carga las variables del archivo .env al entorno
load_dotenv()

# --- Configuración de Azure ---
endpoint = os.environ.get("AZURE_VISION_ENDPOINT")
key = os.environ.get("AZURE_VISION_KEY")

if not endpoint or not key:
    print("Error: Credenciales de Azure no encontradas en .env")
    exit()

# 1. Inicializar el cliente de Azure
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# 2. Inicializar la aplicación Flask
app = Flask(__name__)

# 3. Ruta principal (la página web)
@app.route('/')
def home():
    """Sirve la página HTML principal (index.html)"""
    return render_template('index.html')

# 4. Ruta de la API de análisis
@app.route('/analizar', methods=['POST'])
def analizar_imagen_api():
    """Recibe la imagen y las opciones, la analiza y devuelve un JSON."""
    
    if 'file' not in request.files:
        return jsonify({"error": "No se encontró el archivo"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó archivo"}), 400

    try:
        # --- NUEVO: Leer las opciones del formulario ---
        quiere_descripcion = request.form.get('describir') == 'true'
        quiere_leer_texto = request.form.get('leer_texto') == 'true'

        # --- NUEVO: Construir la lista de features dinámicamente ---
        features = []
        if quiere_descripcion:
            features.append(VisualFeatures.CAPTION)
        if quiere_leer_texto:
            features.append(VisualFeatures.READ)

        if not features:
            return jsonify({"error": "No se seleccionó ninguna opción de análisis."}), 400

        # Leer los datos de la imagen
        imagen_data = file.read()

        # Llamar a la API de Azure solo con las features solicitadas
        result = client.analyze(
            image_data=imagen_data,
            visual_features=features
        )

        # --- Procesar los resultados (solo si se pidieron) ---
        
        caption = None
        if quiere_descripcion and result.caption is not None:
            caption = f"'{result.caption.text}' (Confianza: {result.caption.confidence:.4f})"
        
        texto_encontrado = None
        if quiere_leer_texto and result.read is not None:
            texto_encontrado = []
            if result.read.blocks:
                for block in result.read.blocks:
                    for line in block.lines:
                        texto_encontrado.append(line.text)

        # Devolver un JSON con los resultados
        return jsonify({
            "descripcion": caption,
            "texto_detectado": texto_encontrado
        })

    except Exception as e:
        print(f"!!! ERROR CAPTURADO: {e}")
        traceback.print_exc()
        return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500


# 5. Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)