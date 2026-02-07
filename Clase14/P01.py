# Divisor Seguro

def dividir(a, b):
    """Divide a entre b de forma segura."""
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return None
    
# Pruebas

print(dividir(10, 2))   
print(dividir(10, 0))   
print(dividir(15, 3))   
