import requests
from io import BytesIO
import zipfile

def descargar_imagen(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Retornando los bytes de la imagen descargada
        imagen_bytes = response.content
        print("Imagen descargada con éxito.")
        return imagen_bytes
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return None

def guardar_imagen_como_zip(imagen_bytes, nombre_archivo_zip):
    try:
        with zipfile.ZipFile(nombre_archivo_zip, 'w') as zip_file:
            # Agregando la imagen al archivo ZIP con su nombre dentro del ZIP
            zip_file.writestr("imagen_descargada.jpg", imagen_bytes)
        print(f"Imagen guardada como {nombre_archivo_zip} con éxito.")
    except Exception as e:
        print(f"Error al guardar la imagen como archivo ZIP: {e}")

def extraer_zip(archivo_zip, directorio_destino):
    try:
        with zipfile.ZipFile(archivo_zip, 'r') as zip_file:
            # Extrayendo todo el contenido del ZIP en el directorio especificado
            zip_file.extractall(directorio_destino)
        print(f"Contenido del archivo ZIP extraído en {directorio_destino} con éxito.")
    except Exception as e:
        print(f"Error al extraer el archivo ZIP: {e}")

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

    # Descargando la imagen
    imagen_bytes = descargar_imagen(url_imagen)

    if imagen_bytes is not None:
        # Guardando la imagen como archivo ZIP
        nombre_archivo_zip = "imagen_descargada.zip"
        guardar_imagen_como_zip(imagen_bytes, nombre_archivo_zip)

        # Extrayendo el contenido del archivo ZIP
        directorio_destino = "imagen_extraida"
        extraer_zip(nombre_archivo_zip, directorio_destino)

if __name__ == "__main__":
    main()
