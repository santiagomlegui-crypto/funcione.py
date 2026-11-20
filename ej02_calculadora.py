# Ejercicio 2: Calculadora con funciones independientes
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b


def calculadora():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (+, -, *, /): ")

    if op == "+":
        print("Resultado:", sumar(a, b))
    elif op == "-":
        print("Resultado:", restar(a, b))
    elif op == "*":
        print("Resultado:", multiplicar(a, b))
    elif op == "/":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida")


calculadora()
