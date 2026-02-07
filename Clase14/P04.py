#Lector de Archivos Multiples

def leer_archivos(lista_nombres):

    """Lee multiples archivos manejando errores."""
    resultado = {}
    for nombre in lista_nombres:
        try:
            with open(nombre, "r") as f:
                resultado[nombre] = f.read()
        except FileNotFoundError:
            resultado[nombre] = "Error: archivo no encontrado"
        except PermissionError:
            resultado[nombre] = "Error: sin permisos de lectura"
    return resultado

# Pruebas
archivos = ["datos.txt", "no_existe.txt"]
resultado = leer_archivos(archivos)
for nombre, contenido in resultado.items():
    print(f"{nombre}: {contenido[:50]}...")