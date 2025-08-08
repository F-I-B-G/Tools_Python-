import dns.resolver

# Se definen los nombres de dominios.
dominio_objetivo = input('Introduce el dominio objetivo: ')

# Se va a indicar lo que se quiera obtener del servidor.
tipos_de_registro = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SOA', 'TXT']

# Se va a definir un cliente DNS para realizar las peticiones (DNS Resolver).
resolver = dns.resolver.Resolver()

# Recorremos cada tipo de registro y hacemos la petición al servidor de nombres.
for tipo_de_registro in tipos_de_registro:
    try:
        respuesta = resolver.resolve(dominio_objetivo, tipo_de_registro)
    except dns.resolver.NoAnswer:
        print(f'----- No se pudo obtener respuesta de {tipo_de_registro} -----')
        continue

# Mostramos la información en pantalla.
print(f'----- {tipo_de_registro} registros para {dominio_objetivo}-----')

for data in respuesta:
    print(f'{data}')
