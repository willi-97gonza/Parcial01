#AI-TRAP:ESTRUCTURAL
# Este ejercicio simula el procesamiento de una lista de datos, como sumar ventas diarias o calcular totales en reportes financieros.
"""
#CODIGO DEL PARCIAL
def suma_lista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    if resultado > 100:
        return 'mayor'
    else
        return 'menor'
"""
#CODIGO CORREGIDO
def suma_lista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    if resultado > 100:
        return 'mayor'
    else:
        return 'menor'
# Casos de prueba
listas_de_prueba = [
    [50, 30, 40],    # suma = 120 > 100 -> 'mayor'
    [10, 20, 30],    # suma = 60 <= 100 -> 'menor'
]
for lista in listas_de_prueba:
    resultado = suma_lista(lista)
    print(f"Suma de {lista} es {resultado}")