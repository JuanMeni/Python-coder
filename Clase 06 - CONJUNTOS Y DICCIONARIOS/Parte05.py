personas = [
{"id":1,"first_name":"Catha","last_name":"Carlton","city":"Qingshandi","email":"ccarlton0@twitter.com","gender":"Polygender"},
{"id":2,"first_name":"Toddie","last_name":"Ibeson","city":"San Juan","email":"tibeson1@freewebs.com","gender":"Bigender"},
{"id":3,"first_name":"Ashlee","last_name":"McAuslan","city":"São Jerônimo","email":"amcauslan2@pcworld.com","gender":"Polygender"},
{"id":4,"first_name":"Julie","last_name":"Fischer","city":"Lasusua","email":"jfischer3@ucoz.com","gender":"Agender"},
{"id":5,"first_name":"Manda","last_name":"Mapis","city":"Sindang","email":"mmapis4@foxnews.com","gender":"Non-binary"},
{"id":6,"first_name":"Noami","last_name":"Rubanenko","city":"Siemianowice Śląskie","email":"nrubanenko5@geocities.com","gender":"Genderfluid"},
{"id":7,"first_name":"Daffi","last_name":"Wherton","city":"Kamirenjaku","email":"dwherton6@privacy.gov.au","gender":"Bigender"},
{"id":8,"first_name":"Tamma","last_name":"Worsham","city":"Batang","email":"tworsham7@globo.com","gender":"Male"},
{"id":9,"first_name":"Gibby","last_name":"Blacktin","city":"Makarov","email":"gblacktin8@mac.com","gender":"Agender"},
{"id":10,"first_name":"Locke","last_name":"Pirdy","city":"Ketanggungan","email":"lpirdy9@wix.com","gender":"Polygender"},
{"id":11,"first_name":"Dorree","last_name":"Claypool","city":"Laborie","email":"dclaypoola@un.org","gender":"Female"},
{"id":12,"first_name":"Jermaine","last_name":"Duplan","city":"Chemin Grenier","email":"jduplanb@skype.com","gender":"Polygender"},
{"id":13,"first_name":"Kliment","last_name":"Divill","city":"Baochang","email":"kdivillc@tamu.edu","gender":"Agender"},
{"id":14,"first_name":"Bernice","last_name":"O'Hartnett","city":"Askainen","email":"bohartnettd@tripod.com","gender":"Genderqueer"},
{"id":15,"first_name":"Teirtza","last_name":"Summerlee","city":"Babakanbungur","email":"tsummerleee@scientificamerican.com","gender":"Agender"}]


#2 Dada la lista de personas, pedir al usuario que ingrese una letra y devolver una lista con los nombres de las personas que su nombre empieza con esa letra. En el caso que no haya ninguno, devolver que no existe ningun nombre con esa letra.

letra=input("Ingrese una letra: ")
nombres=set ()

for i in personas:
 if i["first_name"][0]==letra:
    nombres.add(i["first_name"])

if len(nombres)>0:
  print(nombres)
else:
  print("No existe ningún nombre que empiece con esa letra")





