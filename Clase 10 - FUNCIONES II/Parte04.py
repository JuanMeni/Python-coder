mi_lista = [[2,8,-5,24],[1,3,5,7]]
mi_numero=5

mi_lista2=mi_lista.copy()
mi_lista3=mi_lista

def cambia_valores(matriz):
    for fila in matriz:
        fila.append(0)

cambia_valores(mi_lista3)

print(mi_lista)
print(mi_lista2)
print(mi_lista3)