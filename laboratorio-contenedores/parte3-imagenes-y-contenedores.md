# Parte 3: Imágenes y contenedores

## Objetivo

Comprender la diferencia entre una imagen y un contenedor.

## Actividades realizadas

### Descargar una imagen de Ubuntu

```bash
docker pull ubuntu
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar las imágenes disponibles

```bash
docker images
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Ejecutar un contenedor interactivo

```bash
docker run -it ubuntu bash
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Explorar el contenedor (dentro del contenedor)

```bash
ls
pwd
cat /etc/os-release
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Salir del contenedor (dentro del contenedor)

```bash
exit
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar los contenedores

```bash
docker ps -a
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

## Documentación requerida

- **Qué hace `docker pull`**
  TODO
- **Qué muestra `docker images`**
  TODO
- **Qué significa ejecutar un contenedor en modo interactivo**
  TODO
- **Qué observé dentro del contenedor Ubuntu**
  TODO
- **Qué ocurrió al salir del contenedor**
  TODO

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿La imagen Ubuntu es lo mismo que una máquina virtual Ubuntu?**

   TODO

2. **¿Por qué el contenedor puede parecer un sistema Linux si no es una máquina virtual completa?**

   TODO

3. **¿Qué significa que el contenedor comparta el kernel con el host?**

   TODO

4. **¿Qué diferencia hay entre una imagen descargada y un contenedor creado?**

   TODO


---

## Administración de contenedores

### Objetivo

Aprender a crear, nombrar, detener, iniciar y eliminar contenedores.

### Actividades realizadas

#### Ejecutar un contenedor con nombre

```bash
docker run -it --name mi-ubuntu ubuntu bash
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Crear un archivo (dentro del contenedor)

```bash
echo "Hola desde el contenedor" > mensaje.txt
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Verificar que el archivo existe (dentro del contenedor)

```bash
cat mensaje.txt
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Salir (dentro del contenedor)

```bash
exit
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Verificar el contenedor

```bash
docker ps -a
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Iniciar nuevamente el contenedor

```bash
docker start mi-ubuntu
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Entrar al contenedor

```bash
docker exec -it mi-ubuntu bash
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Verificar si el archivo sigue existiendo (dentro del contenedor)

```bash
cat mensaje.txt
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Salir nuevamente (dentro del contenedor)

```bash
exit
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Detener el contenedor

```bash
docker stop mi-ubuntu
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Eliminar el contenedor

```bash
docker rm mi-ubuntu
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Verificar

```bash
docker ps -a
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Uso de `--name`**
  TODO
- **Diferencia entre `docker start` y `docker run`**
  TODO
- **Uso de `docker exec`**
  TODO
- **Diferencia entre detener y eliminar un contenedor**
  TODO
- **Qué pasó con el archivo creado dentro del contenedor**
  TODO

### Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

### Preguntas de reflexión

1. **¿Qué ventaja tiene asignar nombres a los contenedores?**

   TODO

2. **¿Qué diferencia hay entre crear un contenedor nuevo y reiniciar uno existente?**

   TODO

3. **¿Qué sucede con los datos creados dentro de un contenedor si este se elimina?**

   TODO

4. **¿Por qué se dice que los contenedores son desechables?**

   TODO
