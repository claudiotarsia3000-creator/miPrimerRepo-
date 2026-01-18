#password

password = input("Seleccione su Password: ")

#verificarPass
longitud_ok = len(password) >=8
no_password = password != "password"
no_numeros = password != "12345678"

#condicionales para que el PASS sea VALIDO
password_valido = longitud_ok and no_password and no_numeros

print (f"""   THE PASSWORD 
   ES VALIDO: {password_valido}""")
