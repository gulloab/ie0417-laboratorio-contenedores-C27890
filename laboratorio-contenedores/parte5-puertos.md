# Parte 5: Publicación de puertos

## Objetivo

Comprender cómo exponer una aplicación que corre dentro de un contenedor para accederla desde la máquina anfitriona.

## Actividades realizadas

### Ejecutar publicando el puerto 5000

```bash
docker run --name app-puertos -p 5000:5000 laboratorio-flask:1.0
# Abrir http://localhost:5000 y http://localhost:5000/info
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

### Detener y eliminar

```bash
docker stop app-puertos
docker rm app-puertos
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
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
  TODO
- **Qué significa `-p 8080:5000`**
  TODO
- **Cuál puerto pertenece al host**
  TODO
- **Cuál puerto pertenece al contenedor**
  TODO
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

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Inspeccionar el contenedor

```bash
docker inspect app-logs
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
```

#### Uso de recursos

```bash
docker stats
```

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
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
  TODO
- **Qué tipo de información muestra `docker inspect`**
  TODO
- **Qué información muestra `docker stats`**
  TODO

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

**Explicación:** TODO: ¿para qué sirve este comando? (con tus palabras)

**Resultado obtenido:**

```text
TODO: pega aquí la salida de la terminal (o enlaza una captura: ![captura](img/archivo.png))
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
  TODO
- **Qué cambió en la aplicación**
  TODO
- **Por qué no fue necesario reconstruir la imagen**
  TODO
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
