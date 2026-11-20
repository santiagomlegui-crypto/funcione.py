# Ejercicio 3: Número primo
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:          # equivale a i <= raíz cuadrada de n
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input("Ingrese un número: "))
print(es_primo(n))
