import os
import subprocess
import sys

RECIPES = [
    "Orbyt - El Mundo.recipe",
    "Orbyt - Expansión.recipe",
    "Financial Times.recipe"
]

def check_recipe_list():
    print("Comprobando recetas disponibles en Calibre...")
    try:
        result = subprocess.run(
            ["calibre", "fetch-ebook", "--list-recipes"],
            capture_output=True, text=True, check=True
        )
        available = result.stdout
        print("Recetas disponibles:\n", available)
        for r in RECIPES:
            if r not in available:
                print(f"¡ATENCIÓN! Receta {r} NO encontrada en Calibre.")
    except subprocess.CalledProcessError as e:
        print("Error al listar recetas:", e)
        sys.exit(1)

def download_with_recipe(recipe_name):
    print(f"Descargando con receta: {recipe_name}")
    try:
        subprocess.run(
            ["calibre", "fetch-ebook", "--recipe", recipe_name, "--output", "/app/output"],
            check=True
        )
        print(f"Descarga con receta {recipe_name} completada correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error descargando con receta {recipe_name}: {e}")

def main():
    check_recipe_list()

    for r in ["Orbyt - El Mundo.recipe", "Orbyt - Expansión.recipe"]:
        download_with_recipe(r)

    for r in ["WSJ.recipe", "Financial Times.recipe", "El País.recipe"]:
        download_with_recipe(r)

if __name__ == "__main__":
    main()
