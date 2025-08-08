# Metadatos_Python

Este script permite extraer metadatos de archivos comunes en investigaciones OSINT: imágenes, documentos PDF y archivos DOCX. 
Utiliza una arquitectura basada en clases abstractas para facilitar la extensión a nuevos formatos.

## Funcionalidad

- Extrae metadatos de:
  - Imágenes (`.jpg`, `.jpeg`, `.png`)
  - Documentos PDF (`.pdf`)
  - Documentos Word (`.docx`)
- Detecta automáticamente el tipo de archivo
- Extrae correos electrónicos embebidos en PDFs mediante expresiones regulares

## Requisitos

- Python 3.x
- Dependencias listadas en `requirements.txt`

## Uso

### Ejecución directa

```
python Metadatos_Python.py
```

## Se solicitará la ruta del archivo:

> Ingresa la ruta del archivo: /ruta/al/archivo.pdf

## Y se imprimirá la metadata extraída:

```
Author: Fabián
Created: 2025-08-01T12:34:56
Emails: ['contacto@ejemplo.com', 'soporte@dominio.org']
```

## Uso como módulo

```
from Metadatos_Python import extract_metadata

metadata = extract_metadata('ruta/al/archivo.docx')
print(metadata)
```

## Salida esperada

```
{
  'Author': 'Fabián',
  'Created': '2025-08-01T12:34:56',
  'Emails': ['contacto@ejemplo.com', 'soporte@dominio.org']
}
```

## Arquitectura

`MetadataExtractor`: clase abstracta base
`ImageMetadataExtractor`: extrae metadatos EXIF
`pdfMetadataExtractor`: extrae metadatos y correos electrónicos
`DocxMetadataExtract`: extrae propiedades del documento Word
`MetadataExtractorFactory`: selecciona el extractor adecuado según el tipo MIME

## Notas

• Los metadatos pueden variar según el origen del archivo.
• Las imágenes PNG no siempre contienen metadatos EXIF.
• Los correos electrónicos se extraen solo de PDFs con texto accesible.
• Este script forma parte del portfolio público de herramientas OSINT. Las versiones avanzadas y personalizadas son privadas.

## Autor
Creado por Fabián Iván Bertotti Guglielmone
