# Parte 6: Persistencia con volúmenes

## Objetivo

Comprender por qué los datos dentro de un contenedor pueden perderse y cómo los volúmenes permiten persistir información.

## Actividades realizadas

### Crear un volumen

```bash
docker volume create datos-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Listar los volúmenes

```bash
docker volume ls
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Ejecutar Ubuntu montando el volumen

```bash
docker run -it --name contenedor-volumen -v datos-lab:/datos ubuntu bash
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
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

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Eliminar el segundo contenedor

```bash
docker rm contenedor-volumen-2
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Inspeccionar el volumen

```bash
docker volume inspect datos-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

## Documentación requerida

- **Qué es un volumen**
  TODO
- **Cómo se crea**
  TODO
- **Cómo se monta en un contenedor**
  TODO
- **Qué pasó con el archivo después de eliminar el primer contenedor**
  TODO
- **Resultado de `docker volume inspect`**
  TODO

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
