# Ejercicio 5: Máximo de tres números
def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("El máximo es:", maximo_de_tres(a, b, c))
