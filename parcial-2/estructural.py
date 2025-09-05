#AI-TRAP:ESTRUCTURAL
# Este ejercicio se puede aplicar para encontrar el valor máximo en una serie de mediciones, como temperaturas o puntuaciones.

def maximo(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

nums = [3, 7, 2, 9, 5]
print(maximo(nums)
