# Cómo ejecutar `scrape.py` para obtener artículos de CoinMarketCap Academy

## Requisitos previos

- Python 3.x instalado en tu sistema.
- Gestor de paquetes `pip` para Python.

## Paso 1: Configuración del entorno virtual (Opcional pero recomendado)

1. **Crea un entorno virtual:**

   Abre una terminal y navega hasta el directorio donde tienes el archivo `scrape.py`.

   Ejecuta el siguiente comando para crear un entorno virtual:

```
python -m venv venv
```


Esto creará un directorio `venv` que contendrá todos los paquetes instalados localmente para este proyecto.

2. **Activa el entorno virtual:**

- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

Al activar el entorno virtual, verás que el prompt de tu terminal cambiará para indicar que estás utilizando el entorno virtual.

## Paso 2: Instalación de dependencias

1. **Instala las dependencias necesarias:**

Asegúrate de que `pip` esté actualizado:

```
pip install --upgrade pip
```

Instala las dependencias del proyecto (BeautifulSoup y Requests):

```
pip install requests beautifulsoup4
```


## Paso 3: Ejecución del script

1. **Ejecuta el script `scrape.py`:**

- Desde la terminal y con el entorno virtual activado, navega hasta el directorio donde se encuentra `scrape.py`.
- Ejecuta el script con Python:

  ```
  python scrape.py
  ```

## Notas adicionales

- El script `scrape.py` está configurado para obtener artículos de CoinMarketCap Academy en español desde la categoría de investigación (`cmc-research`). Puedes ajustar `num_pages` en el script para obtener más páginas si es necesario.
- Asegúrate de que tu entorno virtual esté activo siempre que ejecutes el script para garantizar que las dependencias instaladas se utilicen correctamente y no interfieran con otros proyectos.
