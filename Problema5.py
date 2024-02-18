def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                resultado = numero * i
                archivo.write(f"{numero} x {i} = {resultado}\n")
        print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar del {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al leer la tabla de multiplicar: {e}")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(f"Línea {linea}: {lineas[linea - 1]}")
            else:
                print(f"Línea {linea} fuera de rango.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al leer la línea de la tabla de multiplicar: {e}")

def main():
    while True:
        try:
            opcion = int(input("\nMENU:\n------\n1. Guardar tabla de multiplicar\n2. Mostrar tabla de multiplicar\n3. Mostrar línea de la tabla de multiplicar\n4. Salir\nDigite una opcion: "))
            
            if opcion == 1:
                numero = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= numero <= 10:
                    guardar_tabla_multiplicar(numero)
                else:
                    print("Número fuera de rango. Intente de nuevo")
            elif opcion == 2:
                numero = int(input("Ingrese un número entre 1 y 10: "))
                if 1 <= numero <= 10:
                    mostrar_tabla_multiplicar(numero)
                else:
                    print("Número fuera de rango. Intente de nuevo")
            elif opcion == 3:
                numero = int(input("Ingrese un número entre 1 y 10: "))
                linea = int(input("Ingrese el número de línea que desea que se muestre: "))
                if 1 <= numero <= 10:
                    mostrar_linea_tabla_multiplicar(numero, linea)
                else:
                    print("Número fuera de rango. Intente de nuevo")
            elif opcion == 4:
                break
            else:
                print("Opción inválida. Intente de nuevo")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido")

if __name__ == "__main__":
    main()
