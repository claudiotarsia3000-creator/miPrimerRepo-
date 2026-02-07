import requests

url = "https://rickandmortyapi.com/api/character/5"

try:
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()  # lanza HTTPError si no es 200-299

    datos = respuesta.json()

    print(f"El personaje es: {datos.get('name', 'Desconocido')}")
    print(f"Especie: {datos.get('species', 'Desconocida')}")
    print(f"Estado: {datos.get('status', 'Desconocido')}")

except requests.exceptions.Timeout:
    print("❌ Se agotó el tiempo de espera (timeout).")
except requests.exceptions.ConnectionError:
    print("❌ No se pudo conectar. ¿Tenés internet o estás bloqueado por proxy/firewall?")
except requests.exceptions.HTTPError as e:
    print(f"❌ Error HTTP: {e} (status {respuesta.status_code})")
except ValueError:
    print("❌ La respuesta no era JSON válido.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")