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

**Explicación:** Crea un contenedor Ubuntu interactivo llamado `cliente`, conectado a la misma red `red-lab` que `servidor-web`. Sirve como cliente para probar la comunicación entre contenedores.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Instalar curl (dentro del contenedor)

```bash
apt update
apt install -y curl
```

**Explicación:** `apt update` actualiza la lista de paquetes e `apt install -y curl` instala `curl`, una herramienta para hacer peticiones HTTP desde la terminal. La imagen de Ubuntu no la trae por defecto.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Probar la conexión hacia el servidor (dentro del contenedor)

```bash
curl http://servidor-web
exit
```

**Explicación:** `curl http://servidor-web` hace una petición HTTP al contenedor de Nginx usando su nombre en lugar de una IP; `exit` cierra la shell del cliente.



### Detener y eliminar contenedores

```bash
docker stop servidor-web
docker rm servidor-web
docker rm cliente
```

**Explicación:** `docker stop` detiene `servidor-web` y los `docker rm` eliminan `servidor-web` y `cliente` (este ya estaba detenido porque salí de su shell).

**Resultado obtenido:**

### Eliminar la red

```bash
docker network rm red-lab
```

**Explicación:** Elimina la red `red-lab`. Solo se puede borrar si ningún contenedor la está usando.



## Documentación requerida

- **Qué es una red en Docker**
  Una red virtual que conecta contenedores entre sí y con el exterior. Docker crea una red `bridge` por defecto y permite crear redes personalizadas.
- **Qué hace `docker network create`**
  Crea una red nueva (por defecto de tipo bridge) con el nombre indicado.
- **Qué significa conectar contenedores a la misma red**
  Que pueden comunicarse entre sí, incluso usando el nombre del contenedor como dirección.
- **Qué ocurrió al ejecutar `curl http://servidor-web`**
  TODO: describe lo que viste en tu terminal (la respuesta HTML de Nginx) y pega la salida arriba.
- **Por qué se pudo usar el nombre `servidor-web`**
  Porque en una red personalizada Docker ofrece un DNS interno que resuelve el nombre de cada contenedor a su IP. Por eso `cliente` pudo llamar a `servidor-web` por nombre, algo que la red `bridge` por defecto no hace.

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Por qué los contenedores necesitan redes?**

   Para poder comunicarse entre sí y con el exterior aunque estén aislados. Sin una red, un contenedor no podría pedirle datos a otro.

2. **¿Qué ventaja tiene usar nombres de contenedor en lugar de direcciones IP?**

   La IP de un contenedor puede cambiar cada vez que se crea o reinicia, mientras que el nombre se mantiene. Usar nombres hace la configuración más estable y más fácil de leer.

3. **¿Qué diferencia hay entre publicar un puerto hacia el host y comunicarse dentro de una red Docker?**

   Publicar un puerto (`-p`) expone el servicio al host y al exterior. Dentro de una red Docker los contenedores se hablan directamente por nombre sin exponer nada al host; por eso `servidor-web` no necesitó `-p` para que `cliente` lo alcanzara.

4. **¿Qué ejemplos reales podrían usar una red Docker?**

   Una aplicación web con su base de datos, un backend con una caché como Redis, varios microservicios que se llaman entre sí, o un proxy inverso con los servicios que protege.


---

## Comunicación entre servicios

### Objetivo

Comprender cómo una aplicación podría comunicarse con otro servicio dentro de una red Docker, sin usar todavía Docker Compose.

### Actividades realizadas

#### Crear una red

```bash
docker network create red-app
```

**Explicación:** Crea una red llamada `red-app` para que los contenedores de este ejemplo se comuniquen.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Ejecutar un contenedor Redis

```bash
docker run -d --name redis-lab --network red-app redis
```

**Explicación:** Ejecuta Redis en segundo plano (`-d`) con el nombre `redis-lab`, conectado a `red-app`. Redis hace de base de datos simulada del ejemplo.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Verificar que está corriendo

```bash
docker ps
```

**Explicación:** Lista los contenedores en ejecución; debe aparecer `redis-lab` con estado `Up`.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Contenedor temporal con cliente Redis

```bash
docker run -it --name cliente-redis --network red-app redis redis-cli -h redis-lab
```

**Explicación:** Crea otro contenedor a partir de la imagen `redis`, pero ejecutando `redis-cli -h redis-lab`, el cliente de línea de comandos, que apunta al servidor por su nombre en la red `red-app`.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Probar la conexión (debe responder PONG) (dentro del contenedor)

```bash
ping
```

**Explicación:** `ping` es un comando de Redis para comprobar que el servidor responde; si todo funciona contesta `PONG`.

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

**Explicación:** `set curso IE0417` guarda un valor con la clave `curso`, `get curso` lo lee y `exit` sale del cliente.

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

**Explicación:** Detiene y elimina el servidor Redis y el cliente, y elimina la red `red-app`.

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Qué es Redis en este ejemplo**
  Una base de datos en memoria de tipo clave-valor. Aquí representa el servicio de datos al que una aplicación se conectaría.
- **Qué representa `redis-lab`**
  El nombre del contenedor del servidor Redis; dentro de la red `red-app` funciona como nombre de host para encontrarlo.
- **Cómo se conectó el cliente al servidor**
  Ambos contenedores están en `red-app` y el cliente usó `redis-cli -h redis-lab`; el DNS interno de Docker resuelve `redis-lab` a la IP del servidor.
- **Qué significa recibir `PONG`**
  Es la respuesta de Redis al comando `ping`: confirma que el cliente llegó al servidor y que este está funcionando.
- **Qué enseñanza deja este ejemplo sobre aplicaciones con varios contenedores**
  Una aplicación se puede dividir en servicios separados (por ejemplo app y base de datos) que se comunican por red usando nombres, sin instalar todo en un solo contenedor.

### Reflexión personal

Crear la red red-lab y comunicar Ubuntu con Nginx me introdujo al concepto de DNS interno de Docker. Entender que los contenedores pueden encontrarse mediante su nombre en lugar de depender de direcciones IP estáticas simplifica enormemente la interconexión de servicios.

### Preguntas de reflexión

1. **¿Por qué una aplicación web podría necesitar comunicarse con una base de datos?**

   Porque guarda y consulta datos persistentes o compartidos (usuarios, sesiones, contenido) que no conviene tener dentro del código ni de un contenedor desechable.

2. **¿Por qué ambos contenedores deben estar en la misma red?**

   Porque en la misma red pueden resolver sus nombres y alcanzarse directamente; en redes distintas están aislados entre sí.

3. **¿Qué ventaja tiene separar servicios en contenedores distintos?**

   Cada servicio se puede actualizar, reiniciar, escalar o reemplazar de forma independiente, y cada contenedor se dedica a una sola tarea.

4. **¿Qué limitación tiene hacerlo manualmente con varios comandos `docker run`?**

   Hay que escribir y mantener a mano muchos comandos, crear la red, respetar el orden y limpiar todo después; es fácil equivocarse y poco reproducible. Docker Compose resuelve esto declarando todo en un archivo.
