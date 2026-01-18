# Formulario Estilizado

print("=" * 40)
print("     ✨ MI PRIMER FORMULARIO ✨")
print("=" * 40)

# Pido datos (añado ":" y espacios para que se vea ordenado al escribir)
nombre = input("👉 Nombre completo: ")
edad = int(input("👉 Edad:            "))
ciudad = input("👉 Ciudad:          ")
pais = input("👉 País:            ")

# Muestro por consola con formato de "Ficha"
print("\n" + "║" + "═" * 38 + "║")
print("║       RESUMEN DE REGISTRO            ║")
print("║" + "═" * 38 + "║")

# Usamos f-strings con alineación (el :<20 le da 20 espacios de ancho)
print(f"║  NOMBRE:  {nombre:<26} ║")
print(f"║  EDAD:    {edad:<26} ║")
print(f"║  CIUDAD:  {ciudad:<26} ║")
print(f"║  PAÍS:    {pais:<26} ║")

print("╚" + "═" * 38 + "╝")
print("\n¡Datos guardados con éxito! 🚀")