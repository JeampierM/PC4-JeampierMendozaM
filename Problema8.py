import sqlite3
import requests
from datetime import date

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        return response.json()["bpi"]
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def obtener_tipo_cambio_sunat(fecha):
    try:
        url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['compra']
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio:", e)
        return None

def crear_tabla_bitcoin(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        FECHA TEXT PRIMARY KEY,
                        PRECIO_USD REAL,
                        PRECIO_GBP REAL,
                        PRECIO_EUR REAL,
                        PRECIO_PEN REAL
                    )''')

def insertar_datos_bitcoin(conn, fecha, precios_bitcoin, tipo_cambio_usd):
    cursor = conn.cursor()
    precio_pen = precios_bitcoin['USD']['rate_float'] * tipo_cambio_usd
    cursor.execute("INSERT INTO bitcoin (FECHA, PRECIO_USD, PRECIO_GBP, PRECIO_EUR, PRECIO_PEN) VALUES (?, ?, ?, ?, ?)",
                   (fecha, precios_bitcoin['USD']['rate_float'], precios_bitcoin['GBP']['rate_float'], 
                    precios_bitcoin['EUR']['rate_float'], precio_pen))

def guardar_precio_bitcoin_en_db():
    precios_bitcoin = obtener_precio_bitcoin()
    if precios_bitcoin is None:
        return
    
    fecha_actual = date.today().strftime('%Y-%m-%d')
    tipo_cambio_usd = obtener_tipo_cambio_sunat(fecha_actual)
    if tipo_cambio_usd is None:
        return
    
    conn = sqlite3.connect('base.db')
    crear_tabla_bitcoin(conn)
    insertar_datos_bitcoin(conn, fecha_actual, precios_bitcoin, tipo_cambio_usd)
    
    conn.commit()
    conn.close()
    
    print("Datos de Bitcoin guardados en la tabla 'bitcoin' de la base de datos 'base.db'")

def obtener_registros_bitcoin():
    with sqlite3.connect('base.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM bitcoin")
        registros_bitcoin = cursor.fetchall()
    return registros_bitcoin

def mostrar_registros_bitcoin(registros_bitcoin):
    for registro in registros_bitcoin:
        print(registro)

def calcular_precio_compra(bitcoins, moneda):
    try:
        with sqlite3.connect('base.db') as conn:
            cursor = conn.cursor()

            # Consultando el precio actual del bitcoin
            cursor.execute(f"SELECT PRECIO_{moneda.upper()} FROM bitcoin ORDER BY FECHA DESC LIMIT 1")
            precio_bitcoin = cursor.fetchone()[0] 

            # Calculando el precio de compra de los bitcoins 
            precio_compra = bitcoins * precio_bitcoin

        return precio_compra

    except (sqlite3.Error, IndexError) as e:
        print(f"Error al calcular el precio de compra: {e}")
        return None

guardar_precio_bitcoin_en_db()

registros_bitcoin = obtener_registros_bitcoin()
mostrar_registros_bitcoin(registros_bitcoin)

precio_compra_pen = calcular_precio_compra(10, 'PEN')
if precio_compra_pen is not None:
    print(f"El precio de compra de 10 bitcoins en PEN es: {precio_compra_pen:.2f} PEN")

precio_compra_eur = calcular_precio_compra(10, 'EUR')
if precio_compra_eur is not None:
    print(f"El precio de compra de 10 bitcoins en EUR es: {precio_compra_eur:.2f} EUR")
