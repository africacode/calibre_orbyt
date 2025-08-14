import os
import subprocess
import logging

def descargar_y_enviar():
    # Variables de entorno
    ORBYT_USER = os.getenv('ORBYT_USER')
    ORBYT_PASS = os.getenv('ORBYT_PASS')
    EMAIL_FROM = os.getenv('EMAIL_FROM')
    EMAIL_PASS = os.getenv('EMAIL_PASS')
    EMAIL_TO = os.getenv('EMAIL_TO')

    if not all([ORBYT_USER, ORBYT_PASS, EMAIL_FROM, EMAIL_PASS, EMAIL_TO]):
        logging.error("Faltan variables de entorno necesarias.")
        return

    receta = "Orbyt - El Mundo.recipe"
    salida = "/app/output/el_mundo.epub"

    try:
        logging.info(f"Descargando ebook con receta {receta}...")
        cmd = [
            "ebook-convert", receta, salida,
            "--username", ORBYT_USER,
            "--password", ORBYT_PASS
        ]
        subprocess.run(cmd, check=True)
        logging.info("Descarga completada.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error descargando con la receta {receta}: {e}")
        return

    # Aquí pondrías la lógica para enviar por email el archivo descargado

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    descargar_y_enviar()

