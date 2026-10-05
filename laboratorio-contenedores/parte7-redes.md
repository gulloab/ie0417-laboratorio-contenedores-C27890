# Parte 7: Redes de Docker

## Objetivo

Crear una red personalizada y comunicar contenedores entre sí usando nombres.

## Actividades realizadas

### Crear una red

```bash
docker network create red-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar las redes

```bash
docker network ls
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Ejecutar un contenedor con Nginx

```bash
docker run -d --name servidor-web --network red-lab nginx
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Ejecutar un contenedor Ubuntu en la misma red

```bash
docker run -it --name cliente --network red-lab ubuntu bash
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Instalar curl (dentro del contenedor)

```bash
apt update
apt install -y curl
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Probar la conexión hacia el servidor (dentro del contenedor)

```bash
curl http://servidor-web
exit
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Detener y eliminar contenedores

```bash
docker stop servidor-web
docker rm servidor-web
docker rm cliente
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Eliminar la red

```bash
docker network rm red-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

## Documentación requerida

- **Qué es una red en Docker**
  TODO
- **Qué hace `docker network create`**
  TODO
- **Qué significa conectar contenedores a la misma red**
  TODO
- **Qué ocurrió al ejecutar `curl http://servidor-web`**
  TODO
- **Por qué se pudo usar el nombre `servidor-web`**
  TODO

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Por qué los contenedores necesitan redes?**

   TODO

2. **¿Qué ventaja tiene usar nombres de contenedor en lugar de direcciones IP?**

   TODO

3. **¿Qué diferencia hay entre publicar un puerto hacia el host y comunicarse dentro de una red Docker?**

   TODO

4. **¿Qué ejemplos reales podrían usar una red Docker?**

   TODO


---

## Comunicación entre servicios

### Objetivo

Comprender cómo una aplicación podría comunicarse con otro servicio dentro de una red Docker, sin usar todavía Docker Compose.

### Actividades realizadas

#### Crear una red

```bash
docker network create red-app
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Ejecutar un contenedor Redis

```bash
docker run -d --name redis-lab --network red-app redis
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Verificar que está corriendo

```bash
docker ps
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Contenedor temporal con cliente Redis

```bash
docker run -it --name cliente-redis --network red-app redis redis-cli -h redis-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Probar la conexión (debe responder PONG) (dentro del contenedor)

```bash
ping
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Guardar y leer un valor (dentro del contenedor)

```bash
set curso IE0417
get curso
exit
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Limpiar

```bash
docker stop redis-lab
docker rm redis-lab
docker rm cliente-redis
docker network rm red-app
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Qué es Redis en este ejemplo**
  TODO
- **Qué representa `redis-lab`**
  TODO
- **Cómo se conectó el cliente al servidor**
  TODO
- **Qué significa recibir `PONG`**
  TODO
- **Qué enseñanza deja este ejemplo sobre aplicaciones con varios contenedores**
  TODO

### Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

### Preguntas de reflexión

1. **¿Por qué una aplicación web podría necesitar comunicarse con una base de datos?**

   TODO

2. **¿Por qué ambos contenedores deben estar en la misma red?**

   TODO

3. **¿Qué ventaja tiene separar servicios en contenedores distintos?**

   TODO

4. **¿Qué limitación tiene hacerlo manualmente con varios comandos `docker run`?**

   TODO
