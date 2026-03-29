import pymysql
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

def obtener_conexion():
    """Establece la conexión con Aiven MySQL."""
    try:
        conexion = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            ssl={"ssl": True}, 
            cursorclass=pymysql.cursors.DictCursor 
        )
        return conexion
    except pymysql.MySQLError as e:
        print(f"❌ Error conectando a MySQL: {e}")
        return None

def inicializar_base_datos():
    """Crea la tabla 'productos' en Aiven si aún no existe."""
    conexion = obtener_conexion()
    if conexion:
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    cantidad INT NOT NULL,
                    precio DECIMAL(10, 2) NOT NULL
                )
                """
                cursor.execute(sql)
            conexion.commit()
            print("✅ Conexión exitosa. Tabla 'productos' lista en Aiven.")
        except Exception as e:
            print(f"❌ Error al crear la tabla: {e}")
        finally:
            conexion.close()

# Esto se ejecuta automáticamente al iniciar la app
inicializar_base_datos()