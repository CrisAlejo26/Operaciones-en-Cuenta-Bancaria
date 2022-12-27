# Operaciones Bancarias

# ! Clase persona

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        

# ! Clase Cliente

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numeroCuenta, saldo):
        super().__init__(nombre, apellido)
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def datosCliente(self):
        print(f'''El nombre del cliente es: {self.nombre} {self.apellido}
            Su numero de cuenta es: {self.numeroCuenta}
            Su saldo actual es: {self.saldo}''')
    
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Su nuevo saldo es {self.saldo}")
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"El valor que intenta retirar es mayor al asignado {self.saldo}")
        else:
            self.saldo = self.saldo - cantidad

# ? Funciones de crear cliente, inicio

def crearCliente(nombre, apellido, numeroCuenta, saldo):
    pass

# ! codigo para elegir depositar, retirar o salir

eleccionOpcion = 0

# ! Crear cliente
if eleccionOpcion == 1:
    # crear cliente
    # Inicio
    pass

# ! Ver datos de Clientes
if eleccionOpcion == 2:
    # Ver nombres de los clientes
    # elegir el cliente
    # ver datos del cliente
    # Inicio
    pass

# ! Depositar en cliente
if eleccionOpcion == 3:
    # Ver nombres de los clientes
    # elegir el cliente
    # Depositar saldo en cliente
    # inicio
    pass

# ! Retirar saldo de cliente
if eleccionOpcion == 4:
    # Ver nombres de los clientes
    # elegir el cliente
    # Retirar saldo en cliente
    # inicio
    pass

# ! Finalizar programa
if eleccionOpcion == 5:
    # Salir del programa