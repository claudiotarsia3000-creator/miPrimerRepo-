#Pedir Notas

Nombre = input('Ingrese su Nombre ')
Nota = float (input('Cual es su nota '))

if Nota >= 90:
    print ('Su Clasificacion es A')
elif Nota >=80:
    print ('Su Clasificacion es B ')
elif Nota >=60:
    print ('Su Clasificacion es C ')
elif Nota >=20:
    print ('Su Clasificacion es D ')
else:
    print('Su Clasificacion es F')

