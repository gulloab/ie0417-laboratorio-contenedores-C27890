<!-- BORRADOR: reescribe las explicaciones y respuestas con tus propias palabras (el enunciado lo exige) y completa los TODO pendientes. Borra este comentario al terminar. -->

# Parte 7: Redes de Docker

## Objetivo

Crear una red personalizada y comunicar contenedores entre sí usando nombres.

## Actividades realizadas

### Crear una red

```bash
docker network create red-lab
```

**Explicación:** Crea una red de Docker (tipo bridge por defecto) llamada `red-lab`; imprime su ID.

**Resultado obtenido:**

```text
480ddaddf75c641241a9de65b3414148d25cb749faa984637794db97ff780c27
```

### Listar las redes

```bash
docker network ls
```

**Explicación:** Lista las redes. Además de las que Docker crea por defecto (`bridge`, `host`, `none`) aparece `red-lab`.

**Resultado obtenido:**

```text
NETWORK ID     NAME      DRIVER    SCOPE
f075f1682609   bridge    bridge    local
22014559ada9   host      host      local
12da644ac6f6   none      null      local
480ddaddf75c   red-lab   bridge    local
```

### Ejecutar un contenedor con Nginx

```bash
docker run -d --name servidor-web --network red-lab nginx
```

**Explicación:** Ejecuta Nginx en segundo plano (`-d`) con el nombre `servidor-web`, conectado a la red `red-lab`. Como la imagen no estaba en mi máquina, Docker la descargó primero.

**Resultado obtenido:**

```text
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
f1169c633cbc: Downloading [====================>                              ]  13.63MB/33.57MB
f802f27d954b: Download complete 
3326c3817340: Download complete 
46243d3234ed: Download complete 
afa8dec48454: Download complete 
2056b40bae09: Download complete 
37d8c7707e42: Download complete 
e40088050cb6: Download complete 
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
  Una red virtual que conecta contenedores entre sí y con el exterior. Docker crea una red `bridge` por defecto y permite crear redes personalizadas.
- **Qué hace `docker network create`**
  Crea una red nueva (por defecto de tipo bridge) con el nombre indicado.
- **Qué significa conectar contenedores a la misma red**
  Que pueden comunicarse entre sí, incluso usando el nombre del contenedor como dirección.
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
