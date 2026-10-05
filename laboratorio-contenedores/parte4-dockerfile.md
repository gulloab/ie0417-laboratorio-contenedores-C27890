# Parte 4: Aplicación sencilla y Dockerfile

## Objetivo

Crear una aplicación web mínima (Flask) y ejecutarla dentro de un contenedor construyendo una imagen personalizada con un Dockerfile.

Código en la carpeta [`app/`](app/): `app.py`, `requirements.txt` y `Dockerfile`.

## Actividades realizadas

### Instalar dependencias (local, opcional)

```bash
pip install -r requirements.txt
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Ejecutar localmente (opcional)

```bash
python app.py
# Abrir http://localhost:5000
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

## Documentación requerida

- **Qué hace la aplicación**
  TODO
- **Qué rutas tiene (`/` y `/info`)**
  TODO
- **Qué dependencia utiliza**
  TODO
- **Por qué se usa `host="0.0.0.0"` en lugar de `localhost`**
  TODO

## Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

## Preguntas de reflexión

1. **¿Qué hace Flask en esta aplicación?**

   TODO

2. **¿Para qué sirve el archivo `requirements.txt`?**

   TODO

3. **¿Por qué una aplicación dentro de un contenedor debe escuchar en `0.0.0.0`?**

   TODO

4. **¿Qué diferencia hay entre ejecutar la aplicación localmente y ejecutarla dentro de Docker?**

   TODO


---

## Construir una imagen con Dockerfile

### Objetivo

Construir una imagen personalizada usando un `Dockerfile`.

### Instrucciones del Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

| Instrucción | Qué hace (con mis palabras) |
|---|---|
| `FROM` | TODO |
| `WORKDIR` | TODO |
| `COPY` | TODO |
| `RUN` | TODO |
| `EXPOSE` | TODO |
| `CMD` | TODO |

### Actividades realizadas

#### Construir la imagen

```bash
cd app
docker build -t laboratorio-flask:1.0 .
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Listar las imágenes

```bash
docker images
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Ejecutar un contenedor

```bash
docker run --name app-lab laboratorio-flask:1.0
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Revisar los contenedores (en otra terminal)

```bash
docker ps
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Detener el contenedor

```bash
docker stop app-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Eliminar el contenedor

```bash
docker rm app-lab
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Documentación requerida

- **Qué significa construir una imagen**
  TODO
- **Qué significa el nombre `laboratorio-flask:1.0`**
  TODO
- **Qué diferencia hay entre el nombre de la imagen y el nombre del contenedor**
  TODO
- **Resultado de `docker images`**
  TODO

### Reflexión personal

TODO: breve reflexión sobre lo que hiciste en esta parte.

### Preguntas de reflexión

1. **¿Qué es una imagen base?**

   TODO

2. **¿Por qué se usa una imagen `slim`?**

   TODO

3. **¿Por qué se copian primero las dependencias y luego el resto del código?**

   TODO

4. **¿Qué diferencia hay entre `RUN` y `CMD`?**

   TODO

5. **¿Qué pasaría si se elimina la imagen pero no el Dockerfile?**

   TODO
