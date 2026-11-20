# Ejercicio 8: Palíndromo
def invertir(cadena, indice=0):
    if indice == len(cadena):
        return ""
    return invertir(cadena, indice + 1) + cadena[indice]


def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    invertida = invertir(cadena)
    for i in range(len(cadena)):          # comparación carácter por carácter
        if cadena[i] != invertida[i]:
            return False
    return True


cadena = input("Cadena: ")
print(es_palindromo(cadena))
