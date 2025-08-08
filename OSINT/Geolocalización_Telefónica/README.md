# Geolocalización_Telefónica

Este script permite obtener información básica de un número telefónico, como país, operador y zona horaria, utilizando la librería `phonenumbers`. 
Además, representa la ubicación estimada en un mapa interactivo mediante `folium` y `geopy`.

## Funcionalidad

- Extrae datos de un número telefónico:
  - País o región
  - Operador
  - Zona horaria
- Geolocaliza el país asociado usando `Photon`
- Genera un mapa HTML con la ubicación estimada

## Requisitos

- Python 3.x
- Conexión a internet para la geolocalización
- Dependencias listadas en `requirements.txt`

## Uso

Ejecutar el script desde la terminal:

```
python Geolocalización_Telefónica.py
```

## Ingresar el número telefónico en formato internacional:

> Introduce un número telefónico, por ejemplo "+5491123456789"

## Salida esperada:

```
{
  'Número': '+54 9 11 2345-6789',
  'País': 'Argentina',
  'Operador': 'Movistar',
  'Zona Horaria': ('America/Argentina/Buenos_Aires',)
}
Mapa guardado en mapa_telefonico.html
```

## Nota
La ubicación mostrada en el mapa es aproximada y basada en el país del número. No representa la ubicación exacta del dispositivo.
Este script es parte del portfolio público de herramientas básicas. Las versiones avanzadas y personalizadas son privadas.

## Autor
Creado por Fabián Iván Bertotti Guglielmone
