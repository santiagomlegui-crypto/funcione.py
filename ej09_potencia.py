# Ejercicio 9: Potencia sin usar **
def potencia(base, exponente):
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


base = float(input("Base: "))
exponente = int(input("Exponente (entero): "))
print(f"{base} ^ {exponente} = {potencia(base, exponente)}")
