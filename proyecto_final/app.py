# app.py - proyecto_final
# Sistema: Tienda Online – Catálogo y Ofertas
# Tienda Online – Catálogo y Ofertas
# Proyecto Flask con plantillas dinámicas

from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta: Sobre la tienda
@app.route("/about")
def acerca_de():
    return render_template("about.html")

# Ruta: Productos
@app.route("/productos")
def productos():
    return render_template("productos.html")

# Ruta: Clientes
@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

# Ruta: Ofertas
@app.route("/ofertas")
def ofertas():
    return render_template("ofertas.html")

if __name__ == "__main__":
    app.run(debug=True)
