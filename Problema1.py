import requests

def obtener_precio_bitcoin():
    try:
        # Consultando la API de CoinDesk para obtener el precio actual de Bitcoin en USD
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  

        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd

    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    while True:
        try:
            cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    precio_actual = obtener_precio_bitcoin()

    if precio_actual is not None:
        # Calculando el costo actual en USD
        costo_actual_usd = cantidad_bitcoins * precio_actual

        print(f"El costo actual de {cantidad_bitcoins:.1f} Bitcoins (en USD) es: ${costo_actual_usd:,.4f}")

if __name__ == "__main__":
    main()
