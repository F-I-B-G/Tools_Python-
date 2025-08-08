import whois

nombre_de_dominio = input('Escribe el nombre de dominio que deseas consultar: ')

# La respuesta se almacenará en la siguiente variable:
respuesta = whois.whois(nombre_de_dominio)

# Se va a consultar a la base de datos whois y la respuesta se sacará por pantalla:
print(respuesta)
