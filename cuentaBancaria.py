# Operaciones Bancarias

from os import system


clientesNuevos = []

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
        canti = int(cantidad)
        self.saldo = self.saldo + canti
        print(f"Su nuevo saldo es {self.saldo}")
        
    def retirar(self, cantidad):
        canti = int(cantidad)
        if canti > self.saldo:
            print(f"El valor que intenta retirar es mayor al asignado {self.saldo}")
        else:
            self.saldo = self.saldo - cantidad
            print(f"Su nuevo saldo es {self.saldo}")

# ? Funcion de crear cliente

def crearCliente():
    print("Ingresa los datos para crear un nuevo cliente")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    numeroCuenta = input("Ingrese el numero de Cuenta: ")
    saldo = input("Ingrese el saldo inicial: ")
    clienteNuevo = Cliente(nombre, apellido, numeroCuenta, int(saldo))
    clientesNuevos.append(clienteNuevo)
    print(f"Se agrego el cliente {clienteNuevo.nombre} {clienteNuevo.apellido}")
    
# ? Funcion de inicio

def inicio():
    # Vamos a limpiar la pantalla primero
    system('cls')
    print("*" * 50)
    print('*' * 5 + "Bienvenido al administrador de recetas" + '*' * 5)
    print("*" * 50)
    eleccion_menu = 'x'
    # Mientras la eleccion no sea numerica o que el numero no este en el rango indicado entonces:
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 6):
        print("Elige una opcion:")
        print('''
            [1] - Crear Cliente
            [2] - Ver datos de Clientes
            [3] - Depositar saldo en cliente
            [4] - Retirar saldo del cliente
            [5] - Finalizar programa
            ''')
        eleccion_menu = input()
    return int(eleccion_menu)


# ? Ver nombres de todos los clientes

def verNombres():
    contador = 1 
    if clientesNuevos == []:
        print("Aun no se han creado clientes")
    else:
        for nombres in clientesNuevos:
            print(f"{contador} {nombres.nombre} {nombres.apellido}")
            contador = contador + 1
    opcion = input("Escoge el cliente: ")
    return int(opcion)
    
# ? Elegir cliente

def verDatos(num):
    opcion = num - 1
    hola = 0
    for x in clientesNuevos:
        if opcion == hola:
            return x.datosCliente()
        else:
            hola = hola + 1

finalizar = False


while not finalizar:
    eleccionOpcion = inicio()
    
    # ! Crear cliente
    if eleccionOpcion == 1:
        # crear cliente
        crearCliente()
        # Inicio
        valor = input("Ingrese la v para volver al inicio:")
        if valor == "v":
            inicio()
        

    # ! Ver datos de Clientes
    elif eleccionOpcion == 2:
        # Ver nombres de los clientes
        cliente = verNombres()
        # ver datos del cliente
        verDatos(cliente)
        # Inicio
        valor = input("Ingrese la v para volver al inicio:")
        if valor == "v":
            inicio()

    # ! Depositar en cliente
    elif eleccionOpcion == 3:
        # Ver nombres de los clientes
        cliente = verNombres()
        cliente = cliente - 1
        # Depositar saldo en cliente
        can = input("Ingrese el monto: ")
        clientesNuevos[cliente].depositar(int(can))
        # inicio
        valor = input("Ingrese la v para volver al inicio:")
        if valor == "v":
            inicio()

    # ! Retirar saldo de cliente
    elif eleccionOpcion == 4:
        # Ver nombres de los clientes
        cliente = verNombres()
        cliente = cliente - 1
        # Retirar saldo en cliente
        can = input("Ingrese el monto a retirar: ")
        clientesNuevos[cliente].retirar(int(can))
        # inicio
        valor = input("Ingrese la v para volver al inicio:")
        if valor == "v":
            inicio()

    # ! Finalizar programa
    elif eleccionOpcion == 5:
        # Salir del programa
        finalizar = True
