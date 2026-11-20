# Ejercicio 10: MCD y MCM
def mcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b           # algoritmo de Euclides
    return a


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)


a = int(input("a: "))
b = int(input("b: "))
print("MCD:", mcd(a, b))
print("MCM:", mcm(a, b))
