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

**Explicación:** Lista todos los contenedores, incluso los detenidos. Quedaban 4: tres de la app (`app-env-2`, `app-env`, `app-puertos-2`) y el de Ubuntu con nombre aleatorio. En `IMAGE` aparece el ID `fbdbfcb045df` en vez del nombre porque reconstruí la imagen y la etiqueta `laboratorio-flask:1.0` pasó a una imagen nueva; estos contenedores siguen apuntando a la anterior.

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE          COMMAND           CREATED       STATUS                   PORTS     NAMES
9e3606edad22   fbdbfcb045df   "python app.py"   5 hours ago   Exited (0) 5 hours ago             app-env-2
eed99b010399   fbdbfcb045df   "python app.py"   5 hours ago   Exited (0) 5 hours ago             app-env
5f3007a2b853   fbdbfcb045df   "python app.py"   5 hours ago   Exited (0) 5 hours ago             app-puertos-2
b54082ea3156   ubuntu         "bash"            5 hours ago   Exited (0) 5 hours ago             competent_mirzakhani
```

### Listar imágenes

```bash
docker images
```

**Explicación:** Lista las imágenes locales: cinco, entre ellas la nueva `laboratorio-flask:1.0` (ID `bd63b7942aaf`).

**Resultado obtenido:**

```text
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest      5e2309035332       25.9kB         9.49kB        
laboratorio-flask:1.0   bd63b7942aaf        222MB         54.3MB        
nginx:latest            abe47724e466        242MB         66.3MB        
python:3.11-slim        6f31d6e9ba2b        200MB         50.8MB        
ubuntu:latest           f144425ff09b        162MB         45.6MB    U   
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

**Explicación:** Lista las redes: solo las tres que Docker crea por defecto.

**Resultado obtenido:**

```text
NETWORK ID     NAME      DRIVER    SCOPE
f075f1682609   bridge    bridge    local
22014559ada9   host      host      local
12da644ac6f6   none      null      local
```

### Eliminar contenedores detenidos

```bash
docker container prune
```

**Explicación:** Elimina todos los contenedores detenidos, previa confirmación. Borró los 4 que estaban en `Exited` y liberó 614.4kB.

**Resultado obtenido:**

```text
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
9e3606edad2221a0e2a03b890db72f9daf7c84aef898c6ce061c5aaf48f6abb5
eed99b01039929c22cbe4319b0c4044d8c0f3aaf7fb2968a998697cd74daee81
5f3007a2b853455ae27109d3a5752ee7eff749325a8c7dc4c2b3ab4efa97cff2
b54082ea31563d8d2306a34ffc6dcf11aee22bfaac3e72f2ab04ca261ca8b8a5

Total reclaimed space: 614.4kB
```

### Eliminar imágenes no utilizadas

```bash
docker image prune
```

**Explicación:** Elimina las imágenes colgantes (dangling, sin etiqueta): la versión anterior de `laboratorio-flask` y capas intermedias de construcciones anteriores, que habían quedado sin nombre al reconstruir. Liberó 5.79MB. Las imágenes etiquetadas no se tocaron.

**Resultado obtenido:**

```text
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
untagged: sha256:4e9c9ca7064228e8ef833e5bcbe5bc6aa0968bcbe57a4f147c97147bcc3a944a
deleted: sha256:4e9c9ca7064228e8ef833e5bcbe5bc6aa0968bcbe57a4f147c97147bcc3a944a
untagged: sha256:e04878d34d54c4faff0b5d72431198edf0e5a452ac9c09204e978d039f8c043c
deleted: sha256:e04878d34d54c4faff0b5d72431198edf0e5a452ac9c09204e978d039f8c043c
untagged: sha256:f35e6301ab5d124241186e8399edf5afd31c5a7bbc30c46adcb6f7e1ba423467
deleted: sha256:f35e6301ab5d124241186e8399edf5afd31c5a7bbc30c46adcb6f7e1ba423467
untagged: sha256:fbdbfcb045df5335511f33c16cbe1465fe3b8bb47758d6200fdb9857fceb1725
deleted: sha256:fbdbfcb045df5335511f33c16cbe1465fe3b8bb47758d6200fdb9857fceb1725
untagged: sha256:06519ab75fe790f23112a4a032684038d4447b85f982fc123b93677a5554f9f1
deleted: sha256:06519ab75fe790f23112a4a032684038d4447b85f982fc123b93677a5554f9f1
untagged: sha256:1ad14bae65e27c70c2b4f840970046ac54d20b57c0daabeae825e189632e8737
deleted: sha256:1ad14bae65e27c70c2b4f840970046ac54d20b57c0daabeae825e189632e8737

Total reclaimed space: 5.79MB
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

**Explicación:** Resume el espacio usado por imágenes, contenedores, volúmenes y caché de build, y cuánto se puede recuperar. Ya no hay contenedores; el volumen `datos-lab` ocupa 33B (el archivo de prueba).

**Resultado obtenido:**

```text
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         0         510.6MB   71.33MB (13%)
Containers      0         0         0B        0B
Local Volumes   1         0         33B       33B (100%)
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
  Antes de limpiar: 4 contenedores detenidos (3 de la app `laboratorio-flask` y 1 de Ubuntu), 5 imágenes etiquetadas (`hello-world`, `laboratorio-flask:1.0`, `nginx`, `python:3.11-slim`, `ubuntu`) más imágenes sin etiqueta de construcciones anteriores, 1 volumen (`datos-lab`) y solo las redes por defecto.
- **Qué comandos de limpieza ejecuté**
  `docker container prune`, `docker image prune` y `docker volume prune`, todos confirmados con `y`, y luego `docker system df` para revisar el espacio. No ejecuté `docker system prune`.
- **Qué diferencia hay entre limpiar contenedores, imágenes y volúmenes**
  `container prune` eliminó los 4 contenedores detenidos (614.4kB); `image prune` eliminó imágenes colgantes, es decir sin etiqueta y sin uso (5.79MB); `volume prune` eliminó 0B porque solo borra volúmenes anónimos sin uso y `datos-lab` tiene nombre, así que sus datos se conservaron. Cada comando libera un tipo distinto de recurso.
- **Resultado de `docker system df`**
  Está copiado arriba: 5 imágenes (510.6MB, 71.33MB recuperables), 0 contenedores, 1 volumen local (33B) y caché de build vacía.

## Reflexión personal

Utilizar los comandos prune para eliminar recursos inactivos fue el cierre necesario para mantener la higiene del entorno de trabajo. Demuestra lo rápido que el almacenamiento puede llenarse con imágenes y contenedores residuales, y la importancia de gestionar los recursos locales.

## Preguntas de reflexión

1. **¿Por qué Docker puede consumir mucho espacio en disco?**

   Porque cada imagen descargada o construida ocupa espacio, y los contenedores detenidos, los volúmenes, las imágenes sin etiqueta y la caché de build siguen ahí hasta que se eliminan. Cada reconstrucción de una imagen también deja capas viejas.

2. **¿Qué diferencia hay entre eliminar un contenedor y eliminar una imagen?**

   Eliminar un contenedor borra esa instancia y los datos de su capa de escritura; eliminar una imagen borra la plantilla, y habría que descargarla o construirla de nuevo para crear contenedores.

3. **¿Por qué se debe tener cuidado al eliminar volúmenes?**

   Porque guardan datos persistentes que sobreviven a los contenedores; si se elimina un volumen, esos datos se pierden definitivamente.

4. **¿Qué buenas prácticas aplicaría para mantener limpio su ambiente local?**

   Eliminar los contenedores cuando termino de usarlos (`docker rm` o la opción `--rm`), revisar `docker system df` de vez en cuando, usar los `prune` leyendo antes la advertencia, y no usar `docker system prune -a` sin entender sus consecuencias.
