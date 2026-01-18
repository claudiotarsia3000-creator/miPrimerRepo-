user_correct = 'admin'
password_correct = 1234

User = (input('Ingrese su Usuario'))
password = (input('Ingrese su password'))

if user_correct and password_correct == True:
    print('Bienvenido al sistema')
else:
    print ('Credenciales incorrectas')