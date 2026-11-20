# Ejercicio 7: Invertir una cadena (recursivo, sin slicing)
def invertir(cadena, indice=0):
    if indice == len(cadena):
        return ""
    return invertir(cadena, indice + 1) + cadena[indice]


cadena = input("Cadena: ")
print(invertir(cadena))
