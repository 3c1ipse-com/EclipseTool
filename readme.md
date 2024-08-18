# Eclipse Tool

_Eclipse Tool_ es una herramienta diseñada para automatizar tareas de hacking en Eclipse. Este script facilita la realización de escaneos de red, la extracción de enlaces de sitios web y el análisis de resultados utilizando inteligencia artificial.

## Características

- **Escaneo de red**: Realiza un escaneo de red utilizando `nmap` para obtener información sobre las direcciones IP.
- **Extracción de enlaces**: Recupera todos los enlaces de una URL específica.
- **Análisis con IA**: Utiliza inteligencia artificial para analizar los resultados obtenidos.

## Instalación

Para instalar y configurar _Eclipse Tool_, sigue los siguientes pasos:

1. Clona el repositorio desde GitHub:
    ```bash
    git clone git@github.com:3c1ipse-com/EclipseTool.git
    ```
    
2. Crea un entorno virtual en Python:
    ```bash
    python3 -m venv venv
    ```
    
3. Activa el entorno virtual:
    ```bash
    . .venv/bin/activate
    ```
    
4. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

5. Verifica que la instalación fue exitosa ejecutando el siguiente comando:
    ```bash
    python3 main.py -h
    ```

## Configuración de OpenAI

Para utilizar la funcionalidad de análisis con inteligencia artificial, necesitas configurar la clave API de OpenAI. Establece la variable de entorno `OPENAI_API_KEY` con tu clave API de OpenAI.

En sistemas Unix (Linux, macOS), puedes hacerlo de la siguiente manera:

```bash
export OPENAI_API_KEY="sk-XXXXXXXX"
```

En sistemas Windows, utiliza el siguiente comando en la línea de comandos:

```cmd
set OPENAI_API_KEY="sk-XXXXXXXX"
```

Asegúrate de reemplazar `"sk-XXXXXXXX"` con tu clave API real.

## Uso

_Eclipse Tool_ se puede utilizar desde la línea de comandos con los siguientes parámetros:

```bash
python3 main.py --nmap [dirección_ip] --links [url] [--IA]
```

- `--nmap`: Realiza un escaneo de red en la dirección IP especificada.
- `--links`: Extrae todos los enlaces de la URL proporcionada.
- `--IA`: Activa el modo de análisis con inteligencia artificial para analizar los resultados obtenidos.

### Ejemplos

1. **Escanear una red**:
    ```bash
    python3 main.py --nmap 192.168.1.1
    ```
    
2. **Extraer enlaces de un sitio web**:
    ```bash
    python3 main.py --links https://ejemplo.com
    ```
    
3. **Escanear una red y analizar con IA**:
    ```bash
    python3 main.py --nmap 192.168.1.1 --IA
    ```

## Contribuciones

Si deseas contribuir a _Eclipse Tool_, por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit de los mismos (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía tus cambios a tu repositorio fork (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia

_Eclipse Tool_ se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Este archivo README ofrece una guía rápida y fácil de seguir para la instalación y uso de _Eclipse Tool_. Si tienes alguna pregunta o problema, no dudes en abrir un issue en el repositorio.