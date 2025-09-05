#AI-TRAP:OOP
# Este ejercicio simula operaciones bancarias, útil en sistemas de gestión financiera o aplicaciones de banca digital.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad < self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            print('Fondos insuficientes')

c = CuentaBancaria('Ana', 100)
c.retirar(150)
