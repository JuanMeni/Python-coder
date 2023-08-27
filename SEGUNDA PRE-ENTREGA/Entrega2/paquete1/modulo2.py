class Cliente:
    def __init__(self, nombre, apellido, edad, email, direccion, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.direccion = direccion
        self.saldo = saldo

    def es_mayor_de_edad(self):
        return self.edad >=18
    
    def comprar(self, monto):
        if self.es_mayor_de_edad():
            if self.saldo >= monto:
                self.saldo -= monto
                return f"{self.nombre} {self.apellido} ha realizado una compra de ${monto}. Saldo restante: ${self.saldo}"
            else:
                return f"{self.nombre} {self.apellido}  no tiene saldo suficiente para esta compra."
        else:
            return f"{self.nombre} {self.apellido} debe ser mayor de edad para continuar con la compra"
    
    def agregar_saldo(self, cantidad):
        self.saldo += cantidad
        return f"Se han agregado ${cantidad} al saldo de {self.nombre}. Saldo actual: ${self.saldo}"
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \nEmail: {self.email}\nDirección: {self.direccion}\nSaldo: ${self.saldo}"
