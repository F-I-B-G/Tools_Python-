import ipinfo
from dotenv import load_dotenv
import os
import sys
import folium

# Parámetros de configuración:
load_dotenv()

# Definimos el Token y una dirección IP:
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
IP = input('Introduce la IP que deseas localizar: ')

# Localización en mapa:
def localizacion_en_mapa(latitud, longitud, localizacion, nombre_fichero='mapa.html'):
    """
    Dibuja un mapa según la información obtenida de una IP.
    """
    mapa = folium.Map(localizacion=[latitud, longitud], zoom_start=9)
    # Para que se marque en el mapa:
    folium.Marker([latitud, longitud], popup=localizacion).add_to(mapa)
    mapa.save(nombre_fichero)
    return os.path.abspath(nombre_fichero)


# Definimos la función que hará la consulta:
def get_ip_details(direccion_ip, token):
    """
    Obtiene información de una IP relacioanda a su geolocalización mediante ipinfo.
    """
    try:
        cliente = ipinfo.getHandler(token)
        detalles_de_IP = cliente.getDetails(direccion_ip)
        return detalles_de_IP.all
    except Exception as e:
        print(f'Se ha producido el siguiente error: {e}')
        sys.exit(1) # Para que corte todo.

if __name__ == '__main__':
    detalles = get_ip_details(IP, ACCESS_TOKEN)
    for clave, valor in detalles.items():
        print(f'{clave}: {valor}')
    
    # Ahora se me va a representar en pantalla según la latitud, longitud y localización:
    latitud = detalles.get('latitude')
    longitud = detalles.get('longitude')
    
    # Usamos las claves 'city', 'region', y 'country' para armar una descripción de la ubicación.
    # Si alguna no existe, usamos una cadena vacía para que no rompa.
    ciudad = detalles.get('city', '')
    region = detalles.get('region', '')
    pais = detalles.get('country', '')
    
    # Construimos una cadena de texto para la localización que aparecerá en el mapa.
    # Si hay latitud y longitud, formamos un mensaje más completo.
    if latitud and longitud:
        localizacion = f"{ciudad}, {region}, {pais}" if ciudad or region or pais else f"Lat: {latitud}, Lon: {longitud}"
    else:
        localizacion = "Ubicación desconocida"

    # Se dibuja:
    if latitud and longitud: # Nos aseguramos de tener la info para dibujar
        ruta_del_mapa = localizacion_en_mapa(float(latitud), float(longitud), localizacion)
        print(f'Mapa guardado en {ruta_del_mapa}')
    else:
        print("No se pudo obtener la latitud y longitud para dibujar el mapa.")
