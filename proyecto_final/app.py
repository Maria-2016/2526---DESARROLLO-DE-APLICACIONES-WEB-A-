from flask import Flask, render_template, request, redirect, url_for
from inventario.inventario import Inventario
from inventario.productos import Producto

app = Flask(__name__)

# Creamos una instancia global de tu inventario
mi_inventario = Inventario()

# --- RUTAS BÁSICAS DE NAVEGACIÓN ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    # Asumiendo que tienes un archivo about.html
    return render_template('about.html') 

@app.route('/clientes')
def clientes():
    # Asumiendo que tienes un archivo clientes.html
    return render_template('clientes.html')

@app.route('/ofertas')
def ofertas():
    return render_template('ofertas.html')

# --- RUTAS DE INVENTARIO Y PRODUCTOS ---

@app.route('/productos')
def mostrar_productos():
    # 1. Actualizamos el diccionario con los datos más recientes de MySQL
    mi_inventario.cargar_desde_bd() 
    
    # 2. Convertimos el diccionario en una lista para enviarla al HTML
    lista_productos = mi_inventario.items.values() 
    
    # 3. Renderizamos la plantilla enviando los datos reales
    return render_template('productos.html', productos=lista_productos)

@app.route('/nuevo_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # 1. Capturamos los datos que el usuario escribió en el HTML
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        
        # 2. Creamos el objeto Producto (ID es None porque MySQL lo asigna)
        nuevo_prod = Producto(id=None, nombre=nombre, cantidad=cantidad, precio=precio)
        
        # 3. Usamos tu clase Inventario para guardarlo en la Base de Datos
        mi_inventario.agregar_producto(nuevo_prod)
        
        # 4. Redirigimos a la tabla para ver el producto recién agregado
        return redirect(url_for('mostrar_productos'))
    
    return render_template('producto_form.html')

# 👇 NUEVA RUTA PARA ELIMINAR 👇
@app.route('/eliminar_producto/<int:id>', methods=['POST'])
def eliminar_producto(id):
    # Usamos el método de tu clase Inventario pasándole el ID
    mi_inventario.eliminar_producto(id)
    
    # Redirigimos de vuelta a la tabla de productos
    return redirect(url_for('mostrar_productos'))


@app.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    # Buscamos el producto actual en nuestro diccionario para saber sus datos
    producto_actual = mi_inventario.items.get(id)
    
    if request.method == 'POST':
        # Capturamos los datos nuevos que el usuario escribió
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        
        # Mandamos a actualizar
        mi_inventario.actualizar_producto(id, nombre, cantidad, precio)
        return redirect(url_for('mostrar_productos'))
    
    # Si es GET, mostramos un formulario especial pre-llenado
    return render_template('editar_producto.html', producto=producto_actual)

if __name__ == '__main__':
    app.run(debug=True)
    

    