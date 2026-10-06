# Parte 1: Verificación de la instalación de Docker

## Objetivo

Verificar que Docker está instalado correctamente y que puedo ejecutar comandos básicos desde la terminal.

## Actividades realizadas

### Versión de Docker

```bash
docker --version
```

**Explicación:** Muestra la versión del cliente de Docker instalada; sirve para confirmar que Docker está instalado.

**Resultado obtenido:**

```text
Docker version 29.1.3, build 29.1.3-0ubuntu4.1
```

### Información del sistema Docker

```bash
docker info
```

**Explicación:** Muestra información del cliente y del daemon de Docker. Si responde, significa que el cliente logra comunicarse con el daemon.

**Resultado obtenido:**

```text
Client:
 Version:    29.1.3
 Context:    default
 Debug Mode: false
 Plugins:
  trust: Manage trust on Docker images (Docker Inc.)
    Version:  29.1.3
    Path:     /usr/libexec/docker/cli-plugins/docker-trust

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 10
 Server Version: 29.1.3
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 
 runc version: 
 init version: 
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 7.0.0-27-generic
 Operating System: Ubuntu 26.04 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 8
 Total Memory: 7.039GiB
 Name: gulloab-IdeaPad-3-15ITL6
 ID: 9e218269-6610-4748-a90a-71d737705820
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Firewall Backend: iptables
```

### Ayuda general

```bash
docker help
```

**Explicación:** Muestra la lista de comandos disponibles y una breve descripción de cada uno; sirve de referencia rápida.

**Resultado obtenido:**

```text
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Authenticate to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

Management Commands:
  builder     Manage builds
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  system      Manage Docker
  trust*      Manage trust on Docker images
  volume      Manage volumes

(salida parcial: la ayuda completa continúa con Swarm Commands, Commands y Global Options)
```

## Documentación requerida

- **Versión de Docker instalada**
  Docker 29.1.3 (build 29.1.3-0ubuntu4.1), según `docker --version`.
- **Sistema operativo utilizado**
  Ubuntu 26.04 LTS, kernel 7.0.0-27-generic, arquitectura x86_64 (según `docker info`).
- **Resultado parcial de `docker info`**
  Líneas relevantes: `Server Version: 29.1.3`, `Containers: 0`, `Storage Driver: overlayfs`, `Cgroup Version: 2`, `Operating System: Ubuntu 26.04 LTS`, `CPUs: 8`, `Total Memory: 7.039GiB`. La salida completa está arriba.
- **Qué información muestra `docker info`**
  Información del cliente (versión, plugins) y del servidor o daemon: cantidad de contenedores (en ejecución, pausados, detenidos) e imágenes, versión, driver de almacenamiento, drivers de logging, plugins de red y volumen, runtime, opciones de seguridad (AppArmor, seccomp), kernel, sistema operativo, arquitectura, CPUs y memoria.
- **Por qué es importante verificar la instalación antes de continuar**
  Si Docker no está bien instalado o el daemon no está activo, ningún comando posterior funciona. Verificarlo primero descarta problemas de instalación y confirma el entorno (sistema operativo y recursos) con el que se trabajará.

## Reflexión personal

Confirmar que Docker y su daemon se están ejecutando correctamente en segundo plano es un paso fundamental. Esta verificación inicial evita horas de frustración intentando diagnosticar errores de conexión más adelante en la práctica.

## Preguntas de reflexión

1. **¿Qué diferencia hay entre instalar Docker y tener Docker ejecutándose correctamente?**

   Instalar significa que los programas están en el sistema. Para que Docker funcione, además el daemon debe estar activo y mi usuario debe poder comunicarse con él. Con solo el cliente instalado, `docker --version` funciona, pero `docker info` daría error de conexión al daemon.

2. **¿Qué información útil muestra el comando `docker info`?**

   Versión del cliente y del servidor, cantidad de contenedores e imágenes, driver de almacenamiento, runtime, drivers de red, kernel, sistema operativo, CPUs y memoria. Sirve para confirmar que el daemon responde y conocer el entorno.

3. **¿Por qué Docker necesita un servicio o daemon ejecutándose en segundo plano?**

   Porque el daemon (`dockerd`) es quien realmente crea y administra contenedores, imágenes, redes y volúmenes, y debe estar disponible siempre para atender solicitudes. El comando `docker` es solo un cliente que se comunica con él.
