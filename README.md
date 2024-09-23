# DASHBOARD CON PYTHON  Y MYSQL
### REQUISITOS
- Python 3.x.
- Flask.
- MySQL Connector.
- Matplotlib.

### Objetivos
- Desarrollar la base de datos solicitada, de acuerdo a los requerimientos, en MySQL.
- Realizar la conexión a la base de datos MySQL con MySQL.Connector.
- Realizar el template en formato HTML para la visualización de la página.
- Desarrollar los gráficos utilizando Matpolib y Flask para el desarrollo web.

## Base de datos y Conexión MySQL
Se desarrolla la base de datos en el mismo MySQL o también se puede realizar en Python y luego la conexión con ella, a través de MySQL.Connector. Se muestra a continuación:

**Para la instalación de las dependencias necesarias se debe crear primero un entorno virtual**

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install mysql-connector-python matplotlib flask

**MySQL - dashboard_db**

	-- Crear la tabla solicitada de la prueba
	CREATE TABLE colaboradores (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100),
	edad INT,
	ciudad VARCHAR(100),
	salario DECIMAL (7,2));
	-- Insertar datos para la tabla, solicitado de la prueba
	INSERT INTO colaboradores (nombre, edad, ciudad, salario) VALUES
	('Luis Enrique', 25, 'Lima', 3000.00),
	('Edwar Lopez', 28, 'Huaraz', 2800.00),
	('Omar Salcedo', 24, 'Huancayo', 2500.00),
	('Jorge Rodríguez', 30, 'Cuzco', 3200.00),
	('Ana Marquez', 38, 'Ancash', 5000.00);
	-- Visualización de la tabla
	SELECT * FROM dashboard_db.colaboradores;

**PYTHON - 01.prueba-db.py**

	import mysql.connector
	from mysql.connector import Error

	def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='PErumundial123!!'
        )
        print("Conexión a MySQL exitosa")
    except Error as e:
        print(f"Error: {e}")
    return connection

	def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Base de datos creada exitosamente")
    except Error as e:
        print(f"Error: {e}")

	def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query ejecutada exitosamente")
    except Error as e:
        print(f"Error: {e}")

	# Crear la base de datos
	create_database_query = "CREATE DATABASE IF NOT EXISTS dasboard_db"
	connection = create_connection()
	if connection is not None:
    create_database(connection, create_database_query)
    connection.database = "dashboard_db"

    # Crear la tabla
    create_table_query = """
    CREATE TABLE IF NOT EXISTS colaboradores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        edad INT,
        ciudad VARCHAR(100),
        salario DECIMAL(7, 2)
    )
    """
    execute_query(connection, create_table_query)
    # Insertar registros de prueba
    insert_data_query = """
    INSERT INTO colaboradores (nombre, edad, ciudad, salario)
    VALUES
    ('Luis Enrique', 25, 'Lima', 3000.00),
    ('Edwar Lopez', 28, 'Huaraz', 2800.00),
    ('Omar Salcedo', 24, 'Huancayo', 2500.00),
    ('Jorge Rodríguez', 30, 'Cuzco', 3200.00),
    ('Ana Marquez', 38, 'Ancash', 5000.00);
    """
    execute_query(connection, insert_data_query)
    connection.close()
   	else:
    print("Error en la conexión a MySQL")

** Ejecutando el archivo 01.prueba-db.py, se tendría que tener lo siguiente al ejecutarlo**

	(venv) PS D:\Proyectos_Python\Prueba_Python> python 01.prueba-db.py
	Conexión a MySQL exitosa
	Base de datos creada exitosamente
	Query ejecutada exitosamente
	Query ejecutada exitosamente
	Query ejecutada exitosamente

Por lo tanto, se comprueba que se realizó de manera exitosa la conexión a la base de datos MySQL.

## Estructura para la generación de los gráficos

### 02.dashboard.py

Archivo principal que ejecuta la aplicación Flask.

### templates

Carpeta que contiene el archivo HTML (01.dashboard.html) para el dashboard.

### Gráficos

Se generan dinámicamente a partir de los datos de la base de datos MySQL.

### Ejecución
Se ejecuta el archivo principal para iniciar el servidor, desarrollando lo solicitado:

	python 02.dashboard.py
