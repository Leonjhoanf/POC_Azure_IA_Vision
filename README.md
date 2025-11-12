# PoC: Azure AI Vision con Flask

Este es un proyecto de prueba de concepto (PoC) que demuestra cómo usar el servicio **Azure AI Vision** (antes Computer Vision) para analizar imágenes.

Es una aplicación web simple construida con **Flask** (Python) que corre en `localhost` y te permite subir una imagen. Luego, puedes seleccionar qué tipo de análisis realizar, como generar una descripción o extraer texto (OCR).

![Captura de pantalla de la aplicación web](https://i.imgur.com/URL_DE_TU_IMAGEN.png)
*(Reemplaza la URL de arriba con una captura de pantalla de tu app funcionando)*

---

## 🚀 Características

* **Subida de Archivos:** Permite subir imágenes (PNG, JPG) desde tu computador.
* **Análisis Dinámico:** Puedes elegir qué analizar antes de enviar la imagen:
    * **Describir la Imagen:** Genera una descripción en lenguaje natural de lo que hay en la imagen (usando `Caption`).
    * **Leer Texto (OCR):** Extrae todo el texto legible de la imagen (usando `Read`).
* **Interfaz Web Local:** Corre en `http://127.0.0.1:5000` gracias a Flask.
* **Manejo Seguro de Claves:** Carga las credenciales de Azure de forma segura desde un archivo `.env` (no incluido en el repositorio).

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3, Flask
* **Cloud Service:** Azure AI Vision SDK (`azure-ai-vision-imageanalysis`)
* **Frontend:** HTML5, CSS, JavaScript (Fetch API)
* **Dependencias:** `python-dotenv` (para manejo de variables de entorno)

---

## ⚙️ Instalación y Ejecución Local

Sigue estos pasos para correr el proyecto en tu máquina local.

### 1. Prerrequisitos

* Python 3.10 o superior.
* Una cuenta de **Azure** con un recurso de **Servicios de Azure AI** (o "Visión") creado. Necesitarás tu **Endpoint** y tu **Clave (Key)**.

### 2. Clonar el Repositorio

```bash
git clone [https://github.com/Leonjhoanf/POC_Azure_IA_Vision.git](https://github.com/Leonjhoanf/POC_Azure_IA_Vision.git)
cd POC_Azure_IA_Vision
