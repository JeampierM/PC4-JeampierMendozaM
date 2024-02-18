# Previo al problema se instaló la librería pyfiglet en la terminal

from pyfiglet import Figlet
import random

def obtener_fuente_usuario():
    fuente = input("Ingrese el nombre de la fuente, o deje en blanco para una seleccion aleatoria: ").strip()
    return fuente if fuente else None

def obtener_texto_usuario():
    return input("Ingrese un texto que desea imprimir: ")

def main():
    figlet = Figlet()

    # Obteniendo las fuentes disponibles
    fuentes_disponibles = figlet.getFonts()

    while True:
        fuente_usuario = obtener_fuente_usuario()

        if fuente_usuario is None:
            fuente_seleccionada = random.choice(fuentes_disponibles)
            break
        elif fuente_usuario in fuentes_disponibles:
            fuente_seleccionada = fuente_usuario
            break
        else:
            print("Fuente no válida. Intenta de nuevo")

    texto_usuario = obtener_texto_usuario()

    # Estableciendo la fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)

    print(figlet.renderText(texto_usuario))

if __name__ == "__main__":
    main()
