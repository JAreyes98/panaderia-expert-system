# Proyecto de Inteligencia Artificial - Base de datos

## Pasos para montar la base de datos

### 1.- Ejecutar el query Panadería.sql
    "Este query crea la base de datos en SQL Server, en total se crean 7 tablas de las cuales 5 corresponden
    a la base de datos final y las otras son tablas que se utilizan para almacenar los datos temporal mente
    durante la migración de estos mismos a sus respectivas tablas de forma estructurada.
    
    Ademas se crea un procedimiento que servirá para realizar las insercicones masivas de un dataset a la base de datos y una funcion que auto general el codigo del producto la cual es utilizada mas adelante en la inserción de estos productos."

### 2.- Entra ejecutar el archivo main.py que se encuentra en el proyeco llamado migration-dataframe-sqlserver
###     Para esto es necesario utilizar la libreria pyodbc de sqlserver y el de pandas.
    "Este pequeño programa inserta los datos de un dataset a la base de datos, especificamente a la tabla llamada trasactions. Hay que tener cuidado de cambiar los datos de su gestor, como el nombre del servido,
    usuario y contraseña."

### 3.- Ejecuta el query EB-build-goods.sql
    "En este query se encuentran los datos del precio de los productos y estos son ingresados en la tabla goods."

### 4.- Ejecuta el query Datos.sql
    "En este query se encuentran las migraciones de las tablas temporales que se llenaron por la inserccion masiva del dataset a la base de datos y se reinsertan en tablas relacionales de la base de datos final."


### 5.- Finalmente se debe ejecutar el query Cursores.sql
    "Finalmente se crean cursores que insertan y actualizan datos y tablas en la base de datos, dejandola lista para su respectivo funcionamiento." 