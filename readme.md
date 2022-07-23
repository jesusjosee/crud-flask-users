## Descripción:
Esta es una aplicación crud para gestioanr usuarios creada con Flask y empaquetada en docker como un microservicio.

## Alcances del desarrollo (nivel desarrollado):
- La aplicación es un microservicio para consultar los usuarios , actualizar y modificarl Y eliminarlos,
es decir realiza todas las operaciones CRUD.
- La aplicaciónfue desarrollada con flask y algunas extensiones como flask-sqlAlchemy para manejar las base de datos sqlite asi como flask-restx para generar la documentacion con swagger.

## Indicaciones de como ejecutar la solución:

1. Clonar el respositorio o descomprimir el archivo, segun como se descargo el proyecto.

2. Ejecutar el siguiente comando en la terminal
    $ docker-compose build

3.  Ejecutar el siguiente comando en la terminal
    $ docker-compose up -d

4 . ir a la dirección http://127.0.0.1:5000/ y probar la api.
### Requerimientos:
    - Tener instalado Docker

*************************************************

# ENGLISH VERSION
## Description:
This is a user crud app built with Flask and packaged in docker as a microservice.

## Scope of development (developed level):
- The application is a microservice to query users, update and modify and delete them,
that is, perform all CRUD operations.
- The application was developed with flask and some extensions such as flask-sqlAlchemy to handle the sqlite database as well as flask-restx to generate documentation with swagger.

## Run the Application
1. clone Repository or unzip the folder

2. execute in the terminal
    $ docker-compose build

3. execute in the terminal
    $ docker-compose up -d

4. go to the address http://127.0.0.1:5000/ and try it the api.

### Requirements:
    1. Have installed Docker