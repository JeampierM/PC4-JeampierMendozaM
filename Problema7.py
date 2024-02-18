import requests
import sqlite3
from datetime import date, timedelta

def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    response = requests.get(url)
    data = response.json()
    dolar_compra = data['compra']
    dolar_venta = data['venta']
    return dolar_compra, dolar_venta

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        FECHA TEXT PRIMARY KEY,
                        COMPRA REAL,
                        VENTA REAL
                    )''')

def insertar_datos(conn, fecha, dolar_compra, dolar_venta):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sunat_info (FECHA, COMPRA, VENTA) VALUES (?, ?, ?)", (fecha, dolar_compra, dolar_venta))

def obtener_registros():
    with sqlite3.connect('base.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM sunat_info")
        usuarios = cursor.fetchall()
    return usuarios

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def main():
    # Conectando a la base de datos SQLite
    with sqlite3.connect('base.db') as conn:
        crear_tabla(conn)

        inicio = date(2023, 1, 1)
        fin = date(2023, 12, 31)

        delta = timedelta(days=1)
        fecha_actual = inicio

        while fecha_actual <= fin:
            dolar_compra, dolar_venta = obtener_tipo_cambio(fecha_actual.strftime('%Y-%m-%d'))
       
            insertar_datos(conn, fecha_actual.strftime('%Y-%m-%d'), dolar_compra, dolar_venta)
          
            fecha_actual += delta

    print("Los datos fueron guardados con exito en la base de datos 'base.db'")

    usuarios = obtener_registros()
    mostrar_usuarios(usuarios)

if __name__ == "__main__":
    main()
