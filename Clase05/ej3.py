#ejercicio 3
#Mayor de edad

Nombre = input('Cual es tu nombre ')
edad = int(input('Cual es tu edad?'))
            
if edad >= 18:
    print(f'Hola {Nombre}, eres mayor de edad')
else:
    print(f'Lo siento mucho {Nombre}, no eres mayor de edad')
    print('NO PUEDES INGRESAR')
