<!-- BORRADOR: reescribe las explicaciones con tus propias palabras (el enunciado lo exige) y completa el TODO de la reflexión personal. Verifica que existan img/parte4-app-local.png e img/parte4-app-info.png. Borra este comentario al terminar. -->

# Parte 4: Aplicación sencilla y Dockerfile

El código está en la carpeta [`app/`](app/): `app.py`, `requirements.txt`, `Dockerfile` y `.dockerignore`.

---

## A. Aplicación sencilla (Parte 5 del laboratorio)

### Qué hace la aplicación

Es un servidor web mínimo hecho con Flask. Cuando se le hace una petición HTTP responde con contenido según la ruta. La página principal muestra un mensaje en HTML; el mensaje se toma de la variable de entorno `MENSAJE` y, si no existe, usa "Hola desde Flask en Docker".

### Rutas

| Ruta | Qué devuelve |
|---|---|
| `/` | Página HTML con el mensaje y un texto que indica que corre dentro de un contenedor |
| `/info` | JSON con `app`, `curso` y `tema` |

### Dependencia

Solo `flask`, declarada en `requirements.txt`. Flask trae a su vez otras librerías (Werkzeug, Jinja2, Click, etc.).

### Por qué se usa `host="0.0.0.0"` en lugar de `localhost`

Con `localhost` (127.0.0.1) la aplicación solo acepta conexiones que se originan dentro de la misma máquina. Dentro de un contenedor, eso significa solo desde el propio contenedor. El tráfico que viene del host llega por la interfaz de red virtual del contenedor, así que la app tiene que escuchar en todas las interfaces (`0.0.0.0`) para poder alcanzarla cuando se publique el puerto.

### Prueba local

Comandos (desde `app/`, con el entorno virtual activo):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Para qué sirven: se crea un entorno virtual aislado, se instalan las dependencias de `requirements.txt` y se ejecuta la aplicación con el Python local.

Salida obtenida:

```text
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.51:5000
Press CTRL+C to quit
```

Capturas del navegador (con la barra de direcciones visible). Esta prueba fue local, no dentro de Docker:

![Aplicación en localhost:5000](img/parte4-app-local.png)

![Ruta /info](img/parte4-app-info.png)

### Preguntas de reflexión (Parte 5)

1. **¿Qué hace Flask en esta aplicación?**
   Es el framework web. Recibe las peticiones HTTP, decide qué función ejecutar según la ruta (`@app.route`), devuelve la respuesta (HTML o JSON) y levanta el servidor con `app.run`.

2. **¿Para qué sirve el archivo `requirements.txt`?**
   Lista las dependencias del proyecto para instalarlas con `pip install -r requirements.txt`. Así cualquiera, o el `Dockerfile`, puede reproducir el mismo entorno.

3. **¿Por qué una aplicación dentro de un contenedor debe escuchar en `0.0.0.0`?**
   Porque `127.0.0.1` dentro del contenedor es su propio loopback. Si la app solo escucha ahí, el host no puede conectarse aunque se publique el puerto. Con `0.0.0.0` acepta conexiones por todas sus interfaces.

4. **¿Qué diferencia hay entre ejecutar la aplicación localmente y ejecutarla dentro de Docker?**
   Localmente depende del Python y los paquetes de mi máquina. En Docker, la app va empaquetada con su Python y sus dependencias en una imagen aislada y reproducible, pero para acceder a ella hay que publicar los puertos.

---

## B. Construir una imagen con Dockerfile (Parte 6 del laboratorio)

### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Qué hace cada instrucción

| Instrucción | Qué hace |
|---|---|
| `FROM python:3.11-slim` | Define la imagen base sobre la que se construye: una imagen con Python 3.11 en versión reducida |
| `WORKDIR /app` | Fija `/app` como directorio de trabajo dentro de la imagen; los comandos siguientes se ejecutan ahí |
| `COPY requirements.txt .` | Copia solo el archivo de dependencias del proyecto a la imagen |
| `RUN pip install --no-cache-dir -r requirements.txt` | Ejecuta durante la construcción la instalación de las dependencias; el resultado queda guardado en la imagen |
| `COPY . .` | Copia el resto del código al directorio de trabajo de la imagen |
| `EXPOSE 5000` | Documenta que la aplicación usa el puerto 5000; no lo publica hacia el host |
| `CMD ["python", "app.py"]` | Define el comando por defecto que se ejecuta cuando se inicia un contenedor |

### Qué significa construir una imagen

Es ejecutar las instrucciones del `Dockerfile` con `docker build` para generar una plantilla inmutable, formada por capas, que contiene todo lo necesario para correr la aplicación. A partir de esa imagen se crean contenedores.

### Qué significa el nombre `laboratorio-flask:1.0`

`laboratorio-flask` es el nombre de la imagen y `1.0` es la etiqueta (tag), que se usa como versión. Se asigna con la opción `-t` de `docker build`.

### Diferencia entre el nombre de la imagen y el nombre del contenedor

`laboratorio-flask:1.0` es la imagen, la plantilla. `app-lab` es el nombre de un contenedor concreto, una instancia creada a partir de esa imagen con `--name`. De una misma imagen se pueden crear muchos contenedores con nombres distintos.

### Construcción de la imagen

```bash
cd app
docker build -t laboratorio-flask:1.0 .
```

Para qué sirve: construye la imagen leyendo el `Dockerfile` de la carpeta actual (el `.` final) y la etiqueta como `laboratorio-flask:1.0`.

Salida obtenida:

```text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  6.144kB
Step 1/7 : FROM python:3.11-slim
 ---> 6f31d6e9ba2b
Step 2/7 : WORKDIR /app
 ---> e04878d34d54
Step 3/7 : COPY requirements.txt .
 ---> f35e6301ab5d
Step 4/7 : RUN pip install --no-cache-dir -r requirements.txt
Successfully installed blinker-1.9.0 click-8.5.0 flask-3.1.3 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.4 werkzeug-3.1.9
 ---> 1ad14bae65e2
Step 5/7 : COPY . .
 ---> 06519ab75fe7
Step 6/7 : EXPOSE 5000
 ---> 4e9c9ca70642
Step 7/7 : CMD ["python", "app.py"]
 ---> bd63b7942aaf
Successfully built bd63b7942aaf
Successfully tagged laboratorio-flask:1.0
```

(Salida resumida: se omiten las líneas de descarga de pip.) Esta vez la imagen base `python:3.11-slim` ya estaba en mi máquina, por eso no hubo descarga en el Step 1. El contexto de build fue de solo 6.144kB gracias al archivo `.dockerignore`, que excluye la carpeta `.venv`; en la primera construcción, sin ese archivo, el contexto era de 17.37MB.

### Resultado de `docker images`

```bash
docker images
```

```text
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest      5e2309035332       25.9kB         9.49kB        
laboratorio-flask:1.0   bd63b7942aaf        222MB         54.3MB        
nginx:latest            abe47724e466        242MB         66.3MB        
python:3.11-slim        6f31d6e9ba2b        200MB         50.8MB        
ubuntu:latest           f144425ff09b        162MB         45.6MB    U   
```

La imagen `laboratorio-flask:1.0` ocupa 222MB en disco (54.3MB de contenido), construida sobre la base `python:3.11-slim` (200MB). Las otras imágenes (`hello-world`, `nginx`, `ubuntu`) vienen de otras partes del laboratorio.

### Ejecución del contenedor

```bash
docker run --name app-lab laboratorio-flask:1.0
```

Para qué sirve: crea y ejecuta un contenedor llamado `app-lab` a partir de la imagen. Se queda en primer plano mostrando los logs de Flask. No se publicó ningún puerto, por eso la página no es accesible desde el navegador del host.

```text
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

Flask se inició dentro del contenedor y escucha en todas las interfaces (`0.0.0.0`). La IP `172.17.0.2` es la dirección interna del contenedor en la red `bridge` de Docker; es distinta a la de mi máquina (`192.168.0.51`), que aparecía en la prueba local.

En otra terminal:

```bash
docker ps
```

Para qué sirve: lista los contenedores en ejecución; debe aparecer `app-lab`.

```text
CONTAINER ID   IMAGE                   COMMAND           CREATED          STATUS          PORTS      NAMES
65aad3e924f8   laboratorio-flask:1.0   "python app.py"   45 seconds ago   Up 45 seconds   5000/tcp   app-lab
```

Se ve que el contenedor `app-lab` está en ejecución a partir de la imagen `laboratorio-flask:1.0`. En `PORTS` aparece solo `5000/tcp`: el contenedor usa ese puerto, pero no está publicado hacia el host, por eso no se puede abrir desde el navegador todavía.

```bash
docker stop app-lab
docker rm app-lab
```

Para qué sirven: `stop` detiene el contenedor y `rm` lo elimina.

```text
app-lab
app-lab
```

Cada comando imprime el nombre del contenedor sobre el que actuó: el primero lo detuvo y el segundo lo eliminó.

### Reflexión personal

Crear, nombrar e interactuar con mi-ubuntu fue clave para asimilar el ciclo de vida de un contenedor. Modificar un archivo y comprobar que persiste al detener y reiniciar el contenedor me ayudó a entender que la volatilidad ocurre solo al momento de usar el comando de eliminación (rm).

### Preguntas de reflexión (Parte 6)

1. **¿Qué es una imagen base?**
   Es la imagen desde la que parte la construcción, indicada con `FROM`. Aquí es `python:3.11-slim`, que ya trae Python instalado, y sobre ella se agregan las capas propias.

2. **¿Por qué se usa una imagen `slim`?**
   Porque es una versión reducida, sin herramientas que la app no necesita. Pesa menos, se descarga más rápido y tiene menos superficie de ataque.

3. **¿Por qué se copian primero las dependencias y luego el resto del código?**
   Por el caché de capas. `requirements.txt` cambia poco y `app.py` cambia seguido. Si solo cambia el código, Docker reutiliza la capa donde ya se instaló Flask y no repite el `pip install`, así que el build es más rápido.

4. **¿Qué diferencia hay entre `RUN` y `CMD`?**
   `RUN` se ejecuta al construir la imagen y su resultado queda guardado en ella (instalar Flask). `CMD` no se ejecuta en el build; define qué comando corre cuando se inicia un contenedor (`python app.py`).

5. **¿Qué pasaría si se elimina la imagen pero no el Dockerfile?**
   No se pierde la aplicación: el `Dockerfile` es la receta y con `docker build` se vuelve a construir la imagen. Lo que se pierde es la imagen ya construida (y habría que descargar de nuevo la base si tampoco está). Además, Docker no deja borrar una imagen mientras exista un contenedor creado a partir de ella, salvo que se fuerce.
