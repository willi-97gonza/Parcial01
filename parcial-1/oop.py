#AI-TRAP:OOP
# Este ejercicio representa el modelado de personas y empleados, útil en sistemas de gestión de recursos humanos o nómina.
"""
#CODIGO DEL PARCIAL
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
"""
#CODIGO CORREGIDO
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
