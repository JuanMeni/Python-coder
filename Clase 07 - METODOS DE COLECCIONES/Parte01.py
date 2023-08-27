frase_original = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

renglones = frase_original.split("&")
frase_resultado = ""

for pos, renglon in enumerate(renglones):
    renglon = renglon.capitalize()
    if pos == 0:    
        frase_resultado += f'{renglon}...\n'
else:
    frase_resultado += f'- {renglon}.\n'
    print(frase_resultado)
    
    """Gordon lanzó su curva...
    - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
    - Dos pies le corrigió Troop.
    - Strawberry menea la cabeza como disgustado… -agrega el comentarista.
    """

