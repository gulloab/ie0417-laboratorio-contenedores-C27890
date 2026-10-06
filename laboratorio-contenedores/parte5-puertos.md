# Parte 5: Publicación de puertos

## Objetivo

Comprender cómo exponer una aplicación que corre dentro de un contenedor para accederla desde la máquina anfitriona.

## Actividades realizadas

### Ejecutar publicando el puerto 5000

```bash
docker run --name app-puertos -p 5000:5000 laboratorio-flask:1.0
# Abrir http://localhost:5000 y http://localhost:5000/info
```

**Explicación:** Crea y ejecuta el contenedor `app-puertos` publicando el puerto 5000 del contenedor en el puerto 5000 del host (`-p puerto_host:puerto_contenedor`). Así la app se puede abrir desde el navegador del host en `http://localhost:5000`.

**Resultado obtenido:**

```text
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
```

### Detener y eliminar

```bash
docker stop app-puertos
docker rm app-puertos
```

**Explicación:** `docker stop` detiene el contenedor y `docker rm` lo elimina; cada comando imprime el nombre del contenedor.

**Resultado obtenido:**

```text
app-puertos
app-puertos
```

### Probar con otro puerto del host

```bash
docker run --name app-puertos-2 -p 8080:5000 laboratorio-flask:1.0
# Abrir http://localhost:8080
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Finalizar

```bash
docker stop app-puertos-2
docker rm app-puertos-2
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

## Documentación requerida

- **Qué significa `-p 5000:5000`**
  Publica el puerto 5000 del contenedor en el puerto 5000 del host. El formato es `-p puerto_host:puerto_contenedor`.
- **Qué significa `-p 8080:5000`**
  El puerto 8080 del host se redirige al puerto 5000 del contenedor: la app se abre en `http://localhost:8080`, aunque dentro del contenedor sigue escuchando en el 5000.
- **Cuál puerto pertenece al host**
  El de la izquierda de los dos puntos (5000 en el primer caso, 8080 en el segundo).
- **Cuál puerto pertenece al contenedor**
  El de la derecha (5000, donde escucha Flask dentro del contenedor).
- **Captura del navegador mostrando la aplicación funcionando**
  TODO

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Por qué no basta con que la aplicación escuche en el puerto 5000 dentro del contenedor?**

   TODO

2. **¿Qué función cumple el mapeo de puertos?**

   TODO

3. **¿Cuál es la diferencia entre el puerto del host y el puerto del contenedor?**

   TODO

4. **¿Qué pasaría si dos contenedores intentan usar el mismo puerto del host?**

   TODO


---

## Logs e inspección

### Objetivo

Aprender a observar el comportamiento de un contenedor usando comandos de inspección.

### Actividades realizadas

#### Ejecutar en segundo plano

```bash
docker run -d --name app-logs -p 5000:5000 laboratorio-flask:1.0
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Revisar los logs

```bash
docker logs app-logs
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Seguir los logs en tiempo real

```bash
docker logs -f app-logs
# En otra terminal/navegador visitar / y /info
```

**Explicación:** Muestra los logs en tiempo real (`-f` = follow): cada petición HTTP que recibe Flask aparece al instante. Al visitar `/` y `/info` desde el navegador salen líneas `GET`. Los `404` de `/favicon.ico` son el navegador pidiendo el ícono de la página, que la app no tiene.

**Resultado obtenido:**

```text
172.17.0.1 - - [06/Oct/2026 15:10:24] "GET /info HTTP/1.1" 200 -
172.17.0.1 - - [06/Oct/2026 15:10:24] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [06/Oct/2026 15:10:39] "GET / HTTP/1.1" 200 -
```

#### Inspeccionar el contenedor

```bash
docker inspect app-logs
```

**Explicación:** Muestra en JSON la configuración y el estado del contenedor: estado, imagen, comando, puertos publicados, red e IP, etc. Se ve `State.Status: running`, `Config.Cmd: python app.py`, el mapeo `5000/tcp` hacia `0.0.0.0:5000` y la IP `172.17.0.2` en la red `bridge`.

**Resultado obtenido:**

```text
[
    {
        "Id": "7ac65d984834dd9904f381329519b478c0d686a651715f05a250d1fb375ee9ed",
        "Created": "2026-10-06T15:10:08.250735122Z",
        "Path": "python",
        "Args": [
            "app.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 73191,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2026-10-06T15:10:08.273037486Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:fbdbfcb045df5335511f33c16cbe1465fe3b8bb47758d6200fdb9857fceb1725",
        "Name": "/app-logs",
        "HostConfig": {
            "NetworkMode": "bridge",
            "PortBindings": {
                "5000/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5000"
                    }
                ]
            },
            ...
        },
        "Config": {
            "Hostname": "7ac65d984834",
            "ExposedPorts": {
                "5000/tcp": {}
            },
            "Cmd": [
                "python",
                "app.py"
            ],
            "Image": "laboratorio-flask:1.0",
            "WorkingDir": "/app",
            ...
        },
        "NetworkSettings": {
            "Ports": {
                "5000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5000"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "5000"
                    }
                ]
            },
            "Networks": {
                "bridge": {
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "MacAddress": "c2:12:7f:60:a2:ab",
                    ...
                }
            }
        },
        ...
(salida parcial: se omiten campos con "...")
```

#### Uso de recursos

```bash
docker stats
```

**Explicación:** Muestra en vivo el uso de recursos del contenedor: CPU, memoria, red, disco y número de procesos. `app-logs` usa 0.02% de CPU y 21.81MiB de los 7.039GiB disponibles (0.30%).

**Resultado obtenido:**

```text
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O    PIDS 
7ac65d984834   app-logs   0.02%     21.81MiB / 7.039GiB   0.30%     20.8kB / 2.14kB   0B / 147kB   1 
```

#### Detener y eliminar

```bash
docker stop app-logs
docker rm app-logs
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Qué muestra `docker logs`**
  TODO
- **Para qué sirve `docker logs -f`**
  Para seguir los logs del contenedor en tiempo real: mientras esté abierto, cada petición nueva que recibe la app aparece de inmediato. Se sale con `Ctrl+C`.
- **Qué tipo de información muestra `docker inspect`**
  Información detallada en JSON: estado y fechas, imagen, comando, variables de entorno, puertos publicados, red (IP y gateway), montajes, límites de recursos y configuración de logs.
- **Qué información muestra `docker stats`**
  Uso de recursos en tiempo real por contenedor: porcentaje de CPU, memoria usada y límite, tráfico de red, lectura/escritura en disco y número de procesos.

### Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

### Preguntas de reflexión

1. **¿Por qué los logs son importantes al trabajar con contenedores?**

   TODO

2. **¿Qué diferencia hay entre ver logs históricos y logs en tiempo real?**

   TODO

3. **¿Qué información útil se puede obtener con `docker inspect`?**

   TODO

4. **¿Por qué es importante observar el consumo de recursos?**

   TODO


---

## Variables de entorno

### Objetivo

Configurar el comportamiento de un contenedor usando variables de entorno.

### Actividades realizadas

#### Ejecutar con una variable de entorno

```bash
docker run --name app-env -p 5000:5000 -e MENSAJE="Hola desde una variable de entorno" laboratorio-flask:1.0
# Abrir http://localhost:5000
```

**Explicación:** Ejecuta la app pasándole la variable `MENSAJE` con `-e`, que la app lee con `os.environ.get("MENSAJE", ...)`. Corre en primer plano, así que se ven las peticiones en la terminal.

**Resultado obtenido:**

```text
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000

172.17.0.1 - - [06/Oct/2026 15:13:20] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [06/Oct/2026 15:13:37] "GET /info HTTP/1.1" 200 -
172.17.0.1 - - [06/Oct/2026 15:13:37] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [06/Oct/2026 15:13:39] "GET /info HTTP/1.1" 200 -
172.17.0.1 - - [06/Oct/2026 15:13:39] "GET /favicon.ico HTTP/1.1" 404 -
```

#### Detener y eliminar

```bash
docker stop app-env
docker rm app-env
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Ejecutar con otro mensaje

```bash
docker run --name app-env-2 -p 5000:5000 -e MENSAJE="Configuración cambiada sin modificar la imagen" laboratorio-flask:1.0
# Abrir http://localhost:5000
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Finalizar

```bash
docker stop app-env-2
docker rm app-env-2
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Qué hace la opción `-e`**
  Define una variable de entorno dentro del contenedor al crearlo (`-e NOMBRE=valor`). Aquí `MENSAJE` cambia el texto que muestra la página principal.
- **Qué cambió en la aplicación**
  TODO
- **Por qué no fue necesario reconstruir la imagen**
  Porque el mensaje no está fijo en la imagen: el código lo lee de una variable de entorno en tiempo de ejecución. Se cambia la configuración al crear el contenedor sin tocar el código ni el Dockerfile.
- **Capturas o salidas de ambas ejecuciones**
  TODO

### Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

### Preguntas de reflexión

1. **¿Por qué es útil configurar aplicaciones mediante variables de entorno?**

   TODO

2. **¿Qué tipo de información podría configurarse así?**

   TODO

3. **¿Por qué no es buena práctica guardar contraseñas directamente dentro del código?**

   TODO

4. **¿Qué ventaja tiene usar la misma imagen con diferentes configuraciones?**

   TODO
