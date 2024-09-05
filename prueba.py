print("esto es una prueba")

# Calcula la suma de todos los múltiplos de 3 o 5 por debajo de 1000

def suma_multiplos(limite):
    suma = 0
    for numero in range(1, limite):
        if numero % 3 == 0 or numero % 5 == 0:
            suma += numero
    return suma

resultado = suma_multiplos(1000)
print("La suma de los múltiplos de 3 o 5 por debajo de 1000 es:", resultado)
