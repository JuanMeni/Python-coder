#DICCIONARIO

persona={
    "name":"Mauricio",
    "last name":None,
    "age":None
}

persona["name"]="Mauri"
persona["email"]="mauricio@gmail.com"

persona.update({
    "name":"Mauri",
    "email":"mauricio@gmail.com",
    "city":"General Pico"
})

persona.update([("mail","mauricio@gmail.com",),("city","General Pico")])

print(persona)
