<!-- BORRADOR: reescribe las explicaciones y respuestas con tus propias palabras (el enunciado lo exige) y completa los TODO pendientes. Borra este comentario al terminar. -->

# Parte 6: Persistencia con volúmenes

## Objetivo

Comprender por qué los datos dentro de un contenedor pueden perderse y cómo los volúmenes permiten persistir información.

## Actividades realizadas

### Crear un volumen

```bash
docker volume create datos-lab
```

**Explicación:** Crea un volumen administrado por Docker llamado `datos-lab`; imprime su nombre.

**Resultado obtenido:**

```text
datos-lab
```

### Listar los volúmenes

```bash
docker volume ls
```

**Explicación:** Lista los volúmenes existentes; aparece `datos-lab` con el driver `local`.

**Resultado obtenido:**

```text
DRIVER    VOLUME NAME
local     datos-lab
```

### Ejecutar Ubuntu montando el volumen

```bash
docker run -it --name contenedor-volumen -v datos-lab:/datos ubuntu bash
```

**Explicación:** Ejecuta un contenedor Ubuntu interactivo y monta el volumen `datos-lab` en la ruta `/datos` del contenedor (`-v datos-lab:/datos`).

**Resultado obtenido:**

```text
root@ae44ba5c0fa7:/# 
```

### Escribir y leer un archivo en el volumen (dentro del contenedor)

```bash
echo "Este archivo está en un volumen" > /datos/archivo.txt
cat /datos/archivo.txt
exit
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Eliminar el contenedor

```bash
docker rm contenedor-volumen
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Nuevo contenedor con el mismo volumen

```bash
docker run -it --name contenedor-volumen-2 -v datos-lab:/datos ubuntu bash
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Verificar el archivo (dentro del contenedor)

```bash
cat /datos/archivo.txt
exit
```

**Explicación:** Lee el archivo desde el segundo contenedor, que montó el mismo volumen `datos-lab` en `/datos`.

**Resultado obtenido:**

```text
Este archivo está en un volumen
```

### Eliminar el segundo contenedor

```bash
docker rm contenedor-volumen-2
```

**Explicación:** Elimina el segundo contenedor; imprime su nombre.

**Resultado obtenido:**

```text
contenedor-volumen-2
```

### Inspeccionar el volumen

```bash
docker volume inspect datos-lab
```

**Explicación:** Muestra los detalles del volumen: nombre, driver `local` y dónde guarda Docker los datos en el host (`Mountpoint`).

**Resultado obtenido:**

```text
[
    {
        "CreatedAt": "2026-10-05T21:56:52-06:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/datos-lab/_data",
        "Name": "datos-lab",
        "Options": null,
        "Scope": "local"
    }
]
```

## Documentación requerida

- **Qué es un volumen**
  Un espacio de almacenamiento administrado por Docker, independiente del ciclo de vida de los contenedores, que sirve para persistir datos.
- **Cómo se crea**
  Con `docker volume create datos-lab`.
- **Cómo se monta en un contenedor**
  Con la opción `-v nombre_volumen:ruta_en_contenedor`, por ejemplo `-v datos-lab:/datos`.
- **Qué pasó con el archivo después de eliminar el primer contenedor**
  TODO
- **Resultado de `docker volume inspect`**
  Está copiado arriba: driver `local` y punto de montaje `/var/lib/docker/volumes/datos-lab/_data`, es decir, los datos viven en el host y no dentro de un contenedor.

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Qué problema resuelven los volúmenes?**

   TODO

2. **¿El volumen pertenece a un contenedor específico?**

   TODO

3. **¿Qué diferencia hay entre eliminar un contenedor y eliminar un volumen?**

   TODO

4. **¿Para qué casos reales se usarían volúmenes?**

   TODO


---

## Bind mounts

### Objetivo

Comprender la diferencia entre un volumen administrado por Docker y montar una carpeta local dentro de un contenedor.

> Nota para Windows (PowerShell): usar `-v ${PWD}:/app` en lugar de `-v "$(pwd)":/app`.

### Actividades realizadas

#### Ejecutar con bind mount (desde la carpeta `app/`)

```bash
docker run --name app-bind -p 5000:5000 -v "$(pwd)":/app laboratorio-flask:1.0
# Abrir http://localhost:5000
# Modificar app.py en el host (por ejemplo, el mensaje HTML)
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Detener y eliminar

```bash
docker stop app-bind
docker rm app-bind
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Volver a ejecutar

```bash
docker run --name app-bind-2 -p 5000:5000 -v "$(pwd)":/app laboratorio-flask:1.0
# Abrir http://localhost:5000
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Finalizar

```bash
docker stop app-bind-2
docker rm app-bind-2
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Qué diferencia hay entre `datos-lab:/datos` y `"$(pwd)":/app`**
  TODO
- **Qué ocurrió al modificar el código local**
  TODO
- **Por qué esto puede ser útil durante el desarrollo**
  TODO

### Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

### Preguntas de reflexión

1. **¿Qué diferencia hay entre un volumen y un bind mount?**

   TODO

2. **¿Cuál parece más conveniente para desarrollo?**

   TODO

3. **¿Cuál parece más conveniente para datos persistentes de una aplicación?**

   TODO

4. **¿Qué riesgos podría tener montar carpetas del host dentro del contenedor?**

   TODO
