import os
import shutil
from pathlib import Path

# Mapeo de extensión → carpeta destino
REGLAS = {
    ".pdf": "Documentos",
    ".txt": "Documentos",
    ".docx": "Documentos",
    ".jpg": "Imágenes",
    ".png": "Imágenes",
    ".mp3": "Audio",
    ".mp4": "Video",
    ".xlsx": "Hojas de cálculo",
}

def organizar(carpeta_fuente):
    """Mueve archivos de una carpeta a subcarpetas según su extensión."""
    fuente = Path(carpeta_fuente)
    movidos = 0

    for archivo in fuente.iterdir():
        if archivo.is_file():
            ext = archivo.suffix.lower()
            destino_carpeta = REGLAS.get(ext, "Otros")
            destino = fuente / destino_carpeta
            destino.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(destino / archivo.name))
            movidos += 1

    print(f"Se movieron {movidos} archivos.")

if __name__ == "__main__":
    import sys
    carpeta = sys.argv[1] if len(sys.argv) > 1 else "."
    organizar(carpeta)   