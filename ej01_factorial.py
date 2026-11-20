# Ejercicio 1: Factorial
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


n = int(input("Ingrese un entero positivo: "))
print(f"{n}! = {factorial(n)}")
