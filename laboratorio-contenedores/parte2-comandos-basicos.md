<!-- BORRADOR: reescribe las explicaciones y respuestas con tus propias palabras (el enunciado lo exige) y completa los TODO pendientes. Borra este comentario al terminar. -->

# Parte 2: Primer contenedor

## Objetivo

Ejecutar el primer contenedor usando una imagen existente desde Docker Hub.

## Actividades realizadas

### Ejecutar hello-world

```bash
docker run hello-world
```

**Explicación:** Crea y ejecuta un contenedor a partir de la imagen `hello-world`. Como la imagen no estaba en mi máquina, Docker la descargó de Docker Hub (`Unable to find image ... locally` y `Pulling from library/hello-world`), creó el contenedor, este imprimió el mensaje y terminó.

**Resultado obtenido:**

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:5e23090353324d887c48ad5e5c56d294eab81588df9605b07d1afe895f9cc8f8
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### Contenedores en ejecución

```bash
docker ps
```

**Explicación:** Lista los contenedores que están en ejecución. Salió vacío (solo los encabezados) porque `hello-world` ya había terminado.

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Todos los contenedores (incluso detenidos)

```bash
docker ps -a
```

**Explicación:** Lista todos los contenedores, incluso los detenidos. Aparece `epic_shockley` (nombre asignado automáticamente por Docker) con estado `Exited (0)`, que indica que terminó sin errores.

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE         COMMAND    CREATED                  STATUS                              PORTS     NAMES
816d06d4525a   hello-world   "/hello"   Less than a second ago   Exited (0) Less than a second ago             epic_shockley
```

## Documentación requerida

- **Qué hizo el comando `docker run hello-world`**
  Creó un contenedor a partir de la imagen `hello-world`, lo ejecutó, mostró el mensaje de bienvenida (que confirma que la instalación funciona) y el contenedor terminó.
- **Qué ocurrió si la imagen no estaba descargada**
  Docker mostró `Unable to find image 'hello-world:latest' locally`, descargó la imagen de Docker Hub (`Pulling from library/hello-world`, `Status: Downloaded newer image`) y después ejecutó el contenedor.
- **Diferencia entre `docker ps` y `docker ps -a`**
  `docker ps` solo muestra los contenedores en ejecución; `docker ps -a` muestra todos, incluidos los detenidos.
- **Captura o copia del resultado de ambos comandos**
  Las salidas de ambos comandos están copiadas arriba.

## Reflexión personal

Ejecutar la imagen hello-world fue una introducción directa y efectiva al flujo de trabajo de Docker. Me permitió observar cómo el sistema descarga automáticamente una imagen de Docker Hub si no existe localmente, crea el contenedor, ejecuta el proceso y finaliza.

## Preguntas de reflexión

1. **¿Qué es la imagen `hello-world`?**

   Es una imagen mínima oficial de Docker Hub cuyo único programa imprime un mensaje de bienvenida. Sirve para verificar que Docker puede descargar imágenes y crear contenedores.

2. **¿El contenedor quedó ejecutándose después de imprimir el mensaje?**

   No. Se ejecutó, imprimió el mensaje y terminó (`Exited (0)`), porque su proceso principal acabó.

3. **¿Por qué aparece en `docker ps -a` pero no necesariamente en `docker ps`?**

   Porque el contenedor sigue existiendo en estado detenido. `docker ps` solo lista los que están corriendo, mientras que `docker ps -a` incluye también los que ya terminaron.

4. **¿Qué demuestra este primer ejemplo sobre Docker?**

   Que Docker descarga imágenes automáticamente desde un registro si no las tiene, que un contenedor es un proceso aislado que vive mientras dure su comando principal, y que con un solo comando se puede ejecutar software sin instalarlo manualmente.
