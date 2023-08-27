mi_lista=["Veronica","Menichetti",37,True,["Jujuy","Salta","Tucuman","Santiago"]]
mi_tupla=("Veronica","Menichetti",37,True,["Jujuy","Salta","Tucuman","Santiago"])

mi_tupla[-1][0]="Cordoba"
mi_lista2=list(mi_tupla)

mi_lista2.append(50)

mi_lista3=list(mi_lista2)

print(mi_tupla)
print(mi_lista2)
print(mi_lista3)