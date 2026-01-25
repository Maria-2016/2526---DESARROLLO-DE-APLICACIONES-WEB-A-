const productos = [
    {
        nombre: "Laptop",
        precio: 800,
        descripcion: "Equipo portátil para estudio y trabajo",
        imagen: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
    },
    {
        nombre: "Celular",
        precio: 500,
        descripcion: "Smartphone de última generación",
        imagen: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    },
    {
        nombre: "Accesorios",
        precio: 50,
        descripcion: "Accesorios tecnológicos",
        imagen: "https://images.unsplash.com/photo-1517433456452-f9633a875f6f"
    }
];

const lista = document.getElementById("listaProductos");

function mostrarProductos() {
    lista.innerHTML = "";

    productos.forEach(producto => {
        const li = document.createElement("li");

        li.innerHTML = `
            <img src="${producto.imagen}" width="150"><br>
            <strong>${producto.nombre}</strong><br>
            Precio: $${producto.precio}<br>
            ${producto.descripcion}
        `;

        lista.appendChild(li);
    });
}

document.getElementById("btnAgregar").addEventListener("click", () => {
    productos.push({
        nombre: "Nuevo producto",
        precio: 100,
        descripcion: "Producto agregado dinámicamente",
        imagen: "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    });

    mostrarProductos();
});

mostrarProductos();
