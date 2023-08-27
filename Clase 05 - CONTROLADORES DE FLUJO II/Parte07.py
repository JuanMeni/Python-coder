# Dada la lista de paises, armar un programa que obtenga la posicion del pais con el nombre mas largo

paises=["Canada","USA","Mexico","Australia","Argentina","China","India","Singapur","Croacia","Corea del Sur"]
candidato=paises[0]

for pos,pais in enumerate(paises):
    if len(pais)>len(candidato):
        candidato=pais
        pos_candidato=pos
print(pos_candidato)

    