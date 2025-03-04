# Proyecto

Repositorio con código base para el desarrollo de una arquitectura hexagonal siguiendo los principios y patrones de DDD.


## Estructura del proyecto

El repositorio en su raíz está estructurado de la siguiente forma:

- **.github**: Directorio donde se localizan templates para Github y los CI/CD workflows 
- **src**: En este directorio encuentra el código fuente para AeroAlpes. En la siguiente sección se explica un poco mejor la estructura del mismo ([link](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure%3E) para más información)
- **tests**: Directorio con todos los archivos de prueba, tanto unitarios como de integración. Sigue el estándar [recomendado por pytest](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html) y usado por [boto](https://github.com/boto/boto).
- **.gitignore**: Archivo con la definición de archivos que se deben ignorar en el repositorio GIT
- **.gitpod.yml**: Archivo que define las tareas/pasos a ejecutar para configurar su workspace en Gitpod
- **README.md**: El archivo que está leyendo :)
- **requirements.txt**: Archivo con los requerimientos para el correcto funcionamiento del proyecto (librerias Python)


## Ejecutar Aplicación Saludteh

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/saludtech/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/saludtech/api --debug run
```


## Ejecutar Aplicación Clientes

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/clientes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/clientes/api --debug run


## Requisitos Previos
Tener instalado Docker y Docker Compose.
Asegurarse de que los puertos utilizados en el docker-compose.yml (como 6650, 8080, 5000 y 5002) estén libres en el host o ajustarlos según sea necesario.


##Estructura de Servicios en Docker Compose
El archivo docker-compose.yml define tres servicios:

pulsar:
Se levanta el broker de Apache Pulsar en modo standalone, exponiendo los puertos 6650 (para clientes) y 8080 (para la consola web).

app:
Es el microservicio principal (por ejemplo, de SaludTec) que se expone en el puerto 5000.

clients:
Es el microservicio de clientes/vuelos, el cual se mapea en el host al puerto 5002 para evitar conflictos con el servicio "app".

## Pasos para Desplegar

```bash
docker-compose up --build
```
Esto construirá las imágenes (si es que no existen) y levantará todos los contenedores definidos

## Verificar el Despliegue

El microservicio app estará disponible en: http://localhost:5000
El microservicio clients estará disponible en: http://localhost:5002
La consola web de Apache Pulsar estará disponible en: http://localhost:8080

## Notas Adicionales
Si algún puerto está en conflicto (por ejemplo, el host ya usa el puerto 5001), modifique el mapeo en el archivo docker-compose.yml.
Asegúrese de que la variable de entorno PULSAR_SERVICE_URL esté correctamente definida en cada servicio que lo requiera, para que el PulsarClient se conecte al broker. En este ejemplo, se usa:
yaml
Copiar
- PULSAR_SERVICE_URL=pulsar://pulsar:6650
Esto permite que, desde dentro de los contenedores, el nombre pulsar se resuelva correctamente.

