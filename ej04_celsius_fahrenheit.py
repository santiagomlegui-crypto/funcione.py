# Ejercicio 4: Celsius a Fahrenheit
def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32


c = float(input("Grados Celsius: "))
print(f"{c} °C = {celsius_fahrenheit(c)} °F")
