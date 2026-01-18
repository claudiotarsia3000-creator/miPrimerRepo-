#Formulario con Condicional e IF

#Pido datos
nombre = "Claudio"
edad = float(input("Cual es tu edad  "))

#Muestro por consola
print("Hola " + nombre + " ...")

#Condicional MAYOR O IGUAL A 18
if edad >= 18:
    print("""Eres mayor de edad
          
APARENTEMENTE         
PUEDES PASAR""")
    #SI NO ES MAYOR, MUESTRO ESTO
else:
    print("ERES MENOR DE EDAD\nACCESO DENEGADO")