# Whois Enumeration

Este script realiza una consulta WHOIS sobre un dominio específico, extrayendo información registral como fechas de creación, expiración, servidores DNS, y datos del registrante (si están disponibles).

## Funcionalidad

- Consulta la base de datos WHOIS para un dominio dado
- Extrae información como:
  - Fechas de creación y expiración
  - Servidores DNS
  - Registrador
  - Estado del dominio
  - Información del propietario (si no está oculta)

## Requisitos

- Python 3.x
- Conexión a internet
- Dependencias listadas en `requirements.txt`

## Uso

Ejecutar el script desde la terminal:

```
python whois_enumeration.py
```

## Ingresar el dominio:

> Escribe el nombre de dominio que deseas consultar: microsoft.com

## Salida esperada:

```
{
  'domain_name': 'MICROSOFT.COM',
  'registrar': 'MarkMonitor Inc.',
  'creation_date': datetime.datetime(1991, 5, 2, 0, 0),
  'expiration_date': datetime.datetime(2025, 5, 3, 0, 0),
  'name_servers': ['NS1.MSFT.NET', 'NS2.MSFT.NET', ...],
  ...
}
```

## Notas
• Algunos dominios tienen protección de privacidad, por lo que ciertos campos pueden estar ocultos.
• La disponibilidad de datos depende del registrador y del tipo de dominio (.com, .org, .gov, etc.).
• Este script forma parte del portfolio público de herramientas OSINT. Las versiones avanzadas y personalizadas son privadas.

## Autor
Creado por Fabián Iván Bertotti Guglielmone
