from inventario.bd import obtener_conexion
from inventario.productos import Producto

class Inventario:
    def __init__(self):
        # Esta es la colección en memoria que pide la tarea (Diccionario)
        self.items = {} 
        self.cargar_desde_bd()

    def cargar_desde_bd(self):
        """Descarga los productos de Aiven y los guarda en el diccionario."""
        conexion = obtener_conexion()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM productos")
                    filas = cursor.fetchall()
                    
                    self.items.clear() # Limpiar el diccionario antes de llenarlo
                    for fila in filas:
                        producto = Producto(fila['id'], fila['nombre'], fila['cantidad'], fila['precio'])
                        self.items[producto.id] = producto
            finally:
                conexion.close()

    def agregar_producto(self, producto):
        """Guarda un producto nuevo en la Base de Datos y actualiza el diccionario."""
        conexion = obtener_conexion()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    sql = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (producto.nombre, producto.cantidad, producto.precio))
                conexion.commit()
                # Recargar desde la BD para obtener el ID que MySQL le asignó
                self.cargar_desde_bd() 
            finally:
                conexion.close()

    def eliminar_producto(self, id_producto):
        """Elimina un producto de la BD por su ID y lo quita del diccionario."""
        conexion = obtener_conexion()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    # 1. Borramos de la base de datos MySQL
                    sql = "DELETE FROM productos WHERE id = %s"
                    cursor.execute(sql, (id_producto,))
                conexion.commit()
                
                # 2. Borramos del diccionario en memoria (Uso de colecciones para tu tarea)
                if id_producto in self.items:
                    del self.items[id_producto]
                    
            except Exception as e:
                print(f"❌ Error al eliminar: {e}")
            finally:
                conexion.close()

    def actualizar_producto(self, id_producto, nuevo_nombre, nueva_cantidad, nuevo_precio):
        """Actualiza un producto en la BD y en el diccionario."""
        conexion = obtener_conexion()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    # 1. Actualizamos en la base de datos MySQL
                    sql = "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s WHERE id=%s"
                    cursor.execute(sql, (nuevo_nombre, nueva_cantidad, nuevo_precio, id_producto))
                conexion.commit()
                
                # 2. Actualizamos en el diccionario en memoria (Colecciones)
                if id_producto in self.items:
                    producto = self.items[id_producto]
                    producto.nombre = nuevo_nombre
                    producto.set_cantidad(nueva_cantidad)
                    producto.set_precio(nuevo_precio)
            except Exception as e:
                print(f"❌ Error al actualizar: {e}")
            finally:
                conexion.close()