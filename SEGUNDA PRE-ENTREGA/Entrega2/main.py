from paquete1.modulo1 import *
from paquete1.modulo2 import Cliente


# Crear clientes
cliente1 = Cliente("Juan Pablo", "Menichetti", 30, "jpmenichetti13@gmail.com", "Calle San Lorenzo 500", 1000)
cliente2 = Cliente("Santiago","Molina", 25, "santimome@gmail.com", "El Cardenal 1250", 1500)
cliente3 = Cliente("Carlos", "Molina", 17,"carlosmolina@gmail.com", "Islas Malvinas 800", 3000)

# Mostrar información de los clientes
print(cliente1)
print(cliente2)
print(cliente3)

# Realizar compras y agregar saldo
print(cliente1.comprar(500))
print(cliente2.agregar_saldo(200))
print(cliente3.comprar(1200))