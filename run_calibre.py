import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def listar_recetas():
    try:
        result = subprocess.run(
            ['calibre', 'fetch-ebook', '--list-recipes'],
            capture_output=True, text=True, check=True
        )
        logging.info("Recetas disponibles:\n%s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Error al listar recetas: %s\n%s", e, e.stderr)

def main():
    logging.info("Comprobando recetas disponibles en Calibre...")
    listar_recetas()

    # Aquí pondrás la lógica para llamar a tus funciones de descarga y envío
    # Por ejemplo:
    # from download_and_send import descargar_y_enviar
    # descargar_y_enviar()

if __name__ == "__main__":
    main()
