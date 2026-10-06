
# Laboratorio 2: Introducción práctica a contenedores con Docker


**Enlace al repositorio:** https://github.com/gulloab/ie0417-laboratorio-contenedores-C27890.git
## Índice
1. [Parte 1: Verificación de instalación](parte1-verificacion.md)
2. [Parte 2: Primer contenedor](parte2-comandos-basicos.md)
3. [Parte 3 y 4: Imágenes, contenedores y administración](parte3-imagenes-y-contenedores.md)
4. [Parte 5 y 6: Creación de aplicación y Dockerfile](parte4-dockerfile.md)
5. [Parte 7, 8 y 9: Puertos, logs y variables de entorno](parte5-puertos.md)
6. [Parte 10 y 11: Persistencia con volúmenes](parte6-volumenes.md)
7. [Parte 12 y 13: Redes y bases de datos simuladas](parte7-redes.md)
8. [Parte 14: Limpieza del ambiente](parte8-limpieza.md)

---

## Reflexión final

**1. ¿Qué es un contenedor?**
Un contenedor es una unidad de software ligera, autónoma y ejecutable que empaqueta una aplicación junto con todas sus dependencias, librerías y configuraciones necesarias para funcionar. Esto permite que el código se ejecute de manera predecible independientemente del entorno.

**2. ¿Qué problema resuelve Docker?**
Docker resuelve el clásico problema de "en mi máquina sí funciona". Proporciona un estándar para desarrollar, empaquetar, distribuir y ejecutar aplicaciones, garantizando que el entorno de desarrollo sea idéntico al de pruebas y producción, eliminando los conflictos de compatibilidad en el sistema anfitrión.

**3. ¿Qué diferencia hay entre una imagen y un contenedor?**
Una imagen es una plantilla inmutable y de solo lectura que contiene el código fuente, las librerías y las dependencias (funciona como un plano de construcción)[. Un contenedor es la instancia viva y en ejecución creada a partir de esa imagen.

**4. ¿Qué diferencia hay entre un contenedor y una máquina virtual?**
Una máquina virtual emula el hardware de una computadora completa y requiere instalar un sistema operativo invitado completo, lo que consume muchos recursos. Un contenedor es mucho más ligero porque no emula hardware; comparte el kernel del sistema operativo del anfitrión y solo aísla los procesos específicos de la aplicación.

**5. ¿Qué aprendió sobre puertos?**
Aprendí que los contenedores están completamente aislados por defecto, incluyendo su red. Para acceder a una aplicación (como un servidor web Flask) desde el exterior, es obligatorio mapear un puerto de la máquina anfitriona hacia un puerto específico dentro del contenedor usando banderas como `-p 8080:5000`. 

**6. ¿Qué aprendió sobre volúmenes?**
Comprendí que los contenedores son efímeros, lo que significa que al eliminarlos se pierde cualquier dato generado en su interior. Los volúmenes (manejados por Docker) y los *bind mounts* (mapeando carpetas locales) solucionan esto, permitiendo almacenar bases de datos, configuraciones o código de manera persistente en el sistema host.

**7. ¿Qué aprendió sobre redes?**
Aprendí que se pueden crear redes virtuales internas donde múltiples contenedores se comunican entre sí de forma segura. En lugar de depender de direcciones IP estáticas, Docker integra un servidor DNS interno que permite a los contenedores encontrarse mutuamente utilizando simplemente sus nombres (por ejemplo, conectando un backend directamente a un contenedor llamado `redis-lab`).

**8. ¿En qué casos usaría Docker en un proyecto de software?**
Lo utilizaría para desplegar herramientas de visualización y APIs (como dashboards de telemetría en Python/Flask), para configurar entornos de compilación reproducibles sin ensuciar mi sistema operativo (por ejemplo, aislando cadenas de herramientas complejas para C/C++), o para levantar rápidamente bases de datos y servicios en red necesarios para probar arquitecturas de software sin configuraciones manuales.

**9. ¿Qué parte del laboratorio le pareció más útil?**
Lo más útil fue la creación de imágenes personalizadas y el uso del comando docker build. Aprender a estructurar un Dockerfile paso a paso para empaquetar nuestro propio código (como la aplicación de Flask) junto con sus dependencias me ayudó a entender realmente cómo se estandariza el software. Es muy práctico ver cómo una vez construida la imagen, esta se puede distribuir y ejecutar en cualquier entorno sin preocuparse por problemas de configuración local.

**10. ¿Qué parte le pareció más confusa?**
Al principio me enredé un poco con el orden y la sintaxis a la hora de mapear los puertos (host:contenedor) y lidiando con los permisos en la terminal de Linux. También me pareció bastante confusa la parte de correr el contenedor de Ubuntu, específicamente cuando creamos y nombramos al de mi-ubuntu; la verdad al inicio no entendía muy bien cuál era la funcionalidad o el propósito de levantarlo. Por último, me tomó un rato aterrizar la idea de cómo funciona el aislamiento de red cuando se ponen a hablar dos aplicaciones distintas (como Flask y Redis) en una misma red personalizada.
