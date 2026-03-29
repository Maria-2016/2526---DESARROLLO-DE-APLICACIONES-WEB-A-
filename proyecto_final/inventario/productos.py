class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos Getters (para obtener información)
    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    # Métodos Setters (para modificar información)
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio