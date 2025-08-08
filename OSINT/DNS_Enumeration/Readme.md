# DNS_Enumeration

Este script realiza una enumeración de registros DNS para un dominio objetivo utilizando la librería `dnspython`. 
Permite obtener información valiosa como registros A, MX, NS, TXT, entre otros, útil en fases de reconocimiento dentro de un análisis OSINT.

## Funcionalidad

- Consulta registros DNS: `A`, `AAAA`, `CNAME`, `MX`, `NS`, `SOA`, `TXT`
- Muestra resultados por tipo de registro
- Maneja errores cuando no hay respuesta del servidor

## Requisitos

- Python 3.x
- Librería `dnspython`

Instalación de dependencias:
```
pip install -r requirements.txt
```

## Uso:

1 - Ejecutar el script desde la terminal:

```
python DNS_Enumeration.py
```

2 - Ingresar el dominio cuando se solicite:

> Introduce el dominio objetivo: `ejemplo.com`

3 - Salida esperada:

```
----- MX registros para ejemplo.com -----
<respuesta del servidor>
...
```

## Nota
Este script es parte del portfolio público de herramientas básicas. Las versiones avanzadas y personalizadas son privadas.

## Autor
Creado por Fabián Iván Bertotti Guglielmone

