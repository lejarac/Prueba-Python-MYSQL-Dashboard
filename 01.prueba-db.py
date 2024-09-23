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

# Eliminar registros existentes
clear_table_query = "DELETE FROM colaboradores"
execute_query(connection, clear_table_query)
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
    ('Ana Marquez', 38, 'Ancash', 5000.00)
    ON DUPLICATE KEY UPDATE
    nombre = VALUES(nombre);
    """
    execute_query(connection, insert_data_query)

    connection.close()
else:
    print("Error en la conexión a MySQL")