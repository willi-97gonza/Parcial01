# EJERCICIO ESTRUCTURAL

## Descripción

Esta función `suma_lista` recibe una lista de números y calcula la suma total de sus elementos. Luego, determina si la suma es mayor o menor que 100, devolviendo `'mayor'` o `'menor'` respectivamente.

## Código
```

def suma_lista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    if resultado > 100:
        return 'mayor'
    else
        return 'menor'
```

## Error y Correccion
#### Al ejecutar el codigo el mismo terminal nos dice la linea en la cual se presenta el error, en este caso se presentaba un error porque despues de un Else no habian los dos puntos ":". En este caso, al faltar el :, Python no sabe dónde empieza el bloque del else y lanza un error de sintaxis.
## CODIGO CORREGIDO
```
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
```
#### Otra cosa que debemos hacer para poder ejecutar el codigo y ver los resultados de nuestra operacion, es agregarle unos datos en este caso los llamaremos "listas de prueba" los cuales luego imprimiremos en la terminal y ahi verificamos que el codigo este sirviendo, el codigo correcto debe mostrarnos algo como:
- Suma de [50, 30, 40] es mayor
- Suma de [10, 20, 30] es menor

# EJERCICIO OOP

## Descripción

Este pequeño sistema modela una jerarquía de clases donde:

- `Persona` representa a una persona con `nombre` y `edad`, y puede verificar si es mayor de edad.
- `Empleado` hereda de `Persona` y además incluye un atributo adicional: `salario`.

Este modelo es útil como base para sistemas de recursos humanos o gestión de empleados.

## Código
```

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def es_mayor(self):
        if self.edad >= 18:
            return True
        return False

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
    self.salario = salario
```

## Error y Correccion
#### En la implementación original, la clase Empleado no llamaba al constructor de la clase padre (Persona). Esto causaba que los atributos nombre y edad no existieran en las instancias de Empleado. Este error fue detectado porque al intentar usar el atributo nombre o edad en una instancia de Empleado, se lanza un AttributeError, para solucionar el problema Se agregó una llamada al constructor de la clase base usando "super()." Esto asegura que los atributos nombre y edad definidos en la clase Persona se inicialicen correctamente en objetos de tipo Empleado.
## CODIGO CORREGIDO
#CODIGO CORREGIDO
```
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor(self):
        if self.edad >= 18:
            return True
        return False

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # ← llamada al constructor de Persona
        self.salario = salario
        
# Casos de prueba

persona1 = Persona("Ana", 17)
persona2 = Persona("Luis", 21)

empleado1 = Empleado("Carlos", 25, 1500)
empleado2 = Empleado("Marta", 16, 1200)

personas = [persona1, persona2, empleado1, empleado2]

for p in personas:
    mayor = p.es_mayor()
    tipo = p.__class__.__name__
    print(f"{tipo} {p.nombre} tiene {p.edad} años. ¿Es mayor de edad? {mayor}")
```
#### Al igual que en el caso anterior para verificar que el codigo este funcionando satisfactoriamente debemos darle unos datos los cuales pueda usar e imprimir, en este caso seran llamados " Casos de prueba" a los cuales les asignaremos un valor y luego imprimiremos en terminal, obteniendo:
- Persona Ana tiene 17 años. ¿Es mayor de edad? False
- Persona Luis tiene 21 años. ¿Es mayor de edad? True
- Empleado Carlos tiene 25 años. ¿Es mayor de edad? True
- Empleado Marta tiene 16 años. ¿Es mayor de edad? False
