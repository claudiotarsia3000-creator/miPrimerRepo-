# Conversor de Edad

def pedir_edad():

    """Pide edad validando tipo y rango."""

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if 0 <= edad <= 150:
                return edad
            else:
                print("La edad debe estar entre 0 y 150")
        except ValueError:
            print("Debes escribir un numero")
edad = pedir_edad()
print(f"Tu edad es: {edad}")
