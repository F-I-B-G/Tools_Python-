import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import folium
from geopy.geocoders import Photon

def obtener_informacion_telefonica(numero_telefonico):
    """
    Obtener información de geolocalización de un número de teléfono.
    """

    # Se define un "cliente" 
    numero = phonenumbers.parse(numero_telefonico)

    # Obtener zona horaria:
    zona_horaria = timezone.time_zones_for_number(numero)

    # Obtener el país / región:
    pais = geocoder.description_for_number(numero, 'es') # 'es' es el idioma del pais del número.

    # Obtener operador asociado con el número:
    operador = carrier.name_for_number(numero, 'es')

    # Diccionario con toda la información:
    informacion = {
        'Número': phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        'País': pais,
        'Operador': operador,
        'Zona Horaria': zona_horaria
    }
    return informacion

def mostrar_mapa(localizacion, filename='mapa_telefonico.html'):
    """
    Dibuja el mapa con la ubicación del número telefónico.
    """
    geolocalizador = Photon(user_agent='VSC') # En user_agent puede ir cualquier cosa.
    localización = geolocalizador.geocode(localizacion)
    
    if localizacion is None:
        print(f"No se pudo geolocalizar: {localizacion}")
        return
    
    mapa = folium.Map(location=[localización.latitude, localización.longitude], zoom_start=10)
    folium.Marker([localización.latitude, localización.longitude], popup=localizacion).add_to(mapa)

    # Se guarda el mapa en formato HTML.
    mapa.save(filename)
    print(f'Mapa guardado en {filename}') # Agregar ruta absoluta

# Ejemplo de uso:
if __name__ == '__main__':
    numero = input('Introduce un número telefónico, por ejemplo "+549....": ')
    informacion = obtener_informacion_telefonica(numero)
    print(informacion)
    mostrar_mapa(informacion['País'])
