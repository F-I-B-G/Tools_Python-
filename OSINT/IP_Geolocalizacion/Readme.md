# IP_Geolocalizacion

Este script permite obtener información geográfica asociada a una dirección IP utilizando la API de [ipinfo.io](https://ipinfo.io). 
Los datos obtenidos se representan en un mapa interactivo generado con `folium`.

## Funcionalidad

- Consulta de IP mediante `ipinfo`
- Extracción de datos como ciudad, región, país, latitud y longitud
- Visualización de la ubicación en un mapa HTML
- Uso de variables de entorno para proteger el token de acceso

## Requisitos

- Python 3.x
- Archivo `.env` con la variable `ACCESS_TOKEN`
- Dependencias listadas en `requirements.txt`

### Ejemplo de `.env`

```
ACCESS_TOKEN=tu_token_de_ipinfo
```


## Uso

1. Crear el archivo `.env` en el mismo directorio que el script.
2. Ejecutar el script:

```
python IP_Geolocalizacion.py
```
3. Ingresar la IP cuando se solicite:

```
Introduce la IP que deseas localizar: 8.8.8.8
```
4. Se mostrará la información en consola y se generará un archivo mapa.html con la ubicación.

## Salida esperada:

```
city: Mountain View
region: California
country: US
latitude: 37.386
longitude: -122.0838
Mapa guardado en /ruta/completa/mapa.html
```

## Nota
Este script es parte del portfolio público de herramientas básicas. Las versiones avanzadas y personalizadas son privadas.

## Autor
Creado por Fabián Iván Bertotti Guglielmone
