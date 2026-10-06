<!-- BORRADOR: reescribe las explicaciones y respuestas con tus propias palabras (el enunciado lo exige) y completa los TODO pendientes. Borra este comentario al terminar. -->

# Parte 3: Imágenes y contenedores

## Objetivo

Comprender la diferencia entre una imagen y un contenedor.

## Actividades realizadas

### Descargar una imagen de Ubuntu

```bash
docker pull ubuntu
```

**Explicación:** Descarga la imagen `ubuntu` (etiqueta `latest` por defecto) desde Docker Hub a mi máquina, sin crear ningún contenedor.

**Resultado obtenido:**

```text
Using default tag: latest
latest: Pulling from library/ubuntu
06ad70e463aa: Pull complete 
4e07a0f12b2c: Pull complete 
8f70d2bfe91a: Download complete 
Digest: sha256:f144425ff09be612d6d9ad965196e9cdc23dae1f42110a8a11a3e9a8198759f7
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

### Listar las imágenes disponibles

```bash
docker images
```

**Explicación:** Lista las imágenes locales con su nombre y etiqueta, ID y tamaño. Aquí aparecen `hello-world`, `laboratorio-flask:1.0`, `python:3.11-slim` y `ubuntu:latest`.

**Resultado obtenido:**

```text
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest      5e2309035332       25.9kB         9.49kB    U   
laboratorio-flask:1.0   fbdbfcb045df        222MB         54.3MB        
python:3.11-slim        6f31d6e9ba2b        200MB         50.8MB        
ubuntu:latest           f144425ff09b        162MB         45.6MB        
```

### Ejecutar un contenedor interactivo

```bash
docker run -it ubuntu bash
```

**Explicación:** Crea un contenedor de Ubuntu y abre una shell `bash` dentro de él. `-i` mantiene la entrada estándar abierta y `-t` asigna una terminal. El prompt `root@1c35b5ebc80f:/#` indica que estoy dentro del contenedor (su nombre de host es el ID del contenedor).

**Resultado obtenido:**

```text
root@1c35b5ebc80f:/# 
```

### Explorar el contenedor (dentro del contenedor)

```bash
ls
pwd
cat /etc/os-release
```

**Explicación:** `ls` lista los archivos del directorio actual (la raíz `/` del contenedor), `pwd` muestra el directorio actual y `cat /etc/os-release` muestra la información del sistema operativo: Ubuntu 26.04.1 LTS.

**Resultado obtenido:**

```text
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
/
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
```

### Salir del contenedor (dentro del contenedor)

```bash
exit
```

**Explicación:** Cierra la shell. Como `bash` era el proceso principal del contenedor, al terminar la shell el contenedor también termina.

**Resultado obtenido:**

```text
exit
```

### Listar los contenedores

```bash
docker ps -a
```

**Explicación:** Lista todos los contenedores. Aparece el de Ubuntu con estado `Exited (0)` y un nombre aleatorio asignado por Docker (`competent_mirzakhani`).

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                      PORTS     NAMES
b54082ea3156   ubuntu    "bash"    41 seconds ago   Exited (0) 29 seconds ago             competent_mirzakhani
```

## Documentación requerida

- **Qué hace `docker pull`**
  Descarga una imagen desde un registro (por defecto Docker Hub) y la guarda localmente; no crea ningún contenedor.
- **Qué muestra `docker images`**
  Las imágenes disponibles en mi máquina: nombre y etiqueta, ID y tamaño en disco.
- **Qué significa ejecutar un contenedor en modo interactivo**
  Ejecutarlo conectado a mi terminal (opciones `-it`) para escribirle comandos en vivo, en lugar de que corra un programa y termine solo.
- **Qué observé dentro del contenedor Ubuntu**
  Un Linux mínimo, con el usuario `root`, el directorio raíz con las carpetas típicas (`bin`, `etc`, `usr`, etc.) y `/etc/os-release` indicando Ubuntu 26.04.1 LTS (Resolute Raccoon). El nombre del host del prompt era el ID del contenedor.
- **Qué ocurrió al salir del contenedor**
  Con `exit` la shell terminó y, al ser el proceso principal, el contenedor se detuvo: aparece como `Exited (0)` en `docker ps -a`.

## Reflexión personal

Entrar de forma interactiva a un contenedor de Ubuntu demostró físicamente la diferencia entre imagen y contenedor. Resulta fascinante ver cómo se levanta un entorno Linux funcional y aislado en cuestión de segundos, compartiendo el kernel del anfitrión sin el peso de una máquina virtual completa.

## Preguntas de reflexión

1. **¿La imagen Ubuntu es lo mismo que una máquina virtual Ubuntu?**

   No. La imagen Ubuntu es el sistema de archivos de Ubuntu y sus paquetes, sin kernel propio ni un sistema operativo completo arrancado. Una máquina virtual incluye su propio kernel y virtualiza el hardware; el contenedor es un proceso aislado.

2. **¿Por qué el contenedor puede parecer un sistema Linux si no es una máquina virtual completa?**

   Porque la imagen trae el sistema de archivos y las herramientas de Ubuntu (bash, `/etc/os-release`, apt) y el contenedor tiene su propio espacio aislado de procesos, red y archivos. Por dentro se siente como Ubuntu aunque no arranca un sistema operativo completo.

3. **¿Qué significa que el contenedor comparta el kernel con el host?**

   Que los procesos del contenedor usan el mismo kernel de Linux del sistema anfitrión (en mi caso el `7.0.0-27-generic` que muestra `docker info`) y no uno propio. Por eso arrancan rápido y pesan menos que una máquina virtual.

4. **¿Qué diferencia hay entre una imagen descargada y un contenedor creado?**

   La imagen es la plantilla inmutable que se descarga (`ubuntu:latest`); el contenedor es una instancia creada a partir de ella, con su propio estado, que puede estar en ejecución o detenida. De una misma imagen se pueden crear muchos contenedores.


---

## Administración de contenedores

### Objetivo

Aprender a crear, nombrar, detener, iniciar y eliminar contenedores.

### Actividades realizadas

#### Ejecutar un contenedor con nombre

```bash
docker run -it --name mi-ubuntu ubuntu bash
```

**Explicación:** Crea y ejecuta un contenedor Ubuntu interactivo con el nombre `mi-ubuntu` (`--name`).

**Resultado obtenido:**

```text
root@9551abfd49ee:/# 
```

#### Crear un archivo (dentro del contenedor)

```bash
echo "Hola desde el contenedor" > mensaje.txt
```

**Explicación:** Escribe el texto en un archivo `mensaje.txt` dentro del contenedor (el comando no imprime nada).

**Resultado obtenido:**

```text
root@9551abfd49ee:/# echo "Hola desde el contenedor" > mensaje.txt
```

#### Verificar que el archivo existe (dentro del contenedor)

```bash
cat mensaje.txt
```

**Explicación:** Muestra el contenido del archivo y confirma que se creó.

**Resultado obtenido:**

```text
Hola desde el contenedor
```

#### Salir (dentro del contenedor)

```bash
exit
```

**Explicación:** Cierra la shell y el contenedor se detiene.

**Resultado obtenido:**

```text
exit
```

#### Verificar el contenedor

```bash
docker ps -a
```

**Explicación:** Lista todos los contenedores: `mi-ubuntu` aparece detenido (`Exited (0)`) pero sigue existiendo.

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS                          PORTS     NAMES
9551abfd49ee   ubuntu    "bash"    30 seconds ago       Exited (0) 22 seconds ago                 mi-ubuntu
b54082ea3156   ubuntu    "bash"    About a minute ago   Exited (0) About a minute ago             competent_mirzakhani
```

#### Iniciar nuevamente el contenedor

```bash
docker start mi-ubuntu
```

**Explicación:** Reinicia el contenedor existente `mi-ubuntu` (no crea uno nuevo); imprime su nombre.

**Resultado obtenido:**

```text
mi-ubuntu
```

#### Entrar al contenedor

```bash
docker exec -it mi-ubuntu bash
```

**Explicación:** Ejecuta una nueva shell `bash` dentro del contenedor que ya está en ejecución.

**Resultado obtenido:**

```text
root@9551abfd49ee:/# 
```

#### Verificar si el archivo sigue existiendo (dentro del contenedor)

```bash
cat mensaje.txt
```

**Explicación:** Muestra el archivo creado antes: sigue ahí, porque el contenedor no fue eliminado.

**Resultado obtenido:**

```text
Hola desde el contenedor
```

#### Salir nuevamente (dentro del contenedor)

```bash
exit
```

**Explicación:** Cierra la shell de `exec`. Como `bash` de `exec` no era el proceso principal, el contenedor sigue en ejecución hasta detenerlo.

**Resultado obtenido:**

```text
exit
```

#### Detener el contenedor

```bash
docker stop mi-ubuntu
```

**Explicación:** 
Después de docker start mi-ubuntu, el contenedor quedó corriendo en segundo plano. Con docker exec -it mi-ubuntu bash solo abriste una shell adicional, y al hacer exit de ella el contenedor siguió activo. Por eso hay que detenerlo explícitamente con docker stop mi-ubuntu. Para documentarlo, puedes explicar que stop apaga el contenedor sin borrarlo, y que se puede reiniciar mientras no se elimine.



#### Eliminar el contenedor

```bash
docker rm mi-ubuntu
```

**Explicación:** TO
**Resultado obtenido:**



#### Verificar

```bash
docker ps -a
```

**Explicación:** Lista los contenedores: `mi-ubuntu` ya no aparece, solo queda el de nombre aleatorio.

**Resultado obtenido:**

```text
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
b54082ea3156   ubuntu    "bash"    2 minutes ago   Exited (0) 2 minutes ago             competent_mirzakhani
```

### Documentación requerida

- **Uso de `--name`**
  Asigna un nombre propio al contenedor (`mi-ubuntu`) en lugar del aleatorio que genera Docker (como `competent_mirzakhani`), lo que permite referirse a él fácilmente en `start`, `exec`, `stop` y `rm`.
- **Diferencia entre `docker start` y `docker run`**
  `docker run` crea un contenedor nuevo a partir de una imagen y lo ejecuta; `docker start` reinicia un contenedor que ya existe y estaba detenido, conservando su estado.
- **Uso de `docker exec`**
  Ejecuta un comando dentro de un contenedor que ya está en ejecución (aquí `bash` con `-it`, para abrir una shell interactiva) sin crear uno nuevo.
- **Diferencia entre detener y eliminar un contenedor**
  `docker stop` detiene el contenedor pero este sigue existiendo (aparece en `docker ps -a` y se puede reiniciar); `docker rm` lo elimina definitivamente junto con sus datos.
- **Qué pasó con el archivo creado dentro del contenedor**
  `mensaje.txt` siguió existiendo después de salir, reiniciar el contenedor con `docker start` y entrar con `exec`, porque el contenedor no se había eliminado. Al eliminar `mi-ubuntu` con `docker rm`, el contenedor y su archivo desaparecen.

### Reflexión personal

Entrar al contenedor de Ubuntu en modo interactivo me ayudó a visualizar claramente la diferencia entre una imagen y un contenedor. Es increíble ver cómo en cuestión de segundos tienes un entorno Linux funcional y aislado, sin la pesadez de arrancar una máquina virtual completa. Me hizo entender que la imagen es solo el "molde" inmutable, mientras que el contenedor es el sistema vivo en el que podemos trabajar. 

### Preguntas de reflexión

1. **¿Qué ventaja tiene asignar nombres a los contenedores?**

   Es más fácil referirse al contenedor en los comandos (`docker start mi-ubuntu`) que usar un ID o un nombre aleatorio, y se identifica mejor qué hace cada uno.

2. **¿Qué diferencia hay entre crear un contenedor nuevo y reiniciar uno existente?**

   Crear uno nuevo (`docker run`) parte de la imagen limpia y genera otro contenedor; reiniciar uno existente (`docker start`) reutiliza el mismo contenedor con su estado y sus archivos.

3. **¿Qué sucede con los datos creados dentro de un contenedor si este se elimina?**

   Se pierden: los datos viven en la capa de escritura del contenedor y desaparecen al eliminarlo. Para conservarlos se usan volúmenes.

4. **¿Por qué se dice que los contenedores son desechables?**

   Porque se pueden crear, destruir y recrear rápidamente a partir de la imagen sin perder nada importante, siempre que lo valioso (la configuración en la imagen y los datos en volúmenes) esté fuera del contenedor.
