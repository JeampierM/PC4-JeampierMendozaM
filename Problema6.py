def contar_lineas_codigo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            lineas_codigo = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith('#')]
            cantidad_lineas_codigo = len(lineas_codigo)
            return cantidad_lineas_codigo
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al contar las líneas de código: {e}")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")

    if not ruta_archivo.endswith(".py"):
        print("El archivo no tiene extensión .py ,el programa no retornará ningún resultado.")
    else:
        cantidad_lineas_codigo = contar_lineas_codigo(ruta_archivo)
        if cantidad_lineas_codigo is not None:
            print(f"El número de líneas de código en {ruta_archivo} es: {cantidad_lineas_codigo}")

if __name__ == "__main__":
    main()
