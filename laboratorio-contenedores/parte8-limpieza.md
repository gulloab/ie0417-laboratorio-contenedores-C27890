<!-- BORRADOR: reescribe las explicaciones y respuestas con tus propias palabras (el enunciado lo exige) y completa los TODO pendientes. Borra este comentario al terminar. -->

# Parte 8: Limpieza del ambiente

## Objetivo

Aprender a limpiar contenedores, imágenes, volúmenes y redes que ya no se utilizan.

> No ejecutar `docker system prune -a` a menos que se entiendan sus consecuencias.

## Actividades realizadas

### Listar contenedores

```bash
docker ps -a
```

**Explicación:** Lista todos los contenedores. En este momento solo existe `servidor-web` (Nginx), que sigue en ejecución.

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS     NAMES
68deb4c1a6fa   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    servidor-web
```

### Listar imágenes

```bash
docker images
```

**Explicación:** Lista las imágenes locales: hay cinco.

**Resultado obtenido:**

```text
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest      5e2309035332       25.9kB         9.49kB        
laboratorio-flask:1.0   fbdbfcb045df        222MB         54.3MB        
nginx:latest            abe47724e466        242MB         66.3MB    U   
python:3.11-slim        6f31d6e9ba2b        200MB         50.8MB        
ubuntu:latest           f144425ff09b        162MB         45.6MB        
```

### Listar volúmenes

```bash
docker volume ls
```

**Explicación:** Lista los volúmenes: queda `datos-lab`.

**Resultado obtenido:**

```text
DRIVER    VOLUME NAME
local     datos-lab
```

### Listar redes

```bash
docker network ls
```

**Explicación:** Lista las redes: las tres por defecto y `red-lab`.

**Resultado obtenido:**

```text
NETWORK ID     NAME      DRIVER    SCOPE
f075f1682609   bridge    bridge    local
22014559ada9   host      host      local
12da644ac6f6   none      null      local
480ddaddf75c   red-lab   bridge    local
```

### Eliminar contenedores detenidos

```bash
docker container prune
```

**Explicación:** Elimina todos los contenedores detenidos, previa confirmación. No liberó espacio (0B) porque `servidor-web` seguía en ejecución y no había contenedores detenidos.

**Resultado obtenido:**

```text
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
```

### Eliminar imágenes no utilizadas

```bash
docker image prune
```

**Explicación:** Elimina las imágenes colgantes (dangling, sin etiqueta). No liberó espacio porque no había ninguna.

**Resultado obtenido:**

```text
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
```

### Eliminar volúmenes no utilizados

```bash
docker volume prune
```

**Explicación:** Elimina los volúmenes anónimos que ningún contenedor usa. No liberó espacio y `datos-lab` se conservó, porque es un volumen con nombre y la advertencia indica que solo se eliminan los anónimos.

**Resultado obtenido:**

```text
WARNING! This will remove anonymous local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
```

### Revisar el espacio utilizado por Docker

```bash
docker system df
```

**Explicación:** Resume el espacio usado por imágenes, contenedores, volúmenes y caché de build, y cuánto se puede recuperar.

**Resultado obtenido:**

```text
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         1         510.7MB   225.4MB (44%)
Containers      1         1         81.92kB   0B (0%)
Local Volumes   1         0         0B        0B
Build Cache     0         0         0B        0B
```

### (Opcional) Limpieza general

```bash
docker system prune
```

**Explicación:** Limpieza general de recursos sin uso. No se ejecutó porque era opcional (y nunca con `-a` sin entender sus consecuencias).

**Resultado obtenido:**

```text
No ejecutado (opcional).
```

## Documentación requerida

- **Qué recursos quedaron creados**
  Al momento de la limpieza: 1 contenedor en ejecución (`servidor-web`), 5 imágenes (`hello-world`, `laboratorio-flask:1.0`, `nginx`, `python:3.11-slim`, `ubuntu`), 1 volumen (`datos-lab`) y la red `red-lab`, además de las redes por defecto.
- **Qué comandos de limpieza ejecuté**
  `docker container prune`, `docker image prune` y `docker volume prune`, todos confirmados con `y`, y luego `docker system df` para revisar el espacio. No ejecuté `docker system prune`.
- **Qué diferencia hay entre limpiar contenedores, imágenes y volúmenes**
  `container prune` elimina contenedores detenidos; `image prune` elimina imágenes colgantes (sin etiqueta y sin uso); `volume prune` elimina volúmenes anónimos sin uso, y sus datos se pierden. Cada comando libera un tipo distinto de recurso.
- **Resultado de `docker system df`**
  Está copiado arriba: 5 imágenes (510.7MB, 225.4MB recuperables), 1 contenedor activo, 1 volumen local y caché de build vacía.

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Por qué Docker puede consumir mucho espacio en disco?**

   Porque cada imagen descargada o construida ocupa espacio, y los contenedores detenidos, los volúmenes y la caché de build siguen ahí hasta que se eliminan. Las capas de las imágenes también se acumulan.

2. **¿Qué diferencia hay entre eliminar un contenedor y eliminar una imagen?**

   Eliminar un contenedor borra esa instancia y los datos de su capa de escritura; eliminar una imagen borra la plantilla, y habría que descargarla o construirla de nuevo para crear contenedores.

3. **¿Por qué se debe tener cuidado al eliminar volúmenes?**

   Porque guardan datos persistentes que sobreviven a los contenedores; si se elimina un volumen, esos datos se pierden definitivamente.

4. **¿Qué buenas prácticas aplicaría para mantener limpio su ambiente local?**

   Detener y eliminar los contenedores cuando termino de usarlos (`docker rm` o la opción `--rm`), revisar `docker system df` de vez en cuando, usar los comandos `prune` leyendo antes la advertencia, y no usar `docker system prune -a` sin entender sus consecuencias.
