import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

RECIPES = [
    "Orbyt - El Mundo.recipe",
    "Orbyt - Expansión.recipe",
    "Financial Times.recipe"
]

def process_recipe(recipe_name):
    try:
        logging.info(f"Iniciando proceso con receta: {recipe_name}")
        safe_name = recipe_name.replace(".recipe", "").strip()
        out_path = os.path.join("/app/output", f"{safe_name}.epub")

        subprocess.run([
            "ebook-convert", recipe_name, out_path, "--output-profile", "kindle"
        ], check=True)

        logging.info(f"Receta {recipe_name} completada correctamente.")
    except subprocess.CalledProcessError as e:
        logging.warning(f"Advertencia: La receta {recipe_name} falló con error: {e}. Continuando con la siguiente.")
    except Exception as e:
        logging.error(f"Error inesperado con {recipe_name}: {e}. Continuando.")

def main():
    for recipe in RECIPES:
        process_recipe(recipe)
    # Aquí puedes invocar envío por email si lo tienes configurado

if __name__ == "__main__":
    main()

