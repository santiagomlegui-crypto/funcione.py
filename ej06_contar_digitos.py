# Ejercicio 6: Contar dígitos
def contar_digitos(n):
    n = abs(n)
    if n == 0:
        return 1
    cantidad = 0
    while n > 0:
        n //= 10
        cantidad += 1
    return cantidad


n = int(input("Ingrese un entero: "))
print("Cantidad de dígitos:", contar_digitos(n))
