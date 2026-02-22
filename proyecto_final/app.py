# app.py - proyecto_final
# Sistema: Tienda Online – Catálogo y Ofertas

from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return 'Bienvenido a Tienda Online – Catálogo y Ofertas. Explora nuestros productos disponibles.'

# Ruta informativa del sistema
@app.route('/sobre-tienda')
def sobre_tienda():
    return 'Tienda Online ofrece productos tecnológicos, accesorios y promociones especiales para nuestros clientes.'

# Ruta dinámica para consultar productos
@app.route('/producto/<nombre>')
def producto(nombre):
    return f'Producto: {nombre} – disponible para compra.'

# Ruta dinámica para clientes
@app.route('/cliente/<nombre>')
def cliente(nombre):
    return f'Bienvenido, {nombre}. Gracias por visitar nuestra Tienda Online.'

# Ruta de ofertas
@app.route('/ofertas')
def ofertas():
    return 'Ofertas especiales disponibles hoy: Descuentos en laptops, celulares y accesorios.'

if __name__ == '__main__':
    app.run(debug=True)
