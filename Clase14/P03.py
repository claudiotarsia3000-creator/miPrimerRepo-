# Acceso Seguro a Diccionario

def obtener_valor(diccionario, clave, valor_defecto=None):

    """Obtiene valor de diccionario de forma segura."""

    try:
        return diccionario[clave]
    except KeyError:
        print(f"Clave '{clave}' no encontrada. Usando valor defecto.")
        return valor_defecto
    

# Pruebas
datos = {"nombre": "Ana", "edad": 25}
print(obtener_valor(datos, "nombre"))          # "Ana"
print(obtener_valor(datos, "telefono", "N/A")) # "N/A"
print(obtener_valor(datos, "ciudad", "Desconocida"))  # "Desconocida"