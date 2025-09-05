#AI-TRAP:OOP
# Este ejercicio representa el modelado de personas y empleados, útil en sistemas de gestión de recursos humanos o nómina.

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
