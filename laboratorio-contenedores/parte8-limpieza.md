# Parte 8: Limpieza del ambiente

## Objetivo

Aprender a limpiar contenedores, imágenes, volúmenes y redes que ya no se utilizan.

> No ejecutar `docker system prune -a` a menos que se entiendan sus consecuencias.

## Actividades realizadas

### Listar contenedores

```bash
docker ps -a
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar imágenes

```bash
docker images
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar volúmenes

```bash
docker volume ls
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar redes

```bash
docker network ls
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Eliminar contenedores detenidos

```bash
docker container prune
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Eliminar imágenes no utilizadas

```bash
docker image prune
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Eliminar volúmenes no utilizados

```bash
docker volume prune
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Revisar el espacio utilizado por Docker

```bash
docker system df
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### (Opcional) Limpieza general

```bash
docker system prune
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

## Documentación requerida

- **Qué recursos quedaron creados**
  TODO
- **Qué comandos de limpieza ejecuté**
  TODO
- **Qué diferencia hay entre limpiar contenedores, imágenes y volúmenes**
  TODO
- **Resultado de `docker system df`**
  TODO

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Por qué Docker puede consumir mucho espacio en disco?**

   TODO

2. **¿Qué diferencia hay entre eliminar un contenedor y eliminar una imagen?**

   TODO

3. **¿Por qué se debe tener cuidado al eliminar volúmenes?**

   TODO

4. **¿Qué buenas prácticas aplicaría para mantener limpio su ambiente local?**

   TODO
